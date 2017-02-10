class Caesar:
    def __init__(self, key):
        self.alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        self._encode = dict()
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            encoded = self.alphabet[(i + key) % len(self.alphabet)]
            self._encode[letter] = encoded
            self._encode[letter.upper()] = encoded.upper()
        self._decode = {}
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            decoded = self.alphabet[(i - key) % len(self.alphabet)]
            self._decode[letter] = decoded
            self._decode[letter.upper()] = decoded.upper()

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, line):
        return ''.join([self._decode.get(char, char) for char in line])

input_text = open('caesar_input.txt', 'r', encoding='utf8').read().lower()
cipher = Caesar(19)
output_text = cipher.decode(input_text)
output = open('caesar_output.txt', 'w', encoding='utf8')
output.write(output_text)
