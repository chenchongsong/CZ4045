import nltk
import json
import matplotlib.pyplot as plt
import spacy
from nltk.corpus import stopwords
from collections import Counter
import random

progress_count = 0

def sentence_text(text, nlp):

    doc = nlp(text)

    sentences = [sent.string.strip() for sent in doc.sents]
    print(sentences[0])
    return sentences


#    return " ".join(tokens_stemmed)


if __name__ == "__main__":

    texts = [[] for _ in range(5)]
    nlp = spacy.load("en_core_web_sm")
    with open("reviewSelected100.json", encoding="ISO-8859-1") as f:
        for line in f:
            review = json.loads(line)
            rating = int(review["stars"])
            texts[rating - 1].append(review["text"])

    for i in range(5):
        len2num = Counter()

        for text in texts[i]:
            sentences = sentence_text(text, nlp)
            len2num[len(sentences)] += 1

        lens, nums = zip(*sorted(len2num.items()))

        plt.bar(lens, nums, label="Num of reviews for each sentence length")
        plt.legend()
        plt.xlabel("Length of Review")
        plt.ylabel("No. of Reviews")
        plt.title("Distribution of Review Lengths")
        plt.savefig("2_sentence_segmentation/fig{}".format(i + 1))
        # plt.show()
        plt.clf()

    random.seed()
    for i in range(5):
        curr_text = random.choice(texts[random.randint(0, 4)])
        print(curr_text)
        print(sentence_text(curr_text, nlp))
