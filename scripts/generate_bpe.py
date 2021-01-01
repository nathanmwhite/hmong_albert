#!/usr/bin/python

import os

import sentencepiece as spm

script_loc = os.path.dirname(__file__)
files_loc = os.path.join(os.path.dirname(script_loc), 'albert_raw_data')

# generates list of data files; sliced to -1 with topdown=False to exclude readme file in top folder
file_list = [os.path.join(root, filename) for (root,_,files) in os.walk(files_loc, topdown=False) for filename in files][:-1]

spm.SentencePieceTrainer.train(input=file_list, model_prefix='hm', vocab_size=50000, user_defined_symbols=[])




