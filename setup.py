from setuptools import setup

setup(
    name="github-activity",
    version="0.1",
    # py_modules=["github_activity"],
    entry_points={
        "console_scripts": [
            "github-activity=main:main",
        ],
    },
)
