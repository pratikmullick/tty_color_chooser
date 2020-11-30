import setuptools

with open("README.md",'r') as fh:
    long_description=fh.read()

setuptools.setup(
    name="ttycolor-pkg-pratikmullick",
    version="0.8.1",
    author="Pratik Mullick",
    author_email="pratikmullick@protonmail.com",
    description="A program to change colors for TTY console in Linux",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pratikmullick/tty_color_chooser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)"
    ],
    python_requires='>=3.6',
)
