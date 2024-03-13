from const import keywords


def check_is_suitable(text: str) -> bool:
    """
    Checks if message must be resent or not.
    :param text:str
    :return: bool
    """

    text_lower = text.lower()
    is_suitable = False

    for keyword in keywords:
        if keyword in text_lower:
            is_suitable = True
            break

    return is_suitable
