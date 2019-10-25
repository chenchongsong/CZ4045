import json
import spacy
nlp = spacy.load("en_core_web_sm")


def get_all_review_texts():
    texts = []
    with open("reviewSelected100.json", encoding="ISO-8859-1") as f:
        for line in f:
            review = json.loads(line)
            texts.append(review["text"])
    return texts


def get_five_random_texts():
    texts = []
    selected_review_ids = ["Yj6KMH5yqZbNNW7XI7sZGA", "sAoRI1JTPVVBFe6sTZLtIA", "Wapj969gKpgov4CxhZZopQ", "6KH3TjQohetjjzB1dNj4ow", "0lkvydwiOkZ_9uDXU9X7Bw"]
    with open("reviewSelected100.json", encoding="ISO-8859-1") as f:
        for line in f:
            review = json.loads(line)
            if review["review_id"] in selected_review_ids:
                texts.append(review["text"])
    return texts


def get_five_random_sentences():
    texts = get_five_random_texts()
    sentences = []
    for text in texts:
        doc = nlp(text)
        for sent in doc.sents:
            sentences.append(sent.string.strip())
            break
    return sentences


if __name__ == "__main__":
    print("First randomly selected 5 reviews\n")
    texts = get_five_random_texts()
    for text in texts:
        print(text)
        print("\n")

    print("\nFirst Sentences from the 5 reviews above\n")
    sentences = get_five_random_sentences()
    for sent in sentences:
        print(sent)
