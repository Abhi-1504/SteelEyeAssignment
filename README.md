# SteelEyeAssignment
--------------------

The repository consist of the solution for SteelEye Python Developer Assignment.
The solution is Python 3 language and requires some additional libraries to be installed.

## Table of contents
--------------------

* controller.py
* helper_functions.py
* logger.py
* config.cfg

## Dependencies
---------------

This solution requires following python modules to be installed:

* os
* logging
* requests

## Configuration
----------------

In config.cfg file the following configuration needs to be done:

* download_path

The relative path from the current directory of the controller script where source and target xml files needs to be downloaded by the script, the script is creating absolute path during it's run.

* csv_path

The relative path from the current directory of the controller script where the csv file needs to be created by the script, the script is creating absolute path during it's run.




## Note to Evaluator
--------------------

Since the target XML file to be converted to csv is a large file, __ElementTree__ parser was few of the suitable parser to parse the same.
__ElementTree__ is not a reliable xml parser and it was unable to extract the text from element when __ElementTree.SubElement(parent_element, child_element_tag)__.
Hence, I had to use nested loop to extract the required data from the xml which in turn increases the time complexity of the solution
