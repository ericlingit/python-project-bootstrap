import setuptools

with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pybootstrap-ericlingit",
    version="0.0.1",
    author="ericlingit",
    description="A python project folder bootstrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6',
)
