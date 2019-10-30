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
    sample1 = "I love love their Kalbi, I always order it the sauce is what makes it really good."
    sample2 = "I reread the description of the burgetta burger and realized that I didn't even get the fried eggplant!"
    sample3 = "Good sushi, fast service!"
    sample4 = "With all the food groups covered, we had a really enjoyable time. "
    sample5 = "But he did ask me if I knew how to turn the temp knob. "
    sample = [sample1, sample2, sample3, sample4, sample5]
    pos_tagging(sample)
