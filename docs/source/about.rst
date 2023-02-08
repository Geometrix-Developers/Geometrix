About Geometrix
===============

What it is
-----------------
Geometrix is a simple-to-use Python package that allows users to solve geometrical problems, which works similarly to a human mathematician.

Input of problem conditions
-----------------------------------
Input is done by adding a new piece of the conditions on every line; for example, to add a point, use `add_point(coordinates)` etc.

Solving mechanism
---------------------------
Our engine checks every single piece of data it is given on every theorem it knows, like a human, and if it finds a new piece of information, it adds it to the things it can use. Once it goes through every theorem, it starts again, using everything it now knows. After each cycle, it checks whether it found what it was asked to. All it does is logged into a file, from start to finish.

Unsolvable problems
-----------------------------------
In case a cycle finishes and no new data is obtained, the program returns an error message saying the conditions are insufficient to solve the problem.

Why it's a Python package
---------------------------
Our idea was that the program in the form of a Python package could be added into any other program, application or web-app, which would make it easier to use and give it more opportunities.

About the developers
--------------------
Geometrix's development was started in February 2023, and initiated by FoxyCoder. Soon after, FJSAGS joined Foxy in his mission to create the best geometry Python package ever made. They are working together to this day.

Foxy is a Python developer who specialises in making Discord bots and django-based websites. FJSAGS is also primarily a Python developer, who worked with Foxy on multiple occasions before Geometrix, for example on the Gobot Discord bot. Both developers have over 3 years of programming and Python experience.