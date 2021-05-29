# -*- coding: utf-8 -*-
"""
@author: Abhilash Raj

Main controller module to perform the required steps
"""

from logger import log # For logging
from configparser import RawConfigParser # For loading config file
from helper_functions import * # Importing all the functions from helper_functions

# Gloabl Variable to store config object
config = None

def load_config():
    """Loads config file"""
    # Accessing config variable
    global config
    try:
        log.info('loading Config file.')
        # Loading config file
        config = RawConfigParser()
        config.read('config.cfg')
        log.info('Config file loaded successfully.')
    except Exception as e:
        log.error(f'Error in loading config file : {str(e)}.')
    return config

def main():
    """Controller function controlling the whole process"""

    log.info('Extracting xml source file url')
    # Extracting the source xml file url
    url = config.get('sourcefile', 'xml_source_url')

    log.info('Extracting xml source file url')
    # Extracting the download path and creating absolute path
    download_path = os.path.join(os.getcwd(),
                                config.get('download', 'download_path')
                                )
    print(download_path)
    log.info('Calling download function')
    # Calling the download helper function to download the file
    xml_file = download(url, download_path, 'sourcefile.xml')

    # Checking if the file download failed
    if not xml_file:
        print('File Download Fail, Kindly check logs for more details')
        print('Exiting...')
        return
    print(xml_file)
    log.info('Calling parse_source_xml function')
    # Calling the source xml file parser helper function to download the file
    file_metadata = parse_source_xml(xml_file)
    print(file_metadata)
    # Checking if the required file metadata extraction failed
    if not file_metadata:
        print('File Parsing Failed, Kindly check logs for more details')
        print('Exiting...')
        return

    # Extracting file name and file download link from file file_metadata
    filename, file_download_link = file_metadata

    log.info('Calling download function')
    # Calling the download helper function to download the file
    xml_zip_file = download(file_download_link, download_path, filename)

    if not unzip_file(xml_zip_file):
        print('Extration Failed, Kindly check logs for more details')
        print('Exiting...')
        return

    xml_file = os.path.join(download_path, filename)
    


if __name__ == '__main__':
    # Check for the config file loading
    if not load_config():
        print('Error while loading config file, check logs')
        print('Exiting...')
        # Exiting the script if the config files were not loaded
        exit(1)

    main()
