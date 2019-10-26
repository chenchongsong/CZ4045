import nltk
import string
    

def pos_tagging(sample):
    for text in sample:
        print(text)
        tokens = nltk.word_tokenize(text)

        # Filter out punctuations
        tokens = list(filter(lambda token: token not in string.punctuation, tokens))
        print(nltk.pos_tag(tokens))
        print('\n')


if __name__ == '__main__':
    sample = ["", "", "", "", ""]  # TODO put 5 sample sentences from each of the 5 reviews
    pos_tagging(sample)
