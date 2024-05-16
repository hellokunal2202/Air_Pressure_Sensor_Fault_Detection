from setuptools import find_packages,setup # This is used to install the packages
from typing import List # This is used to define the type of the variable
NAME="sensor"
VERSION="0.0.1"
AUTHOR="Kunal_Mali"
AUTHOR_EMAIL_ID="malikunal2202@gmail.com"
REQUIREMENTS_FILE_NAME="requirements.txt"
HYPHEN_E_DOT="-e ."

## Function to get requirements from requirements.txt file
def get_requirements(file_path:str=REQUIREMENTS_FILE_NAME)->List[str]:
    requirements=[]

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    
    return requirements


setup(name=NAME,
version=VERSION,
author=AUTHOR,
author_email=AUTHOR_EMAIL_ID,
packages=find_packages(), ## This will automatically include all the packages in the project
install_requires = get_requirements() #['pandas','numpy','scikit-learn','pymongo']
)

