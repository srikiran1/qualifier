from setuptools import setup, find_packages

# PLEASE DO NOT EDIT THIS, MANAGED FOR CI PURPOSES
__QUALIFIER__ = ""

setup(
    name="qualifier",
    version="1.0.0" + __QUALIFIER__,
    description="A simple python project used for updating the qualifier part of the version for python projects.",
    author="Srikalyan Swayampakula",
    author_email="srikalyansswayam@gmail.com",
    url="https://github.com/srikalyan/qualifier",
    packages=find_packages(exclude=["*.tests"]),
    test_suite="qualifier.tests",
    setup_requires=[
        "pytest-runner",
    ],
    install_requires=[
    ],
    tests_require=[
        "mock",
        "pyhamcrest",
        "pytest",
        "pytest-cov",
    ],
    entry_points={
        "console_scripts": [
            "update_qualifier = qualifier.executor:main"
        ],
    },
)
