import re

import pytest


def email_formatting(email=''):
    if re.search(r"[a-zA-Z0-9]+@[a-zA-Z]+\.(ru|com)", email):
        pass
    else:
        return False


@pytest.mark.parametrize('email_data', ['some-email@mail.net', 'email.email.com',
                                        'numbers_in_domen@123.ru'])
def test_strig_email_negative(email_data):
    assert email_formatting(email=email_data) is False


