import setuptools
from pathlib import Path


root_dir = Path(__file__).absolute().parent
with (root_dir / "VERSION").open() as f:
    version = f.read()
with (root_dir / "README.md").open() as f:
    long_description = f.read()


setuptools.setup(
    name="ldap-trombi-py",
    description="Application générant un trombinoscope à partir d" "un LDAP",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    maintainer="Parcs national des Ecrins",
    maintainer_email="theo.lechemia@ecrins-parcnational.fr",
    url="https://github.com/PnEcrins/trombi",
    python_requires=">=3.6",
    version=version,
    packages=setuptools.find_packages("ldaptrombipy"),
    package_dir={"": "ldaptrombipy"},
    install_requires=list(open("requirements.in", "r")),
    classifiers=[
        "Framework :: Flask",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
)
