import spacy

nlp = spacy.load('en_core_web_sm')


if __name__ == "__main__":
    texts = [
        "This location was a surprise to me, even though I have been here a million times.",
        "I bought a wine and bar fridge in August, I was told that the wine fridge had two temps, it only had one.",
        "Gary, the sales person who said he'd check with the manager and he'd call me next day.",
        "They didn't have any menus in English when we arrived, but, luckily Google Translate saved my day.",
        "The Poutine was tasty with all its toppings and the burger patty was good.",
    ]
    for idx, text in enumerate(texts):
        doc = nlp(text)
        print("\nSentence #{}".format(idx))

        for entity in doc.ents:
            print("{0: <10} | {1: <10}".format(entity.label_, entity.text))
