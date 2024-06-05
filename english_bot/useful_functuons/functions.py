
def replacer_escaped_symbols(sentence: str) -> tuple:
    """the function adds '\' in front of symbols of must_to_be_escaped list if the item of must_be_escaped is
    in the sentence the function gets"""
    must_be_escaped = [".", "!", "(", ")", "-"]
    for symbol in must_be_escaped:
        replace = fr"\{symbol}"
        sentence = sentence.replace(symbol, replace)
    return sentence
