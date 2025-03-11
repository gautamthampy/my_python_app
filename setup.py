"""Setup file for my_app package."""

from setuptools import setup, find_packages

setup(
    name="my_app",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.8",
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple calculator application",
    keywords="sample, calculator, jenkins",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)