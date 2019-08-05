import re

""" Creates sorted list of lower-case words from title. """
def prepare_for_analysis(form_text):
    text = form_text.split()
    for word in range(len(text)):
        text[word] = text[word].lower()
        text[word] = re.sub(r'\W+', '', text[word]) # Removes non-alphanum
        if text[word] is '':
            text.pop(word)
    text.sort()
    return text

def word_analysis(form_text):
    words = prepare_for_analysis(form_text)
    word_dict = {}
    for word in words: # dict creation
        count = words.count(word)
        if word not in word_dict:
            word_dict[word] = count
    return word_dict

def display_word_analysis(word_dict):
    display_text = "<p>"
    display_text += "Word count: "
    text_length = 0
    for word in word_dict:
        text_length += word_dict[word]
    display_text += str(text_length) + "</p>"
    for word in word_dict:
        display_text += "<p><small>"
        percent = round(100 * word_dict[word] / text_length, 2)
        display_text += "<i>'{0}'</i> appears {1} times and consists of {2} percent of text.".format(word, word_dict[word], percent)
        display_text += "</small></p>"
    return display_text