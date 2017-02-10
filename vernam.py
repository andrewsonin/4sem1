import random


class Vernam:
    def __init__(self):
        self.string_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя _,.' \
                               '?!abcdefghijklmnopqrstuvwxyz1234567890-=+/|\:;@#№$%^&*~`…><[]"\'{}'
        self.string_alphabet += self.string_alphabet.upper()
        self.alphabet = list(map(str, self.string_alphabet))
        self.alphabet_dict = {index: ch for ch, index in enumerate(self.alphabet)}
        self.reversed_alphabet_dict = {ch: index for ch, index in enumerate(self.alphabet)}
        self._keyword = ''.join([random.choice(self.alphabet) for i in range(random.randint(40, 100))])
        self._keyword_byte = self.byte(self._keyword)
        self.len_keyword_byte = len(self._keyword_byte)

    def return_key(self):
        return self._keyword

    def byte(self, text):
        operational_list = list(map(str, text))
        operational_list = [self.alphabet_dict.get(i) for i in operational_list]
        return operational_list

    def encode(self, text):
        text_byte_list = self.byte(text)
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


ver = Vernam()
print('Key:', ver.return_key())
coded = ver.encode('Аве, Цезарь! Спешу должить, что наши войска только что форсировали Рубикон!')
print('Coded view:', coded)
print('Decoded:', ver.decode(coded))
