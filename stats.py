def get_number_words(text):
    return len(text.split())

def get_char_count(text):
    char_count_dict = {}
    lower_text = text.lower()
    for char in lower_text:
        if char.isalpha():
            if char in char_count_dict:
                char_count_dict[char] += 1
            else:
                char_count_dict[char] = 1
    return char_count_dict

def sort_char_count(char_count):
    char_list = []
    for char in char_count:
        char_list.append({
            'char' : char,
            'count' : char_count[char]
        })
    char_list.sort(key=sort_on, reverse=True)
    #print(char_list)
    return char_list

def sort_on(dict):
    return dict['count']               
    