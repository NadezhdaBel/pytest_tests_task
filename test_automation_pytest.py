import re

import pytest


def email_formatting(email=''):
    if re.search(r"[a-zA-Z0-9]+@[a-zA-Z]+\.(ru|com)", email):
        return True
    else:
        return False


@pytest.mark.parametrize('email_data', ['some-email@mail.net', 'email.email.com',
                                        'numbers_in_domen@123.ru'])
def test_strig_email_negative(email_data):
    assert email_formatting(email=email_data) is False


def test_strig_email_positive():
    assert email_formatting(email='some-email@mail.ru') is True


def test_list_even():
    list = [2, 6, 8, 246]
    for x in list:
        try:
            assert x % 2 == 0
        except:
            raise ValueError


def test_list_names():
    list = ['Иван', 'Дмитрий', 'Василий']
    assert 'Дмитрий' in list
