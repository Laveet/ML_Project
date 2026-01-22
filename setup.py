from setuptools import find_packages , setup
from typing import List

Hypen='-e .'
def get_requirements(file_path:str)->List:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if Hypen in requirements:
            requirements.remove(Hypen)
    return requirements
   

    

setup(
    name="Machine Learning Cycle",
    version="1.00",
    author="Laveet Kumar",
    author_email="laveetkumar5@gmail.com",
    packages=find_packages(),
    requires=get_requirements("requirements.txt")
    
)
# requires=get_requirements("requirements.txt")
# print(requires)