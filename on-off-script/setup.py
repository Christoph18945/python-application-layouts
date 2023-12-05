# lots of ways doing packaging in python
# setup.py interacts withmany packaging and apllciations tools:
# tox -- harness for testing under multiple version of Python
# twine -- tool for uploading your package to pypi.org
# RealPython article on pipenv
# https://realpython.com/pipenv-guide/
SETUP_ARGS = dict(
    version="0.1.0",
    description=('Grabs the Hello World Wikipeida page and prints its title'),
    long_description="long_description",
    url='https://www.that-is-the-page.com',
    author_email="<EMAIL>",
    license="MIT",
    include_package_data=True,
    classifier=[
        'Developemt Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Progamming Language :: Python :: 3.12'
    ],
    py_modules = ['helloWorld',],
    install_requires = [
        'requests>=2.22',
    ],
)

if __name__ == "__main__":
    from setuptools import setup, find_packages
    SETUP_ARGS['packages'] = find_packages()
    setup(**SETUP_ARGS)