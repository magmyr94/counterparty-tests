def precedingSibling(value, endElement = '*'):
    """ get preceding-sibling xpath

    :param value: str
    :return: str
    """
    return f'//*[text()[contains(.,\'{value}\')]]/preceding-sibling::{endElement}'


def followingSibling(value, endElement = '*'):
    """ get following-sibling xpath

    :param value: str
    :param endElement: str
    :return: str
    """
    return f'//*[text()[contains(.,\'{value}\')]]/following-sibling::{endElement}'


def contains(value):
    """ get text-contains xpath

    :param value: str
    :return: str
    """
    return f'//*[text()[contains(.,\'{value}\')]]'
