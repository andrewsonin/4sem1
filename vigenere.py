class Vigenere:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def __init__(self, keyword):
        self.alphaindex = {ch: index for index, ch in enumerate(self.alphabet)}
        self.key = [self.alphaindex[letter] for letter in keyword.lower()]

    def caesar(self, letter, shift):
        if letter in self.alphaindex:  # шбжцлюэи ьтчоэ
            index = (self.alphaindex[letter] + shift)%len(self.alphabet)
            cipherletter = self.alphabet[index]
        elif letter.lower() in self.alphaindex:  # йэряэоюэи ьтчоэ
            cipherletter = self.caesar(letter.lower(), shift).upper()
        else:
            cipherletter = letter
        return cipherletter

    def encode(self, line):
        ciphertext = []
        for i, letter in enumerate(line):
            shift = self.key[i % len(self.key)]
            cipherletter = self.caesar(letter, shift)
            ciphertext.append(cipherletter)

        return ''.join(ciphertext)

    def decode(self, line):
        ciphertext = []
        for i, letter in enumerate(line):
            shift = -self.key[i % len(self.key)]
            cipherletter = self.caesar(letter, shift)
            ciphertext.append(cipherletter)

        return ''.join(ciphertext)

alphabet_string = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet_set = set(map(str, alphabet_string))

input_text = open('vigenere_input.txt', 'r', encoding='utf8').read().lower()
input_text_list = input_text.split()
eight_list, k = [], 0
for i in range(len(input_text_list)):
    for j in input_text_list[i]:
        if j in alphabet_set:
            k += 1
        else:
            input_text_list[i] = input_text_list[i][:-1]
    if k == 8:
        eight_list.append(input_text_list[i])
    k = 0

output = open('vigenere_output.txt', 'w', encoding='utf8')
for keyword in ['столлман']:
    cipher = Vigenere(keyword)
    output.write(cipher.decode(input_text))
