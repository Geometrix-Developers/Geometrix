from setuptools import find_packages, setup

setup(
    name='Geometrix',
    packages=find_packages(include=['Geometrix']),
    version='0.1.0',
    description='Automatic geometry problem solver in the shape of a Python library',
    author='FoxyCoder',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='Tests',
)
