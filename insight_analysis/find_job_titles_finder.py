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
    for sentence in list_report:

        matched = has_job_title(sentence)

        if matched is not None:
            job = matched.match
            match_number = re.search(r"(\d+(\.\d+)?)\s*(?:%|percent|per[\s-]?cent)", str(sentence))

            if match_number:
                dictionary[job] = match_number.group(1)

    return dictionary
