# Module Installation

# download module in local  
pip install .

# setup for pip repository
python setup.py sdist
twine upload --repository-url https://test.pypi.org/legacy/ dist/*