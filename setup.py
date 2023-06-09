import pathlib

from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent
INSTALL_REQUIRES = (HERE / "requirements.txt").read_text().splitlines()
TESTS_REQUIRE = (HERE / "requirements-dev.txt").read_text().splitlines()[1:]
README, DEV_README = open("README.md").read().split('# Development')
setup(
    name="web-bricks",
    version="0.1.4",
    description="Page Object constructor for UI automation",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Yuriy Sagitov",
    author_email="pro100.ko10ok@gmail.com",
    python_requires=">=3.8.0",
    url="https://github.com/ko10ok/web-bricks",
    license="Apache-2.0",
    packages=find_packages(exclude=("tests",)),
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
