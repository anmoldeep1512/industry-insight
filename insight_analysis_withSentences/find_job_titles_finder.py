from random import random

from find_job_titles import FinderAcora
import re

# def analyse():
#     finder=FinderAcora()
#     longest_match = finder.finditer(' avg Attrition Rate for UI/UX Designer is 18.9 % for fy2022-23. ')
#     try:
#         for match in longest_match:
#             print(match)
#     except StopIteration:
#         print("No more matches found.")
# [('Senior Vice President', 9),
#  ('Vice President', 16),
#  ('President', 21)]

# attrition, turn-over, rate, turn over, layoff, turnover, retention,

def has_job_title(text):
    finder = FinderAcora()
    text = str.title(str(text))
    longest_match = finder.finditer(text)
    # res = []
    try:
        for match in longest_match:
            return match
            # res.append(match)
        # return res
    except RuntimeError:
        return None


def find_title(list_report):

    dictionary = {}

    def get_percent(sentence, job):
        match_number = re.search(r"(\d+(\.\d+)?)\s*(?:%|percent|per[\s-]?cent)", str(sentence))

        if match_number:
            dictionary[job] = match_number.group(1)

        # print(dictionary, sentence, job, match_number.group(1))

    for sentence in list_report:
        matched = has_job_title(sentence)
        if matched is not None:
            job = matched.match
            get_percent(sentence, job)
        else:
            import spacy
            from spacy.pipeline import EntityRecognizer
            nlp = spacy.load("en_core_web_sm")

            doc = nlp(str(sentence))

            # Define a list of entity labels that correspond to job fields and departments
            job_fields = ["PROFESSION", "INDUSTRY", "FIELD", "AREA", "JOB_FIELD", "JOB"]
            departments = ["ORG", "GPE", "LOC", "DEPARTMENT"]

            for ent in doc.ents:

                if ent.label_ in job_fields:
                    job = ent.text
                    get_percent(sentence, job)
                elif ent.label_ in departments:
                    job = ent.text
                    get_percent(sentence, job)

    return dictionary


# def temp(text):
#     import spacy
#     from spacy.training import Example
#
#     # Load the pre-trained NLP model
#     nlp = spacy.load("en_core_web_sm")
#     doc = nlp(text)
#     for token in doc:
#         print("tag", token.tag)
#
#         print(token.text, token.ent_type_)

    # # prepare the training data
    # train_data = [
    #     ("I love my iPhone", {"entities": [(10, 16, "PRODUCT")]}),
    #     ("The Galaxy S10 is a great phone", {"entities": [(4, 12, "PRODUCT")]}),
    #     ("The Pixel 3 camera is amazing", {"entities": [(4, 10, "PRODUCT")]}),
    # ]
    #
    # # create a blank model and add the NER pipeline
    # nlp = spacy.blank("en")
    # ner = nlp.add_pipe("ner")
    #
    # # add the entity label to the model
    # ner.add_label("PRODUCT")
    #
    # # train the model
    # for text, annotations in train_data:
    #     doc = nlp.make_doc(text)
    #     example = Example.from_dict(doc, annotations)
    #     nlp.update([example], losses={})
    #
    # # test the model
    # test_data = ["I love my MacBook", "The OnePlus 7 is a great phone"]
    # for text in test_data:
    #     doc = nlp(text)
    #     for ent in doc.ents:
    #         print(ent.text, ent.label_)
    #
    # # save the model
    # nlp.to_disk("custom_ner_model")

    # # prepare the training data
    # train_data = [
    #     ("I love my iPhone", {"entities": [(10, 16, "PRODUCT")]}),
    #     ("The Galaxy S10 is a great phone", {"entities": [(4, 12, "PRODUCT")]}),
    #     ("The Pixel 3 camera is amazing", {"entities": [(4, 10, "PRODUCT")]}),
    # ]
    #
    # # create a blank model and add the NER pipeline
    # nlp = spacy.blank("en")
    # ner = nlp.add_pipe("ner")
    # ner.add_label("PRODUCT")
    # ner.add_label("O")  # add the "O" label for non-entity tokens
    #
    # # train the model
    # for text, annotations in train_data:
    #     doc = nlp.make_doc(text)
    #     example = Example.from_dict(doc, annotations)
    #     nlp.update([example], losses={})
    #
    # # test the model
    # test_data = ["I love my MacBook", "The OnePlus 7 is a great phone"]
    # for text in test_data:
    #     doc = nlp(text)
    #     for ent in doc.ents:
    #         print(ent.text, ent.label_)
    #
    # # save the model
    # nlp.to_disk("custom_ner_model")

    # # Define the new entity label
    # LABEL = "MY_ENTITY"
    #
    # # Create a new training example
    # text = "This is an example of MY_ENTITY"
    # entities = [(15, 24, LABEL)]
    # example = Example.from_dict({"text": text, "entities": entities}, nlp.vocab)
    #
    # # Add the example to the training data set
    # TRAIN_DATA = [example]
    #
    # # Train a new NER model using the updated training data set
    # nlp.disable_pipes("tagger", "parser")
    # ner = nlp.get_pipe("ner")
    # ner.add_label(LABEL)
    # optimizer = nlp.begin_training()
    # for i in range(10):
    #     random.shuffle(TRAIN_DATA)
    #     for example in TRAIN_DATA:
    #         nlp.update([example], sgd=optimizer)
    #
    # # Process new text and extract entities
    # doc = nlp("This is another example of MY_ENTITY")
    # for ent in doc.ents:
    #     print(ent.text, ent.label_)

    # Define the entity label
    # label = "MY_ENTITY"
    #
    # # Define the training data
    # text = "This is an example of MY_ENTITY"
    # entities = [(15, 24, label)]
    # example = Example.from_dict({"text": text, "entities": entities}, nlp.vocab)
    # train_data = [example]
    #
    # # Disable other pipes and update the model
    # other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
    # with nlp.disable_pipes(*other_pipes):
    #     optimizer = nlp.begin_training()
    #     for i in range(10):
    #         random.shuffle(train_data)
    #         losses = {}
    #         for batch in spacy.util.minibatch(train_data, size=2):
    #             nlp.update(batch, sgd=optimizer, drop=0.35, losses=losses)
    #         print(losses)


    # print("Inside temp")
    # import spacy
    # from spacy.pipeline import EntityRecognizer
    # nlp = spacy.load("en_core_web_sm")
    #
    # # text = "Our company is looking for an SDET and a solution architect to join our team"
    #
    # # define the custom labels for job fields and departments
    # job_fields = ["SDET", "solution architect"]
    # departments = ["engineering", "IT"]
    #
    # # define the getter function for the custom label "JOB_FIELD"
    # def get_job_field(ent):
    #     if ent.text in job_fields:
    #         print("returning")
    #
    #         return {"label": "JOB_FIELD"}
    #     print("returning none")
    #     return None
    #
    # # define the getter function for the custom label "DEPARTMENT"
    # def get_department(ent):
    #     if ent.text in departments:
    #         print("returning")
    #
    #         return {"label": "DEPARTMENT"}
    #     print("returning none")
    #     return None
    #
    # from spacy.tokens import Span
    # # add the getter functions to the Span extensions
    # Span.set_extension("job_field", getter=get_job_field)
    # Span.set_extension("department", getter=get_department)
    #
    # # process the text and extract the named entities
    # doc = nlp(text)
    # print("doc entries", doc.ents)
    # print("doc", doc)
    # for ent in doc.ents:
    #     print("in for ")
    #     if ent.label_ == "PERSON":
    #         print(f"Name: {ent.text}")
    #     elif ent._.job_field:
    #         print(f"Job Field: {ent.text}")
    #     elif ent._.department:
    #         print(f"Department: {ent.text}")
    #
    #     print(ent.text)
    #
    # print("outside temp")

# def try_spacy_for_titles(paragraph):

