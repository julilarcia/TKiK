class TokenType:
    INTEGER = "INTEGER"
    IDENTIFIER = "IDENTIFIER"

    PLUS = "PLUS"
    MINUS = "MINUS"
    MUL = "MUL"
    DIV = "DIV"

    LPAREN = "LPAREN"
    RPAREN = "RPAREN"

    END = "END"
    ERROR = "ERROR"


class Token:

    def __init__(self, type, value, column):
        self.type = type
        self.value = value
        self.column = column

    def __str__(self):
        return f"({self.type}, {self.value})"


class Scanner:

    def __init__(self, text):
        self.source = text
        self.position = 0


    def skip_whitespace(self):
        while self.position < len(self.source) and self.source[self.position].isspace():
            self.position += 1

    def next_token(self):

        self.skip_whitespace()

        if self.position >= len(self.source):
            return Token(TokenType.END, "EOF", self.position)

        start = self.position
        char = self.source[self.position]
        self.position += 1

        if char == '+':
            return Token(TokenType.PLUS, "+", start)

        if char == '-':
            return Token(TokenType.MINUS, "-", start)

        if char == '*':
            return Token(TokenType.MUL, "*", start)

        if char == '/':
            return Token(TokenType.DIV, "/", start)

        if char == '(':
            return Token(TokenType.LPAREN, "(", start)

        if char == ')':
            return Token(TokenType.RPAREN, ")", start)

        if char.isdigit():
            return self.scan_number(start)

        if char.isalpha():
            return self.scan_identifier(start)


        return Token(TokenType.ERROR, char, start)

    def scan_number(self, start):

        number = ""
        while self.position < len(self.source) and self.source[self.position].isdigit():
            number += self.source[self.position]
            self.position += 1

        number = self.source[start:self.position]
        return Token(TokenType.INTEGER, number, start)

    def scan_identifier(self, start):

        while self.position < len(self.source) and self.source[self.position].isalnum():
            self.position += 1

        name = self.source[start:self.position]
        return Token(TokenType.IDENTIFIER, name, start)


    def scan_all(self):

        token = self.next_token()
        while token.type not in (TokenType.END, TokenType.ERROR):
            print(token)
            token = self.next_token()

        print(token)

        if token.type == TokenType.ERROR:
            print(f"Błąd w kolumnie {token.column}")