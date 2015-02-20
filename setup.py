import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-adminflex',
    version='0.1',
    packages=['adminflex'],
    include_package_data=True,
    license='MIT',
    description='A simple Django app.',
    long_description=README,
    url='https://github.com/guoqiao/django-adminflex',
    author='Guo Qiao',
    author_email='guoqiao@gmail.com',
    install_requires=[
    ],
)
