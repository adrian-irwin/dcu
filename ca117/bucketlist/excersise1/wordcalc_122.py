#!/usr/bin/env python3

import sys

lines = [line.strip() for line in sys.stdin]

definitions = {}

for line in lines:
    tokens = line.split()
    command = tokens[0]

    if command == "def":
        word, integer = tokens[1], int(tokens[2])
        if integer >= -1000 and integer <= 1000:
            if len(word) <= 30 and len(word) >= 1 and word == word.lower() and word != "unknown":
                definitions[word] = integer

    elif command == "calc":
        calculations = tokens[1:]
        result = definitions[calculations[0]]
        try:
            i = 0
            while i < len(calculations):
                if calculations[i] == "+":
                    result = result + definitions[calculations[i + 1]]
                elif calculations[i] == "-":
                    result = result - definitions[calculations[i + 1]]
                i += 1
        except KeyError:
            result = "unknown"

        try:
            print(f"{' '.join(calculations)} {list(definitions.keys())[list(definitions.values()).index(result)]}")
        except ValueError:
            print(f"{' '.join(calculations)} unknown")

    elif command == "clear":
        definitions = {}
