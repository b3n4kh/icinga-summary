import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="icinga2ve",
    version="0.0.1",
    author="Benjamin Akhras",
    author_email="b@akhras.at",
    description="Icinga Commandline Client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/b3n4kh/icinga-summary",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'tableformatter',
        'colored',
        'Click',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'icinga2ve=icinga2ve.cli:cli'
        ],
    },
    include_package_data=True,
    python_requires='>=3.6',
)
