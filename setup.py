import os
from setuptools import setup, find_packages

module_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    setup(
        name="optimanage",
        version="0.0.1",
        description="Prioritizing computational workflows",
        long_description=open(os.path.join(module_dir, "README.md")).read(),
        packages=find_packages(),
        package_data={},
        python_requires='>=3.6',
    )
