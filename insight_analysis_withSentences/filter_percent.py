def open_document():
    with open('data/analytics.txt', 'r') as file:
        report = file.readlines()
    return report


def contains_percent(text):
    keywords = ["%", "percent", "per-cent", "per cent"]
    for keyword in keywords:
        if keyword in text:
            return True
    return False


def extract_percent_statement(report):
    final_sentences = []
    for sentence in report:
        if contains_percent(sentence):
            final_sentences.append(sentence)
    return "".join(final_sentences)
