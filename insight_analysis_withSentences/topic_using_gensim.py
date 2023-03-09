# import nltk
# nltk.download('wordnet')      #download if using this module for the first time
#
#
# from nltk.stem import WordNetLemmatizer
# from nltk.corpus import stopwords
# nltk.download('stopwords')    #download if using this module for the first time
#
# import string
# stopwords = set(stopwords.words('english'))
# exclude = set(string.punctuation)
# lemma = WordNetLemmatizer()
#
# #For Gensim
# import
#  string
# from gensim import corpora
# from gensim.corpora.dictionary import Dictionary


def contains_keywords(text):
    keywords = ["attrition", "rate", "turnover", "turn over", "layoff", "retention", "turn-over"]
    for keyword in keywords:
        if keyword in text:
            return True
    return False


def extract_keyword_statement(report):
    final_sentences = []
    for sentence in report:
        if contains_keywords(sentence):
            final_sentences.append(sentence)

    return final_sentences


def using_spacy_find_topic(paragraph):
    import spacy
    nlp = spacy.load("en_core_web_sm")

    doc = nlp(paragraph)

    keywords = ["attrition", "rate", "turnover", "turn over", "layoff", "retention", "turn-over"]
    relevant_sentences = []
    for sentence in doc.sents:
        for token in sentence:
            if token.dep_ == "nsubj":
                topic = token.text
                for child in token.children:
                    if child.dep_ == "compound":
                        topic = child.text + " " + topic
                for keyword in keywords:
                    if keyword in topic and sentence not in relevant_sentences:
                        relevant_sentences.append(sentence)

    return relevant_sentences
