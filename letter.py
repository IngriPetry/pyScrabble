from os import isatty
from consts import letterPoints
from board import boardMultiplier, WORD, LETTER, displayCharacter

class Letter:

    def __init__(self, letter, y, x, isNew):
        self.letter = letter
        self.y = y
        self.x = x
        self.isNew = isNew

    def getValue(self):
        value = letterPoints[self.letter]
        if (self.y,self.x) in boardMultiplier:
            place, mult = boardMultiplier[(self.y, self.x)]
            if place == LETTER:
                value = value * mult
        return value

    def __repr__(self):
        return self.letter

    def __eq__(self, otherLetter):

        if not isinstance(otherLetter, Letter):
            return False

        if self.letter != otherLetter.letter or self.x != otherLetter.x or self.y != otherLetter.y:
            return False
        return True

class Word:

    def __init__(self):
        self.letters = []

    def addLetter(self, letter):
        self.letters.append(letter)

    def getWordScore(self):
        value = 0
        for letter in self.letters:
            value += letter.getValue()
        return value

    def __repr__(self):
        palavra = ''
        for letra in self.letters:
            palavra = palavra + letra.letter
        return palavra

    def __eq__(self, otherWord):

        if not isinstance(otherWord, Word):
            return False

        if len(self.letters) != len(otherWord.letters):
            return False
        
        for i in range(len(self.letters)):
            if self.letters[i] != otherWord.letters[i]:
                return False

        return True


