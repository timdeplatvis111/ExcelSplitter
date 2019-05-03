from setuptools import setup
from app import app 

app.run(
    debug = True
)

setup(
    name='flaskr',
    packages=['flaskr'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_mysqldb',
        'flask_sqlalchemy',
        'openpyxl',
    ],
)