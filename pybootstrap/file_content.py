GITIGNORE = """env/
__pycache__/
.vscode/
"""

def setup(name, desc):
    return f"""import setuptools

with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
    name="{name}",
    version="0.0.1",
    description="{desc}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
)
"""


def testpy(app_name):
    return f"""import unittest
from {app_name} import {app_name}


class TestAddFunc(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_app(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()

"""
