from setuptools import setup, find_packages

setup(
    name="pets",
    version="0.0.3",
    description="IskayPet CLI",
    py_modules=[
        "pets",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
        "requests",
        "questionary",
    ],
    entry_points="""
        [console_scripts]
        pets=pets:cli
    """,
)
