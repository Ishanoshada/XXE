from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Package requirements
requirements = [
    "requests>=2.25.0",
    "urllib3>=1.26.0",
    "lxml>=4.9.0",
    "defusedxml>=0.7.1",
    "python-dateutil>=2.8.2",
]


setup(
    name="xxe",
    version="0.1.5",
    author="Ishan Oshada",
    author_email="ishan.kodithuwakku.offical@gmail.com",
    description="A comprehensive XML External Entity (XXE) security testing toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ishanoshada/xxe",
    project_urls={
        "Bug Tracker": "https://github.com/ishanoshada/xxe/issues",
        "Documentation": "https://xxe.readthedocs.io/",
        "Source Code": "https://github.com/ishanoshada/xxe",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Topic :: Security",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "xxe-scan=xxe.cli:main",
        ],
    },
    keywords=[
        "security",
        "penetration-testing",
        "xml",
        "xxe",
        "security-testing",
        "vulnerability-scanner",
        "ethical-hacking",
        "xml-security",
    ],
    zip_safe=False,
    platforms="any",
)