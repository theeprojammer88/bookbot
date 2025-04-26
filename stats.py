def count_words(file_contents):
    word_count = file_contents.split()
    word_count = len(word_count)
    word_count = f"Found {word_count} total words"
    return word_count

def count_chars(file_contents):
    char_dict = {}
    chars = file_contents.lower()
    for char in chars:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(item):
    return item["num"]
    
def char_sort(char_dict):
    dict_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            new_dict = {"char": char, "num": count}
            dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sort_on)   
    return dict_list
