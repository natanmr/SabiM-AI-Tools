from setuptools import setup, find_packages

# Read the content of README.md for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="SabiM-AI-Tools",  # Package name
    version="0.1.0",  # Initial version
    author="Natan Moreira Regis",  # Replace with your name
    author_email="natan.moreira.regis12@gmail.com",  # Replace with your email
    description="A Python package for analyse scientific articles using Large Language Models",
    long_description=long_description,  # Detailed description from README.md
    long_description_content_type="text/markdown",  # Format of the long description
    url="https://github.com/natanmr/SabiM-AI-Tools",  # Replace with your GitHub repo URL
    project_urls={  # Optional: additional URLs related to the project
        "Bug Tracker": "https://github.com/natanmr/SabiM-AI-Tools/issues",
        "Documentation": "https://your-docs-url.com",
    },
    classifiers=[  # Metadata about the package
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3",  # Update if using a different license
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    packages=find_packages(),  # Automatically find and include all Python packages in the directory
    python_requires=">=3.7",  # Minimum Python version required
    install_requires=[  # Dependencies needed to install and run the package
        "pandas",
        "pybtex"
    ],
    extras_require={  # Optional dependencies
        "dev": ["pytest", "black"],  # For development
        "docs": ["sphinx"],  # For generating documentation
    },
    include_package_data=True,  # Include additional files specified in MANIFEST.in
    entry_points={  # Define scripts/command-line tools
        "console_scripts": [
            "sabi-ai-tools=sabi_ai_tools.__main__:main",
        ],
    },
)
