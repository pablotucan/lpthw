import sys
script, input_encoding, error = sys.argv


languages = open("languages.txt", encoding="utf-8")

def main(languages, input_encoding, errors):
    line = languages.readline()

    if line:
        print_line(line, input_encoding, errors)
        return main(languages, input_encoding, errors)


def print_line(line, input_encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(input_encoding, errors=errors)
    cooked_string = raw_bytes.decode(input_encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
