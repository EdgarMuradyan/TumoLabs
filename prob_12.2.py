
def create_dict(text):
    key_word = ""

    word_dict = {}

    for i in text.split():
        key_word = i
        if key_word in word_dict:
            word_dict[key_word] += 1

        else:
            word_dict.update({key_word: 1})
        key_word = ""


    return word_dict

text = "ok good ok bad good good banana well banana "
print(create_dict(text))
