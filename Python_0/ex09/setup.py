from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    author="ochetrit",
    author_email="ochetrit@42.fr",
    description="A sample test package",
    long_description="This is a simple test package for \
    demonstration purposes.",
    long_description_content_type="text/markdown",
    url="https://github.com/ochetrit/ft_package",
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
