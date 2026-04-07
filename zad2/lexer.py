from tokens import KEYWORDS, OPERATORS, SEPARATORS


class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value


class Lexer:
    def __init__(self, text):
        self.text = text

    def tokenize(self):
        tokens = []
        i = 0
        n = len(self.text)
        source = self.text

        while i < n:
            c = source[i]

            # białe znaki (spacje, entery, taby)
            if c.isspace():
                start = i
                while i < n and source[i].isspace():
                    i += 1
                tokens.append(Token("WHITESPACE", source[start:i]))

            # komentarze //
            elif c == '/' and i + 1 < n and source[i + 1] == '/':
                start = i
                while i < n and source[i] != '\n':
                    i += 1
                tokens.append(Token("COMMENT", source[start:i]))

            # string "tekst"
            elif c == '"':
                start = i
                i += 1  # pomija pierwszy cudzysłów
                while i < n and source[i] != '"':
                    i += 1
                if i < n:
                    i += 1  # pomija zamykający cudzysłów
                tokens.append(Token("STRING", source[start:i]))

            # liczby
            elif c.isdigit():
                start = i
                while i < n and (source[i].isdigit() or source[i] == '.'):
                    i += 1
                tokens.append(Token("NUMBER", source[start:i]))

            # identyfikatory i keywords
            elif c.isalpha() or c == '_':
                start = i
                while i < n and (source[i].isalnum() or source[i] == '_'):
                    i += 1
                lexeme = source[start:i]

                if lexeme in KEYWORDS:
                    tokens.append(Token("KEYWORD", lexeme))
                else:
                    tokens.append(Token("IDENTIFIER", lexeme))

            #operatory
            elif c in OPERATORS:
                if i + 1 < n and source[i:i + 2] in {"==", ">=", "<=", "!="}:
                    tokens.append(Token("OPERATOR", source[i:i + 2]))
                    i += 2
                else:
                    tokens.append(Token("OPERATOR", c))
                    i += 1

            elif c in SEPARATORS:
                tokens.append(Token("SEPARATOR", c))
                i += 1
            else:
                tokens.append(Token("UNKNOWN", c))
                i += 1

        return tokens