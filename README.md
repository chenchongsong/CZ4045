# cz4045

### Requirements
- Python 3.6+

### Installation

Install requirements with pip

```shell
pip3 install -r requirements.txt
```

Download pretrained statistical models for SpaCy
```shell
python3 -m spacy download en_core_web_sm
```

Download model for NLTK
```shell
python
>>> import nltk
>>> nltk.download()
```

Place `reviewSelected100.json` under the root folder, so that the directory structure looks like this:
```
cz4045
   |——————assets
   |——————2_sentence_segmentation.py
   |       ...
   |——————7_named_entity_recognition.py
   └——————reviewSelected100.json
```

### Getting Started

To run task 2 - 7 :
```shell
python3 2_sentence_segmentation.py
python3 3_tokenization_stemming.py
python3 4_pos_tagging.py
python3 5_frequent_adj.py
python3 6_summarizer.py
python3 7_named_entity_recognition.py
```

