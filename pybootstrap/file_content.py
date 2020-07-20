def setup_content(name, author, email, desc, url):
    return f"""import setuptools

with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
    name="{name}",
    version="0.0.1",
    author="{author}",
    author_email="{emai}",
    description="{desc}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="{url}",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
)"""


def testpy_content(src_dir):
    return f"""import unittest
from {src_dir} import app

class TestAddFunc(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_app(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()"""
