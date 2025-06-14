from setuptools import find_packages,setup

Hypen_e_dot = "-e ."

def get_requirements(file_path:str):
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)

setup (
    name="Diamond Price Predictor",
    version="0.0.1",
    author="Rajat Sarkar",
    author_email="sarkarrajat214@gmail.com",
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages(),
    
)
