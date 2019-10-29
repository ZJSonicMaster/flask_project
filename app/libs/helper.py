def is_isbn_or_key(word):
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    q_replace = word.replace('-', '')
    if '-' in word and len(q_replace) == 10 and q_replace.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key