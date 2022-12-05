# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['profanity_filter', 'profanity_filter.analysis']

package_data = \
{'': ['*'], 'profanity_filter': ['data/*']}

install_requires = \
['cached-property>=1.5',
 'more-itertools>=8.0',
 'ordered-set-stubs>=0.1.3',
 'ordered-set>=3.0',
 'poetry-version>=0.1.3',
 'pydantic>=1.3',
 'pyyaml',
 'spacy>=2.0']

entry_points = \
{'console_scripts': ['profanity_filter = profanity_filter.console:main']}

setup_kwargs = {
    'name': 'profanity-filter',
    'version': '1.3.4',
    'description': 'A Python library for detecting and filtering profanity',
    'long_description': '# profanity-filter: A Python library for detecting and filtering profanity',
    'author': 'Roman Inflianskas',
    'author_email': 'infroma@gmail.com',
    'maintainer': 'Roman Inflianskas',
    'maintainer_email': 'infroma@gmail.com',
    'url': 'https://github.com/rominf/profanity-filter',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
