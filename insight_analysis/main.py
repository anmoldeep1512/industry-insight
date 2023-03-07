# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import filter_percent
import topic_using_gensim
import find_job_titles_finder

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    report = filter_percent.open_document()
    # print(report)
    percent_sentences = filter_percent.extract_percent_statement(report)
    # print("".join(percent_sentences))
    # topics = topic_using_gensim.analysis(percent_sentences)
    # for i in topics:
    #
    #     print("topics" , i)
    # sentences_with_keywords = topic_using_gensim.extract_keyword_statement(percent_sentences)

    # print(sentences_with_keywords)
    spacy_topic_find = topic_using_gensim.using_spacy_find_topic(percent_sentences)
    # print(spacy_topic_find)
    dictionary_result = find_job_titles_finder.find_title(spacy_topic_find)
    print(dictionary_result)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
