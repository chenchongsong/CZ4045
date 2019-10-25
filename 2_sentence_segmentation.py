import json
import matplotlib.pyplot as plt
import spacy
from collections import Counter
import random
from common import get_five_random_texts

progress_count = 0


def sentence_text(text, nlp):
    doc = nlp(text)
    sentences = [sent.string.strip() for sent in doc.sents]
    print(sentences[0])
    return sentences


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
        plt.savefig("task2_fig{}".format(i + 1))
        # plt.show()
        plt.clf()


    # for sample 5 sentences
    for curr_text in get_five_random_texts():
        print(curr_text)
        print(sentence_text(curr_text, nlp))
