from setuptools import setup

setup(
    name="pets",
    version="1.1",
    py_modules=["pets"],
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
