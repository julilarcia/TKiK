from scanner import Scanner

def main():

    expression = input("Podaj wyrażenie: ")

    scanner = Scanner(expression)

    scanner.scan_all()


if __name__ == "__main__":
    main()