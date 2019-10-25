import nltk
import string
from common import get_five_random_sentences

# Please Download the modules needed
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('universal_tagset')
    

def pos_tagging(sample):
    for text in sample:
        print(text)
        tokens = nltk.word_tokenize(text)

        # Filter out punctuations
        tokens = list(filter(lambda token: token not in string.punctuation, tokens))
        print(nltk.pos_tag(tokens))
        print('\n')


if __name__ == '__main__':
    sample = get_five_random_sentences()
    pos_tagging(sample)
