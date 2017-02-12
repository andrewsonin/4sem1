class Vernam:
    alphabet = list(enumerate(map(str, open('vernam_alphabet.txt', 'r', encoding='utf8').read()), 10))
    alphabet_dict = {index: ch for ch, index in alphabet}
    alphabet_dict.update({ch: index for ch, index in alphabet})

    def __init__(self, text):
        from random import choice
        self.text = text
        self.keyword_len = len(self.text)
        self.keyword = ''.join([choice(self.alphabet)[1] for i in range(self.keyword_len)])
        self.keyword_byte_list = self.byte(self.keyword)

    def return_key(self):
        return self.keyword

    def byte(self, text):
        return [self.alphabet_dict.get(i) for i in list(map(str, text))]

    def encode(self):
        text_byte_list = self.byte(self.text)
        for i in range(len(text_byte_list)):
            non_zero_coded_letter = str(text_byte_list[i] ^ self.keyword_byte_list[i % self.keyword_len])
            text_byte_list[i] = '0'*(3 - len(non_zero_coded_letter)) + non_zero_coded_letter
        return ''.join(text_byte_list)

    def decode(self, text):
        text_list = []
        for i in range(0, len(text), 3):
            byte = int(text[i:i+3]) ^ self.keyword_byte_list[i//3 % self.keyword_len]
            text_list.append(self.alphabet_dict.get(byte))
        return ''.join(text_list)

coder = Vernam(open('vernam_input.txt', 'r', encoding='utf8').read())
coded = coder.encode()
decoded = coder.decode(coded)
output = open('vernam_output.txt', 'w', encoding='utf8')
output.write('Key:\n' + coder.return_key() + '\n\nCoded view:\n' + coded + '\n\nDecoded view:\n' + decoded)
print('Key:', coder.return_key(), '\nCoded view:', coded, '\nDecoded:', decoded, sep='\n')
