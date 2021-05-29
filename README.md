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

The solution is using following python modules:

* os
* boto3
* pandas
* zipfile
* logging
* requests
* xml.etree
* configparser

## Configuration
----------------

In config.cfg file the following configuration needs to be done:

* download_path

The relative path from the current directory of the controller script where source and target xml files needs to be downloaded by the script, the script is creating absolute path during it's run.

* csv_path

The relative path from the current directory of the controller script where the csv file needs to be created by the script, the script is creating absolute path during it's run.

* bucket_name

Provide the name of the S3 bucket to which file needs to be uploaded

* aws_access_key_id

Provide the AWS access key ID

* aws_secret_access_key

Provide the AWS secret access key

* region_name

Provide the AWS region in which the S3 bucket is hosted

## Files
--------

* config.cfg        : Configuration file consisting of paths and informations required for script to work.

* controller.py     : This is the main script that calls the specific function from helper_functions module to execute the steps for the assignment in the required sequence.

* helper_functions  : This module consists of all the functions that are performing individual steps mentioned in the Assignment.

* logger.py         : This module initializes logger which is being used in the helper_functions and controller script for logging.

## Note to Evaluator
--------------------

Since the target XML file to be converted to csv is a large file, __ElementTree__ parser was few of the suitable parser to parse the same.
__ElementTree__ is not a reliable xml parser and it was unable to extract the text from element when __ElementTree.SubElement(parent_element, child_element_tag)__.
Hence, I had to use nested loop to extract the required data from the xml which in turn increases the time complexity of the solution
