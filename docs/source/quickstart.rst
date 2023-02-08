Quick Start Guide
=================

This page describes how to start using Geometrix in just a few minutes.

How to install the package
--------------------------
This guide describes how to install and import Gemetrix on your machine.

1. Go to https://github.com/Geometrix-Developers/Geometrix.
2. Clone the repository  to your machine.
3. Install everything in `requirements.txt`.
4. Run `python setup.py bdist_wheel` in the project's root directory terminal.
5. Go to the newly created `dist` and copy rhe **full** path of the `.whl` file in it.
6. Go to the directory where you want to use the package.
7. Install the package using `pip install full/path/you/copied.whl` whereever you plan to use it (on your machine).
8. Include `import Geometrix` in the imports of your program.

Congratulations! If you did everything correctly, you should be able to use the package on your machine now.
These next few steps show how to get started working with the simplest modules.

Simple functions
----------------
This guide tells about a few of the most important part of the pakage.

1. Create a `Workfield` instance and write it into a variable using `field = Geometrix.Workfield()`.
2. Add a point using `add_point(x-coord, y-coord)`, and write it into a variable, e.g  `point1 = field.add_point(1, 5)`
3. Add another point similarly
4. Connect them with `add_line(point1_id, point2_id)`. IDs of point are stored in your point variables' `id` attribute, so to make a line using our points we just created, run `field.add_line(point1.id, point2.id)`. IDs are assigned to points automatically.
5. Create another three points, and connect them all in a triangle using `tri1 = field.add_triangle(point3.id, point4.id,point5.id)`
6. Create another four points and connect them all in a quadrilateral using `quad1 = field.add_quadrilateral(point6.id, point7.id, point8.id)`. Points will be connected in the order you give them.
7. Make another point, and make a circle using `circ1 = field.add_circle(point9.id, 7)`, where the first arg is the ID of the centre point (it has to be created prior), and the second is the radius.

You are now able to create simple objects and connect them using Geometrix. Use the :doc:`reference` to learn more about the library.

How to create a local version of the documentation
--------------------------------------------------
This guide shows how to create a local version of the project's documentation.

1. Run `pip install sphinx` and `pip instal furo` in the root directory of your local version of Geometrix.
2. Navigate to the `docs` directory.
3. In it, run `sphinx-quickstart`. When prompted, answer `y` in the first prompt, and fill out the next three with antyhing you like.
4. Find one of the `make` files in the directory `docs`, and copy its full path.
5. In the terminal, run the `make` file with an attribute `html`, e.g on Windows: `path/to/make.bat html`
6. Navigate to the `build` directory just created in the `docs` directory you're already in
7. Find `index.html` in it and open it in a broswer.

You have now obtained a local copy of the project's documentation.
