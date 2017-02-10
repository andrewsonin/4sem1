input_list = list(open('freq_input.txt', 'r', encoding='utf8').read().lower())
output_file = open('freq_output.txt', 'w', encoding='utf8')
data_list = []
for i in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
    data_list.append((i, input_list.count(i)))
data_list = sorted(data_list, key=lambda x: x[1], reverse=True)
for element in data_list:
    output_file.write(' '.join(map(str, element)) + '\n')
