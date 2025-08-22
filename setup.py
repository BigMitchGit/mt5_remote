from setuptools import find_packages, setup

setup(
    name="mt5_remote",
    python_requires=">=3.11",
    packages=find_packages(include=["mt5_remote", "mt5remote", "mt5_remote.*"]),
    version="1.0.0",
    description="MetaTrader5 with remote access using a client/server architecture",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    author="BigMitchGit",
    license="MIT",
    url="https://github.com/bigmitchgit/mt5_remote",
    install_requires=open("requirements.txt", "r").read().split("\n"),
    setup_requires=[],
    tests_require=[],
    test_suite="tests",
)
