from unittest.mock import MagicMock

import pytest

from auditinater import api
from auditinater import detection


@pytest.mark.parametrize(
    ('token', 'expected'),
    [
        ('', ''),
        ('token', 'token'),
        ('token', 'token'),
        ('bearer token', 'token'),
        ('BEARER token', 'token'),
        ('BEARER      token', 'token'),
        ('      BEARER      token', 'token'),
        ('      BEARER      token        ', 'token'),
    ]
)
def test_strip_bearer_from_tokens(log, token, expected):
    """Verify how token with or without bearer is handled.
    """
    assert api.strip_bearer(token) == expected


@pytest.mark.parametrize(
    ('users', 'offenders'),
    [
        (
            [
                dict(origin='uua', username='bob@example.com'),
                dict(origin='google', username='1234567890'),
                dict(origin='google', username='0987654321')
            ],
            [
                dict(origin='uua', username='bob@example.com'),
            ]
        ),
        (
            [
                dict(origin='google', username='1234567890'),
                dict(origin='google', username='0987654321')
            ],
            []
        ),
        (
            [], []
        )
    ],
)
def test_find_offenders(log, users, offenders):
    """Verify the finding or not of API offenders.
    """
    api_url = "https://api.com/v3/users"
    client = MagicMock()
    data = MagicMock()
    data.json.return_value = dict(resources=users)
    client.get.return_value = data

    assert detection.find_offenders(client, api_url) == offenders
