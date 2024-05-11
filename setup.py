from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path : str)->List[str]:
    '''
    This function is used to pull everything in the requirement.txt file and send it to install_requires
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:    
            requirements.remove(HYPEN_E_DOT)

    return requirements
setup(
    name='my_package',
    version='0.0.1',
    author='ARAVIND',
    author_email='aravindgrandhi1996@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)