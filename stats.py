def get_num_words(text):
    words_list = text.split()
    return len(words_list)

def charcter_count(text):
    character_list = list(text.lower())
    character_dict = {}
    for char in character_list:
        if char not in character_dict:
            character_dict[char] = 1 
        else:
            character_dict[char] += 1
    return character_dict
    
def sorted_by_character_count(dict):
    sorted_list_by_keys = [{'char': k, 'count': v} for k,v in sorted(dict.items(), key=lambda x:x[1], reverse=True)]
    return sorted_list_by_keys