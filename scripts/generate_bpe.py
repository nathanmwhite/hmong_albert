#!/usr/bin/python

import os

import sentencepiece as spm

file_list = os.listdir() # assuming this is already in the sch_corpus folder;
# will later need to update this with all relevant text files

spm.SentencePieceTrainer.train(input=file_list, model_prefix='hm', vocab_size=50000, user_defined_symbols=[])




