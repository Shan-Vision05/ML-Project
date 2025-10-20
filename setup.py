from setuptools import setup, find_packages


def GetRequirements(file_path):
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [package.strip().replace('\n','') for package in requirements if not package.strip().startswith('#')]
    return requirements[:-1] # Exclude the last line as it's not a package

setup(
    name="ml_project",
    version="0.0.1",
    author="Shanmukha Vamshi",
    author_email="shan.vk.05@gmail.com",
    packages=find_packages(),
    install_requires= GetRequirements('requirements.txt')
)