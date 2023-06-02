import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="betterstar",
    version="0.0.1",
    author="Ole Meiforth",
    description="Better Star for matplotlib plots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=["betterstar"],
    package_dir={'':'betterstar/src'},
    install_requires=['numpy', 'matplotlib']
)