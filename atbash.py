class Atbash:
    def __init__(self):
        self.alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        lowercase_code = {x: y for x, y in zip(self.alphabet, self.alphabet[::-1])}
        uppercase_code = {x.upper(): y.upper() for x, y in zip(self.alphabet, self.alphabet[::-1])}
        self._encode = dict(lowercase_code)
        self._encode.update(uppercase_code)

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

cipher = Atbash()
input_string = open('atbash_input.txt', 'r', encoding='utf8').read().lower()
output = open('atbash_output.txt', 'w', encoding='utf8')
output.write(cipher.encode(input_string))
