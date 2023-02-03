# Geometrix (v0.0.0)
Automatic geometry problem solver in the shape of a Python library

## About the project
Geometrix is a Python library that allows its users to input conditions of a maths problem, what the problem requires to find, and then finds the answer to the problem, checking what it can do and calculate using geometric theorems step-by-step, and eventually (if the problem is solvable) reaches an answer. This project was believed to be helpful to those struggling with easy and intermediate geometry, and make solving of simple, every-day work problems for mathematicians and engineers faster and less time-consuming, and for them not to be required to solve the problem themselves, to save time. The idea to integrate it into a Python library was from the belief it can have a wider range of uses in this format, and can be made into an application, a web app or any other form. 

## Development Stage
Very early (no releases)

## Installation Guide -- pre-relase
1. Clone this git repository to your device
2. Install twine, wheel, setuptools
3. Run `python setup.py bdist_wheel`
4. Copy the full path to the `.whl` file in the `dist` directory you just created
5. Run `pip install full/path/to/wheelfile.whl` wherever you woul like to use this package
6. Include `import Geometrix` in your code to import the library
