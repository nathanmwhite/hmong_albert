# hmong_albert

This repository holds the data for the _ALBERT for Hmong_ project as part of the Hmong Medical Corpus.

The project has the following dependencies:
* ALBERT (google-research/albert)
* SentencePiece (google/sentencepiece)

Current folders:
* albert_raw_data : Contains the raw text files for use in training.
* albert_raw_test_data : Contains the raw text files for use in testing.
* cased_data : Contains the preprocessed cased text data for use in training.
* scripts : Contains python script files for preprocessing.
* sentencepiece_model_files : Contains the SentencePiece model files for use with ALBERT.
* uncased_data : Contains the preprocessed uncased text data for use in training.

Current files:
* README.md : This file.
* bpe_stats.md : Contains information about the SentencePiece models trained on the data.

Deprecated:
* cased_data_deprecated : An older version of the preprocessed cased data.
* sentencepiece_model_files_deprecated : An older version of the SentencePiece models.
* uncased_data_deprecated : An older version of the preprocessed uncased data.
