from lexer import Lexer
def main():

    text = '123 ; 11  ; "udjsd" //kom '
    lexer = Lexer(text)
    tokens = lexer.tokenize()
    for token in tokens:
        print(f"Typ: {token.type:<12} Wartość: '{token.value}'")

if __name__ == "__main__":
    main()