import random


class Vernam:
    string_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя_,.?!abcdefghijklmnopqrstuvwxyz1234567890-=+/|\:;@#№$%^&*' \
                      '~`…><[]"\'{}—()\n\t\r\a\f\v\b«»„“”‘’ '
    string_alphabet += string_alphabet.upper()

    def __init__(self, text):
        self.alphabet = list(map(str, self.string_alphabet))
        self.alphabet_dict = {index: ch for ch, index in enumerate(self.alphabet)}
        self.reversed_alphabet_dict = {ch: index for ch, index in enumerate(self.alphabet)}
        self.text = text
        self._keyword = ''.join([random.choice(self.alphabet) for i in range(len(text))])
        self._keyword_byte = self.byte(self._keyword)
        self.len_keyword_byte = len(self._keyword_byte)

    def return_key(self):
        return self._keyword

    def byte(self, text):
        operational_list = list(map(str, text))
        operational_list = [self.alphabet_dict.get(i) for i in operational_list]
        return operational_list

    def encode(self):
        text_byte_list = self.byte(self.text)
        for i in range(len(text_byte_list)):
            non_zero_added_coded_letter = str(text_byte_list[i] ^ self._keyword_byte[i % self.len_keyword_byte])
            text_byte_list[i] = '0'*(3 - len(non_zero_added_coded_letter)) + non_zero_added_coded_letter
        return ''.join(text_byte_list)

    def decode(self, text):
        text_list = []
        for i in range(0, len(text), 3):
            byte = int(text[i:i+3]) ^ self._keyword_byte[i//3 % self.len_keyword_byte]
            text_list.append(self.reversed_alphabet_dict.get(byte))
        return ''.join(text_list)

coder = Vernam(open('vernam_input.txt', 'r', encoding='utf8').read())
output = open('vernam_output.txt', 'w', encoding='utf8')
print('Key:', coder.return_key())
coded = coder.encode()
print('Coded view:', coded)
decoded = coder.decode(coded)
print('Decoded:', coder.decode(coded))
output.write('Key:\n' + coder.return_key() + '\n\nCoded view:\n' + coded + '\n\nDecoded view:\n' + decoded)