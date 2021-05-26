"""
@author: Abhilash Raj

Module containing all the helper functions for the process
"""
import os # For file paths
import requests # For downlaoding files
from logger import log # For logging

def download_xml(url, download_path, filename):
    """Downloads the xml file in the download path
    Param(s):
        url (str)           :   download link of xml files
        download_path (str) :   path to download the xml
        filename            :   filename to give the downlaoded xml
    Return(s):
        xml_file (str)  :   absolute path to the downloaded xml file
    """
    xml_file = ''
    log.info('Downloading the xml file.')
    # Getting the content of the file
    response = requests.get(url)

    # Checking if the requests got a correct response
    if response.ok:
        # Creating directories in the given download path if not exists
        if not os.path.exists(download_path):
            os.makedirs(download_path)
        # Creating the filepath for downloading xml file
        xml_file = os.path.join(download_path,filename)

        # Creating the xml file at the path with the given file name
        with open(xml_file, 'w') as file:
            file.write(response.text)

        log.info('xml file downloaded')
    else:
        # Logging if the download of the xml file fails
        log.error('Error while downloading the xml file')

    return xml_file
