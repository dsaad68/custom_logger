from setuptools import setup, find_packages

VERSION = '0.1.0'
DESCRIPTION = "Customizable logger with support for additional attributes"
LONG_DESCRIPTION = "This library provides a customizable logger with support for additional attributes, stream and file logging, as well as integration with Azure Application Insights."

setup(
        name="custom_logger",
        version=VERSION,
        author="Daniel Saad",
        author_email="<me@dsaad.com>",
        description=DESCRIPTION,
        long_description= LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["opencensus","opencensus-context","opencensus-ext-azure"],
        keywords=['python', 'first package'],
        classifiers= [
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)