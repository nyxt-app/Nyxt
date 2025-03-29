from setuptools import setup, find_packages

setup(
    name="nyxt",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "flask",
    ],
    author="load",
    author_email="load@loaddev.xyz",
    description="Nyxt - Nyxt is a Python framework inspired by Next.js, designed to enable seamless navigation and dynamic components.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nyxt-app/nyxt",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)