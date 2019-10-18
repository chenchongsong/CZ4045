import nltk
import json
import random
import string

# Download the modules needed 
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('universal_tagset')


def select_sentence(fname):
    text_list = []
    for line in open(fname, 'r', encoding='ISO-8859-1'):
        data = json.loads(line)
        text_list.append(data['text'])
    return random.sample(text_list, 5)
    

def pos_tagging(sample):
    for text in sample:
        print(text)
        tokens = nltk.word_tokenize(text)
        # Filter out punctuations
        tokens = list(filter(lambda token: token not in string.punctuation, tokens))
        print(nltk.pos_tag(tokens, tagset='universal'))
        print('\n')


if __name__ == '__main__':
    sample = select_sentence('../reviewSelected100.json')
    # sample = ['hello, I am huimin. And you?', "can't"]
    pos_tagging(sample)
