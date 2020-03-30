from setuptools import setup, find_packages


with open("README.md") as f:
    long_description = f.read()

setup(
    name="FileSplitter",
    version="2.1",
    packages=find_packages(),
    py_modules=["app"],
    entry_points={"console_scripts": ["filesplitter = app:main",]},
    exclude_package_data={
        "": ["CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "requirements.txt"]
    },
    author="Marco Orfei",
    author_email="marcoasrorfei@gmail.com",
    description="File splitter is a tool that split large file into multiple small file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="file splitter fs",
    url="https://github.com/asrmarco13/the-file-splitter",
    project_urls={
        "Bug tracker": "https://github.com/asrmarco13/the-file-splitter/issues",
        "Documentation": "https://github.com/asrmarco13/the-file-splitter/blob/master/README.md",
        "Source code": "https://github.com/asrmarco13/the-file-splitter",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
