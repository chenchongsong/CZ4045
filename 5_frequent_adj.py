import json
import spacy
import math
from collections import Counter


nlp = spacy.load('en_core_web_sm')


def parse(f_name):
    ret = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: []
    }
    for line in open(f_name, 'r', encoding='ISO-8859-1'):
        data = json.loads(line)
        star = int(data['stars'])
        ret[star].append(data['text'])
    print('Done Parsing')
    return ret


def top10(f_name):
    tab = parse(f_name)
    occ = {
        1: {},
        2: {},
        3: {},
        4: {},
        5: {}
    }
    ret = {}
    counter = 0
    for rating in range(1, 6):
        text = tab[rating]
        for sentence in text:
            tokens = nlp(sentence)
            for token in tokens:
                if token.pos_ == 'ADJ':
                    word = token.text.lower()
                    if word in occ[rating]:
                        occ[rating][word] += 1
                    else:
                        occ[rating][word] = 1
            counter += 1
            if counter % 100 == 0:
                print(counter)
        tmp = Counter(occ[rating])
        ret[rating] = tmp.most_common(10)
    return ret


def indicative10(f_name):
    tab = parse(f_name)
    occ = {
        0: {},
        1: {},
        2: {},
        3: {},
        4: {},
        5: {}
    }
    tot = [0 for _ in range(6)]
    ret = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: []
    }
    for rating in range(1, 6):
        text = tab[rating]
        for sentence in text:
            tokens = nlp(sentence)
            for token in tokens:
                if token.pos_ == 'ADJ':
                    word = token.text.lower()
                    if word in occ[rating]:
                        occ[rating][word] += 1
                    else:
                        occ[rating][word] = 1
                    tot[rating] += 1
                    if word in occ[0]:
                        occ[0][word] += 1
                    else:
                        occ[0][word] = 1
                    tot[0] += 1
    for rating in range(1, 6):
        for word in occ[rating]:
            cnt = occ[rating][word]
            sum = occ[0][word]
            p = cnt / tot[rating]
            q = sum / tot[0]
            cnt = p * math.log2(p / q)
            ret[rating].append((word, cnt))
        ret[rating] = sorted(ret[rating], key=lambda x: x[1], reverse=True)[:10]
    return ret


if __name__ == '__main__':
    # tab = top10('../reviewSamples20.json')
    tab = top10('../reviewSelected100.json')
    print(tab)
    # tab = indicative10('../reviewSamples20.json')
    tab = indicative10('../reviewSelected100.json')
    print(tab)
