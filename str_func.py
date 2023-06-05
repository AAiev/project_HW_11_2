def transform_in_upper(word):
    """
    Меняет буквы входящего слова на заглавные
    :param word: str
    :return: word.upper
    """
    word_str = str(word)
    if word_str.isalpha():
        return word_str.upper()


def transform_in_title(word):
    """
    Меняет первую букву входящего слова на заглавную
    :param word: str
    :return: word.title
    """
    word_str = str(word)
    if word_str.isalpha():
        return word.title()
