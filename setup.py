
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Data Models project (CS-784)',
    'author': 'Ali and Shaleen',
    'url': '',
    'download_url': 'Where to download it.',
    'author_email': 'alihitawala@cs.wisc.edu, shaleen.deep@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['Crawlers'],
    'scripts': [],
    'name': 'crawlers'
}

setup(**config)
