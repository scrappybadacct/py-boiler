from setuptools import setup

setup(
    name="example-nltk",
    version="0.0.1",
    author="Conor Fleming",
    author_email="conorfleming@outlook.com",
    description="an example nltk project",
    license="MIT",
    keywords="None",
    url="nope",
    packages=["app", "lib", "tests"],
    entry_points={"console_scripts": ["runme=app.app:main"]},
)
