from setuptools import setup

setup(
    name="pets",
    version="1.0",
    py_modules=["pets"],
    include_package_data=True,
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        pets=pets:cli
    """,
)