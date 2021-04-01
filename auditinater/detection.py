"""
Find non-compliant behaviour.

"""


def find_offenders(client, api_url):
    """Recover the list of users who are not using google SSO to login.

    :param api_url: The PaaS API to query for offenders.

    :param api_token: The PaaS API to query for offenders.

    """
    usernames = []

    data = client.get(api_url)
    response = data.json()['resources']
    for user in response:
        if user['origin'] != 'google':
            usernames.append(user)
    usernames.sort()

    return usernames
