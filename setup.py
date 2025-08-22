from setuptools import find_packages, setup

setup(
    name="mt5-remote",
    python_requires=">=3.11",
    packages=find_packages(include=["mt5-remote"]),
    version="0.2.0",
    description="MetaTrader5 with remote access with a client/server architecture",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    author="BigMitchGit",
    license="MIT",
    url="https://github.com/bigmitchgit/mt5-remote",
    install_requires=open("requirements.txt", "r").read().split("\n"),
    setup_requires=[],
    tests_require=[],
    test_suite="tests",
)
