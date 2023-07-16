import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pgn2neo4j",
    version="0.0.1",
    author="Anton Forsman",
    description="Convert chess games (PGN:s) to a Neo4j database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=["pgn2neo4j"],
    package_dir={'':'pgn2neo4j/src'},
    install_requires=[
        "tqdm",
        "chess",
    ]
)