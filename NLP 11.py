def parse(grammar, sentence):
    def top_down_parse(input, symbols):
        if not input and not symbols:
            return True
        if input and not symbols:
            return False
        if not input and symbols:
            return False

        symbol = symbols[0]
        if symbol in grammar:
            for production in grammar[symbol]:
                if top_down_parse(input, production + symbols[1:]):
                    return True
        elif input[0] == symbol:
            return top_down_parse(input[1:], symbols[1:])
        return False

    return top_down_parse(sentence.split(), ['S'])

# Example usage
grammar = {
    'S': [['NP', 'VP']],
    'NP': [['Det', 'N'], ['N']],
    'VP': [['V', 'NP']],
    'Det': ['the', 'a'],
    'N': ['cat', 'dog'],
    'V': ['chased', 'ran']
}
sentence = "the cat chased the dog"
print(parse(grammar, sentence))
