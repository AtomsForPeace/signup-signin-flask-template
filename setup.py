from setuptools import setup

setup(
    name='signup-signin-flask-template',
    version='0.2',
    description='Simple template for flask with a simple'
        'username/email/password signup, signin, and signout.',
    author='Adam Bannister',
    author_email='adam.p.bannister@gmail.com',
    url='',
    install_requires=[
        'flask>=0.12.3','flask-login==0.2.11',
        'sqlalchemy==0.9.9','flask-sqlalchemy==2.0',
        'flask-wtf==0.11', 'Flask-Migrate==1.5.0',
        'SQLAlchemy==0.9.9', 'WTForms==2.0.2',
        'sqlalchemy-migrate==0.9.7',
        ],
     )
