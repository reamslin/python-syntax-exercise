def print_upper_words(strs, starts_with):
    ''' prints each word on a separate line if it starts with a character in the starts_with set '''
    for s in strs:
        if s.lower()[0] in starts_with:
            print(s.upper())

print_upper_words(["hi", "please", "earl"], {"p", "e"})