from setuptools import setup, Extension
import os

def getfiles(root):
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            yield os.path.relpath(os.path.join(dirpath, filename))

test_deps = ["pytest"]

extras = {
    "testing": test_deps
}

setup(
    name = "makePDF",
    author = "Jonathan Keane",
    author_email = "jkeane@gmail.com",
    description = "",
    license = "MIT",
    version = "0.2.5",
    classifiers = ['Development Status :: 1 - Planning',
                   'Intended Audience :: Developers'],
    scripts = ['scripts/makePDF', 'scripts/makePDF.py'],
    packages = ["makePDF"],
    package_dir = {"": "src"},
    include_package_data=True,
    namespace_packages = ["makePDF"],
    install_requires = ["setuptools",
                        "img2pdf",
                        "Pillow"],
    tests_require = test_deps,
    extras_require = extras
)
