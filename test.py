letter = 'a b c d e f g h i j k l'
list_letters = letter.split(' ')
print(list_letters)
string_tep = ''
for i ,l in enumerate(list_letters):
    string_tep += '|'
    string_tep += f' {l} '
    
    print(i)
    if i == len(list_letters) - 1:
        string_tep += '|'
print(string_tep)
