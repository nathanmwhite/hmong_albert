#!/usr/bin/python

# Byte-pair encoding script for Hmong ALBERT project
# Copyright (c) 2021 Hmong Medical Corpus Project
# Author : Nathan M. White <nathan.white1@my.jcu.edu.au>
"""
This script generates byte-pair encodings from the raw data
for the Hmong ALBERT model.
"""

import os

import sentencepiece as spm

# Copyright notice
__copyright__ = "Copyright (c) 2021 Hmong Medical Corpus Project"

# project_url
__url__ = "https://corpus.ap-southeast-2.elasticbeanstalk.com/hminterface"

# author
__author__ = "Nathan M. White"
__author_email__ = "nathan.white1@my.jcu.edu.au"

# central function of script
def generate_bpe(data_loc):
	"""
        Generates the byte-pair encodings based on the data found at 
         data_loc.
	@param data_loc : string consisting of the folder name containing
	                   the data, without any separators
        """

	# determines the absolute filepath for the files
	script_loc = os.path.dirname(__file__)
	files_loc = os.path.join(os.path.dirname(script_loc), data_loc)

	# generates list of data files; sliced to -1 with topdown=False
	#  to exclude readme file in top folder
	file_list = [os.path.join(root, filename) \
	             for (root,_,files) in os.walk(files_loc, topdown=False) \
	             for filename in files][:-1]

    # trains the model
	spm.SentencePieceTrainer.train(input=file_list,
								   model_prefix='hm.' + data_loc,
								   control_symbols=['[CLS]', '[SEP]', '[MASK]'],
								   vocab_size=50000,
								   user_defined_symbols=[])
								
if __name__ == '__main__':
    # generate byte-pair encodings on both uncased and cased data
    generate_bpe('uncased_data')
    generate_bpe('cased_data')								
