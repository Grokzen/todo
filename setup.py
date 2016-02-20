from setuptools import setup

setup(
    name='todocli',
    version='2.0.0',
    py_modules=['todo'],
    entry_points={
        'console_scripts': [
            'todo = todo:main'
        ]
    },
    install_requires=[
        'docopt==0.6.2',
    ],
    test_suite='tests',
    author='foobuzz',
    author_email='dprosium@gmail.com',
    description='A command line todo list manager',
    keywords='command line todo list',
    url='https://github.com/foobuzz/todo'
)
