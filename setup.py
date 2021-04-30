import setuptools
import re

ver = ''
with open("tags/__init__.py") as f:
    ver = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

readme = ''

with open("README.md") as f:
    readme = f.read()

setuptools.setup(
    name='tags.py',
    author='priguy914629',
    version = ver,
    url='https://github.com/proguy914629bot/tags.py',
    license='MIT',
    description='A Tag helper.',
    long_description=readme,
    long_description_content_type="text/markdown",
    python_requires=">=3.5"
)
