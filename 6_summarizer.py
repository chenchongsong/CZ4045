import spacy

nlp = spacy.load("en_core_web_sm")

sample_doc1 = nlp("""
    I ordered the sea bass special. It was to die for. Cooked perfectly, seasoned perfectly, perfect portion.
    I can not say enough good things about this dish.
    When the server asked how it was he seemed very proud of the dish and said, \" doesn't she (the chef) do an incredible job?\"
    She does. My hubby got the crab tortellini and also loved his.
    I heard \"mmmm this is so good\" from all around the table.
    Our waiter was super nice and even gave us free desserts because we were some of the last people in the restaurant.
    Service was very slow and the place was PACKED but we had our jugs of wine and a large group with good conversation so it didn't seem to bother anyone.
    So-Do order the calamari and fried zucchini appetizers. Leave out the mussels.
    If they have the sea bass special, I highly recommend it.
    The chicken parm and crab tortellini were also very good and very big.
    The chicken Romano was a bit bland. The house salads were teeny.
    Do make a reservation but still expect to wait for your food.
    Go with a large group of people and plan for it to be loud.
    Don't go with a date unless you're fighting and don't feel like hearing anything they have to say. 
    Ask to sit in the side room if it's available.""")


def get_noun_adj_pairs(doc):
    result_pairs = []
    for token in doc:
        if token.pos_ == "ADJ" and token.dep_ == "amod":
            if token.head.pos_ == "NOUN":
                result_pairs.append((token.head.text, token.text))

        if token.pos_ in ["NOUN", "PROPN"] and token.dep_ == "nsubj":
            noun_list = [token]
            for noun in noun_list:
                for child in noun.children:
                    if child.pos_ in ["NOUN", "PROPN"] and child.dep_ == "conj" and child not in noun_list:
                        noun_list.append(child)

            adj_list = []
            for r in token.head.rights:
                if r.pos_ == "ADJ":
                    adj_list.append(r)
                    break
            for adj in adj_list:
                for child in adj.children:
                    if child.pos_ == "ADJ" and child.dep_ == "conj" and child not in adj_list:
                        adj_list.append(child)
                        break

            for noun in noun_list:
                for adj in adj_list:
                    result_pairs.append((noun.text, adj.text))

    return result_pairs


if __name__ == "__main__":
    doc_demo = nlp("The chicken parm, and crab tortellini were also very good and very big.")
    for token in doc_demo:
        print(token.text, token.dep_, token.head.text, token.head.pos_, [child for child in token.children], token.pos_, token.tag_)
    print(get_noun_adj_pairs(doc_demo))
    print(get_noun_adj_pairs(sample_doc1))
