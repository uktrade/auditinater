import requests


def strip_bearer(token):
    """Strip the bearer text from the token if present

    :returns: The token string without the bearer keyword.

    E.g.::

        'bearer 1234' -> '1234'
        '1234' -> '1234'

    """
    # remove trailing spaces
    _token = token.strip()

    # split on gap between bearer and token (if any)
    parts = token.split(' ')

    # if the gap has more than on space strip all spaces
    parts = [part for part in parts if part]

    # return everything at the end of the list and make it into a string.
    _token = "".join(parts[-1:])

    return _token


def client(api_token):
    """Return a request session read for action.

    :param api_token: The token string.

    This is set as the AUTHORIZATION header. The api_token can contain or not
    the bearer identifier at the begining. This won't cause problems.

    :returns: A requests.session instance.

    """
    token = strip_bearer(api_token)

    request = requests.session()
    request.headers.update({
        'AUTHORIZATION': f'bearer {token}',
        'ACCEPT': 'application/json'
    })

    return request
