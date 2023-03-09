# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import filter_percent
import topic_using_gensim
import find_job_titles_finder
import db
import make_sentences_from_db

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    report = filter_percent.open_document()
    # print(report)

    # percent_sentences = filter_percent.extract_percent_statement(report)
    # spacy_topic_find = topic_using_gensim.using_spacy_find_topic(percent_sentences)
    # dictionary_result = find_job_titles_finder.find_title(spacy_topic_find)

    # print("-------------------------------------percent---------------------------------------------")
    # print(percent_sentences)
    # print("-------------------------------------spacy---------------------------------------------")
    # print(spacy_topic_find)
    # print("-------------------------------------dictionary---------------------------------------------")
    # print(dictionary_result)

    # db.create_table()
    # db.add_dictionary_to_table(dictionary_result)

    final_output = make_sentences_from_db.get_sentence_from_db()
    for output in final_output:
        print(output)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
