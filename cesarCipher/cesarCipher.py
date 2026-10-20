class CesarCipher:
    def __init__(self, word, key):
        self._word = word
        self._key = key

    def Cipher(self):
        self._word = self._word.lower()
        self.result = ""

        for char in self._word:

            if 'a' <= char <= 'z':
                self.result += chr((ord(char) + self._key - 97) % 26 + 97)
            else:
                self.result += char
        print(self.result)


    def run(self):
        self._word = input("Podaj haslo do zaszyfrowania: ")
        self._key = int(input("Podaj klucz szyfrowania (liczbe): "))
        self.Cipher()

if __name__ == "__main__":
    app = CesarCipher("", "")
    app.run()