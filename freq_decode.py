class Monoalphabet:
    def __init__(self, key_table):
        self.alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        self._encode = {x: y for x, y in zip(self.alphabet, key_table)}
        self._decode = {self._encode[item]: item for item in self._encode}

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, text):
        return ''.join([self._decode.get(char, char) for char in text])

cipher = Monoalphabet('эьормщднйгычясюцажшбтпвёлеъузхкфи')
input_text = open('freq_input.txt', 'r', encoding='utf8').read().lower()
output = open('freq_decode_output.txt', 'w', encoding='utf8')
output.write(cipher.decode(input_text))
