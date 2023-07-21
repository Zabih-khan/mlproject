from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    '''
    This function reads a requirements.txt file and returns the list of requirements.
    It will remove the newline character from the end of each requirement.
    '''
    requirements = []
    with open(file_path) as file_obj:
        # Read the lines of the requirements.txt file
        requirements = file_obj.readlines()
        # Remove the newline character from the end of each requirement
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

# Setup configuration for the project
setup(
    name="mlproject",  # Name of the project
    version='0.0.1',   # Version number
    author='Zabih',    # Author's name
    author_email='Zabihullah18381@gmail.com',  # Author's email
    packages=find_packages(),  # Find all packages in the project
    install_requires=get_requirements('requirements.txt')  # Set the project dependencies from requirements.txt
)




"""
The setup.py file is an important part of building and distributing Python packages, as it contains the necessary information for building and installing your package. By using the pip tool and the setup.py file, you can easily share your Python packages with others and make them available for use in their own projects.
"""

















