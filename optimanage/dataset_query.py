from pymatgen.ext.matproj import MPRester
import json


def get_materials_with_elastic_tensors(filepath):
    """
    Queries MP for materials with computed elastic tensors and writes
    the mp_ids and elastic_tensors to a json
    """
    with MPRester() as m:
        res = m.query(criteria={"elasticity.elastic_tensor": {"$exists": 1}},
                      properties=["task_id", "elasticity.elastic_tensor"])
        with open(filepath, 'w+') as fp:
            json.dump(res, fp, indent=4)
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
            json.dump(toy_data, toy, indent=4)
            print("Removed {} elastic tensors from the full dataset {}."
                  .format(removed_count, total_count))


if __name__ == "__main__":
    # get_materials_with_elastic_tensors("full_elastic_dataset.json")
    # make_toy_elastic_dataset("full_elastic_dataset.json", "toy_dataset.json")
