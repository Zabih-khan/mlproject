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
setup() is like a special tool that comes with a Python package called "setuptools." It helps you manage and share your Python programs with others easily.

Imagine you made a cool program using Python, and you want to share it with your friends or even the whole world! Well, that's where setup() comes in. It helps you prepare your program so that people can install it on their own computers and use it.

To get your program ready for sharing, you create a special file called "setup.py." In this file, you use the setup() tool to tell Python some important things about your program, like its name, version, what it does, and even what other programs it needs to work.

"""

















