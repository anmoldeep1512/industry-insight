import db
import random

def get_sentence_from_db():
    templates = ["The observed attrition rate for {Track} is of {Percent}%.",
                 "The average attrition rate for {Track} stands at {Percent}%.",
                 "According to industry data, the average attrition rate for {Track} is {Percent}%.",
                 "The attrition rate in the {Track} market stands at {Percent}%."]

    data = db.get_attrition_insight()
    final_sentences = []
    for curr_attr in data:
        template = random.choice(templates)
        sentence = template.format(Track=curr_attr[0], Percent=curr_attr[1])
        final_sentences.append(sentence)

    return final_sentences
