clean_word = input().strip('{').strip('}')
print(len(set(clean_word.split(', ')))) if len(clean_word) != 0 else print(0)