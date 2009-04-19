Pywind is a collection of scripts for generating 3D CAD models of airfoils to be used in the design of wind turbine blades.

At present, it is able to generate a part consisting of a series of arbitrarily transformed splines in Solidworks from the combination of a .CSV file and an airfoil profile in Selig format. The code is still very brittle and poorly tested, but the basic functionality is there.

Rough steps for use, until either forever or I have time to 
write more documentation:

0. Realize that this code is far from mature. The Solidworks macro, in particular, is sketchy.

1. Run the Python script called pyairfoil.py in the same directory as testfoil.csv and sd6060.dat. (Change the filenames to whatever you want, but your new names and pyairfoil.py must be consistent.) It will output a file called airfoil.txt.

2. Check that airfoil.txt has 61 * 6 = 366 lines of nonnegative coordinates, followed by a single blank line. Total filesize should be 8.9 kB. Move airfoil.txt to C:\airfoil.txt on the Windows machine you will use to run Solidworks.

3. Create a new part in Solidworks.

4. Run the macro CreateAirfoilPart.swp.

5. If airfoil.txt is parsed successfully, you will see a Solidworks alert to that end.

6. Hope that the macro doesn't crash. If it does, click "Debug" and see where. Send Brandon an error report.

## Developer contact info ##

[Brandon Stafford](http://pingswept.org)

brandon at pingswept org

