try:
    from setuptools import setup
except ImportError:
    from distributed import setup

config = {
    'description': "My Test Project",
    'author': "pengliheng",
    'url': "https://github.com/pengliheng/python",
    'download_url': 'https://github.com/pengliheng/python',
    'author_email': 'My email',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)