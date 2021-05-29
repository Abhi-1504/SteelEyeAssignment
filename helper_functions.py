"""
@author: Abhilash Raj

Module containing all the helper functions for the process
"""
import os # For file paths
import requests # For downlaoding files
from logger import log # For logging
from xml.etree import ElementTree as ET# To Parse XML

def download(url, download_path, filename):
    """Downloads the given file in the download path
    Param(s):
        url (str)           :   download link of file
        download_path (str) :   path to download the file
        filename            :   filename to give the downlaoded xml
    Return(s):
        file (str)  :   absolute path to the downloaded xml file
    """
    file = ''
    log.info('Downloading the xml file.')
    try:
        # Getting the content of the file
        response = requests.get(url)

        # Checking if the requests got a correct response
        if response.ok:
            # Creating directories in the given download path if not exists
            if not os.path.exists(download_path):
                os.makedirs(download_path)
            # Creating the filepath for downloading xml file
            file = os.path.join(download_path,filename)

            # Creating the xml file at the path with the given file name
            with open(file, 'wb') as f:
                f.write(response.content)

                log.info('xml file downloaded')
        else:
            # Logging if the download of the xml file fails
            log.error('Error while downloading the xml file')
    except Exception as e:
        # Logging if the download of the xml file fails
        log.error(f'Error occurred - {str(e)}')

    return file


def parse_source_xml(xml_file):
    """Function to Parse the provided xml
    Param(s):
        xml_file (str)  :   Path to the xml file
    Return(s):
        download_link   :   Link to download target xml file
    """
    try:
        log.info('Loading the xml file.')
        # Loading the xml file content
        xmlparse = ET.parse(xml_file)

        log.info('Parsing the xml file.')
        # Getting the required xml root (<result>)
        root = xmlparse.getroot()[1]
        # Getting all the doc tag elements
        docs = root.findall('doc')

        log.info('Traversing all the doc elements.')
        # Traversing through all the doc tag elements
        for doc in docs:

            log.info('Extracting the file type')
            # Extracting file type of the doc
            file_type = doc.find(".//str[@name='file_type']")

            # Checking if the file type of the doc 'DLTINS'
            if file_type.text == 'DLTINS':

                log.info('Match found for file type DLTINS')

                # Extracting the File name and download link from the xml
                log.info('Extracting the file name')
                file_name = doc.find(".//str[@name='file_name']").text

                log.info('Extracting the file download link')
                download_link = doc.find(".//str[@name='download_link']").text

                # Breaking out of the loop since we got the first file download
                # link with file type 'DLTINS'
                break
        else:
            log.info('Match not found for file type DLTINS')
            # Returning from the function if not matches of file type found
            return

        return file_name, download_link

    except Exception as e:
        log.error(f'Error occurred - {str(e)}')



def unzip_file(zipped_file):pass

def create_csv(xml_file):pass

def aws_s3_upload():pass
