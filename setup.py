import codecs
import os.path
from setuptools import find_packages, setup


here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

tests_require = [
    "flake8",
    "pytest",
    "pytest-cov",
    "tox",
]

setup(
    name="aio-web-sandbox",
    use_scm_version={
        "root": here,
        "write_to": os.path.join(here, "foo/_version.py"),
    },
    description="What is foo",
    long_description=long_description,
    packages=find_packages(where=here),
    entry_points={
        "console_scripts": [
            "foo = foo:main",
        ],
    },

    install_requires=[
        "aiohttp",
        "aiopg",
        "alembic",
        "sqlalchemy",
    ],
    setup_requires=[
        "pytest-runner",
        "setuptools_scm>=1.10.1,<2.0.0",
    ],
    tests_require=tests_require,
    extras_require={
        "tests": tests_require,
    },

    classifiers=[
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",

        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
    ],
)
