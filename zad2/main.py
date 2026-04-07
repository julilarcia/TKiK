from lexer import Lexer
from highlighter import highlight, wrap_html


def main():
    with open("input.txt", "r", encoding="utf-8") as f:
        code = f.read()

    lexer = Lexer(code)
    tokens = lexer.tokenize()

    colored = highlight(tokens)
    html = wrap_html(colored)

    with open("output.html", "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    main()