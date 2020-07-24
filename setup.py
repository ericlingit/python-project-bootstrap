import setuptools

with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pybootstrap-ericlingit",
    version="0.0.1",
    author="ericlingit",
    author_email="ericlingit@users.noreply.github.com",
    description="A python project folder bootstrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ericlingit/python-project-bootstrap",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Topic :: Software Development",
    ],
    python_requires='>=3.6',
)
