def get_words_num(bookdata):
    words = bookdata.split() # Splits the string into a list of words
    word_count = len(words)
    return word_count

def count_characters(s):
    counts = {}
    for char in s.lower():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_on(items):
    return items["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list