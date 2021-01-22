#!/usr/bin/python

# Casing script for Hmong ALBERT project
# Copyright (c) 2020-2021 Hmong Medical Corpus Project
# Author : Nathan M. White <nathan.white1@my.jcu.edu.au>
"""
This file contains the script that generates
cased and uncased data as input to the
byte-pair encoding generator script.
"""

import logging
import os
import re

logging.basicConfig(level=logging.INFO)

# Copyright notice
__copyright__ = "Copyright (c) 2020-2021 Hmong Medical Corpus Project"

# project_url
__url__ = "https://corpus.ap-southeast-2.elasticbeanstalk.com/hminterface"

# author
__author__ = "Nathan M. White"
__author_email__ = "nathan.white1@my.jcu.edu.au"

# relative folder specifications in project
root_loc = os.path.dirname(os.path.dirname(__file__))
source_loc = os.path.join(root_loc, 'albert_raw_data')

uncased_folder = 'uncased_data'
cased_folder = 'cased_data'

# central function of script
def run_casing_script():
    """
    This script access each file in the raw data and produces
    two processed datasets: one cased and the other uncased.
    """
    for (root, _, files) in os.walk(source_loc, topdown=True):
        rootpath_parts = root.split('albert_raw_data')
        try:
            os.mkdir(rootpath_parts[0] + uncased_folder + rootpath_parts[1])
            os.mkdir(rootpath_parts[0] + cased_folder + rootpath_parts[1])
        except:
            pass
            
        for filename in files:
            if filename != "README.md":
                in_filename = os.path.join(root, filename)
                in_file = open(in_filename, 'r')
                in_file_lines = in_file.readlines()
                in_file.close()

                # generate uncased data file
                filepath_parts = in_filename.split('albert_raw_data')
                out_filename = filepath_parts[0] + uncased_folder + filepath_parts[1]                    
                out_file = open(out_filename, 'w')
                for line in in_file_lines:
                    out_file.write(line.lower())
                out_file.close()
                logging.info('Successfully wrote uncased ' + os.path.basename(out_filename))
                
                
                # generate cased data file
                out_filename = filepath_parts[0] + cased_folder + filepath_parts[1]
                out_file = open(out_filename, 'w')
                for line in in_file_lines:
                    out_line = re.sub('([A-Za-z0-9])([.,?!\-:;\'"()])', '\g<1> \g<2>', line)
                    out_line = re.sub('([.,?!\-:;\'"()])([A-Za-z0-9])', '\g<1> \g<2>', out_line)
                    out_file.write(out_line)
                out_file.close()
                logging.info('Successfully wrote cased ' + os.path.basename(out_filename))

if __name__ == '__main__':
    run_casing_script()
