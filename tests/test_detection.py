from unittest.mock import MagicMock


def test_post_message(log):
    """Verify the URL generated to point at (UI not API) ticket in zendesk.
    """
    mock_web_client = MagicMock()
