from pymatgen.ext.matproj import MPRester
import json
from monty.json import MontyEncoder, MontyDecoder
from pymatgen import Structure

try:
    from pydash import chunk as get_chunks
except ImportError:
    from math import ceil

    def get_chunks(array, size=1):
        chunks = int(ceil(len(array) / float(size)))
        return [array[i * size:(i + 1) * size]
                for i in range(chunks)]

try:
    # import `tqdm_notebook` for prettier output in Jupyter Notebook
    from tqdm import tqdm as PBar
except ImportError:
    class PBar():
        def __init__(self, total):
            self.total = total
            self.done = 0
            self.report()

        def update(self, amount):
            self.done += amount
            self.report()

        def report(self):
            print("{} of {} done {:.1%}".format(
                self.done, self.total, self.done/self.total))


def bulk_query(self, criteria, properties, chunk_size=100, **kwargs):
    data = []
    mids = [d["material_id"] for d in
            self.query(criteria, ["material_id"])]
    chunks = get_chunks(mids, size=chunk_size)
    progress_bar = PBar(total=len(mids))
    if not isinstance(criteria, dict):
        criteria = self.parse_criteria(criteria)
    for chunk in chunks:
        chunk_criteria = criteria.copy()
        chunk_criteria.update({"material_id": {"$in": chunk}})
        data.extend(self.query(chunk_criteria, properties, **kwargs))
        progress_bar.update(len(chunk))
    return data


MPRester.bulk_query = bulk_query


def get_materials_with_elastic_tensors(filepath, desired_properties):
    """
    Queries MP for materials with computed elastic tensors and writes
    the mp_ids and elastic_tensors to a json
    """
    assert isinstance(desired_properties, set)
    with MPRester() as m:
        needed_properties = set(["task_id", "elasticity"]) \
                            | desired_properties
        print(needed_properties)
        res = m.bulk_query(criteria={"elasticity.elastic_tensor":
                                     {"$exists": 1}},
                           properties=list(needed_properties))
        print(type(res[1]["elasticity"]))
        with open(filepath, 'w+') as fp:
            json.dump(res, fp, indent=4, cls=MontyEncoder)
        print("Dumped {} results into {}".format(len(res), filepath))


def make_toy_elastic_dataset(full_dataset_filepath, toy_filepath):
    """
    Removes elastic tensors from half of the full dataset
    so that we can simulate "unknown" elastic tensors.
    This is chosen pseudo-randomly by looking at mp-id mod 2.
    """
    with open(full_dataset_filepath) as full_data:
        with open(toy_filepath, 'w+') as toy:
            all_data = json.load(full_data)
            toy_data = []
            removed_count = 0
            total_count = len(all_data)
            for data in all_data:
                if ((int)(data['task_id'].split('-')[1])) % 2 == 0:
                    del(data['elasticity.elastic_tensor'])
                    toy_data.append(data)
                    removed_count += 1
                else:
                    toy_data.append(data)
            json.dump(toy_data, toy, indent=4, cls=MontyEncoder)
            print("Removed {} elastic tensors from the full dataset {}."
                  .format(removed_count, total_count))


if __name__ == "__main__":
    properties_to_query = set()
    get_materials_with_elastic_tensors("full_elastic_dataset2.json",
                                       properties_to_query)
    # make_toy_elastic_dataset("full_elastic_dataset2.json", "toy_dataset2.json")
