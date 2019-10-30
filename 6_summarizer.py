import spacy
from collections import Counter
from common import get_five_random_businesses

nlp = spacy.load("en_core_web_sm")


def concat_noun_with_compound(noun):
    for child in noun.children:
        if child.pos_ in ["NOUN", "PROPN"] and child.dep_ == "compound":
            return child.text + " " + noun.text
    return noun.text


def concat_adj_with_adv(adj):
    for child in adj.children:
        if child.pos_ == "ADV" and child.dep_ == "advmod":
            return child.text + " " + adj.text
    return adj.text


def get_noun_adj_pairs(doc):
    result_pairs = []
    for token in doc:

        # for adjectives as "amod" (adjectival modifier)
        # e.g. a red and fresh apple
        if token.pos_ == "ADJ" and token.dep_ == "amod":
            if token.head.pos_ in ["NOUN", "PROPN"]:
                noun_list = [token.head]
                adj_list = [token]
                for child in token.children:
                    if child.pos_ == "ADJ" and child.dep_ == "conj":
                        adj_list.append(child)

                for noun in noun_list:
                    for adj in adj_list:
                        noun_string = concat_noun_with_compound(noun)
                        adj_string = concat_adj_with_adv(adj)
                        result_pairs.append((noun_string, adj_string))

        # for adjectives as "acomp" (adjectival complement)
        # e.g. The apple is red and fresh.
        if token.pos_ in ["NOUN", "PROPN"] and token.dep_ == "nsubj":
            noun = token
            noun_list = [noun]

            for child in noun.children:
                if child.pos_ in ["NOUN", "PROPN"] and child.dep_ == "conj" and child not in noun_list:
                    noun_list.append(child)

            adj_list = []
            for r in noun.head.rights:  # find the first adjective after the noun
                if r.pos_ == "ADJ":
                    adj_list.append(r)
                    break
            if len(adj_list) == 0:
                continue
            adj = adj_list[0]
            for child in adj.children:
                if child.pos_ == "ADJ" and child.dep_ == "conj" and child not in adj_list:
                    adj_list.append(child)

            for noun in noun_list:
                for adj in adj_list:
                    noun_string = concat_noun_with_compound(noun)
                    adj_string = concat_adj_with_adv(adj)
                    result_pairs.append((noun_string, adj_string))

    return result_pairs


if __name__ == "__main__":
    print("Top 5 common <noun, adj> pairs for each of the 5 businesses:")
    businesses = get_five_random_businesses()
    for business_id, texts in businesses.items():
        assert len(texts) == 100
        counter = Counter()

        for text in texts:
            doc = nlp(text)
            pairs = get_noun_adj_pairs(doc)
            for pair in pairs:
                noun, adj = pair
                counter[(noun.lower(), adj.lower())] += 1

        top5_pairs = counter.most_common(5)
        print(top5_pairs)

    print("\nDemo sentences:")
    text_demo_1 = "The crab and chicken wings were also great and extremely big."
    doc_demo_1 = nlp(text_demo_1)
    # crab     <-------------- were
    # wings    <-----conj----- crab
    # chicken  <---compound--- wings
    #
    # great    <-------------- were
    # big      <-----conj----- great
    # extremely<----advmod---- big

    print(text_demo_1)
    print(get_noun_adj_pairs(doc_demo_1))
    print("\n")

    text_demo_2 = "A popular and nice dish!"
    doc_demo_2 = nlp(text_demo_2)
    # popular <---amod--- dish
    # nice    <---conj--- popular
    print(text_demo_2)
    print(get_noun_adj_pairs(doc_demo_2))

