import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAEME = "kiran-001"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "kirankumarnimakayala@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAEME,
    author_email=AUTHOR_EMAIL,
    description="Python ackage for NLP application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAEME}/{REPO_NAME}/issues",
    project_urls={"Bug Tracker": f"https://github.com/{AUTHOR_USER_NAEME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
    )
