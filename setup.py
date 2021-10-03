import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

Project_Name = "ANN-implementation-demo"
user_name = "guptabhishek8"


setuptools.setup(
    name=f"{Project_Name}-{user_name}",
    version="0.0.1",
    author=user_name,
    author_email="guptabhishek8@gmail.com",
    description=" A small package for ANN implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{user_name}/{Project_Name}",
    project_urls={
        "Bug Tracker": f"https://github.com/{user_name}/{Project_Name}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        "tensorflow",
        "matplotlib",
        "seaborn",
        "numpy",
        "pandas"
    ]
)
