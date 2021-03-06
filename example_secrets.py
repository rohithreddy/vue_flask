import uuid


def is_production():
    """ Determines if app is running on the production server via uuid comparison.

    HOW TO USE:
    Open a terminal
    > python
    > import uuid
    > uuid.getnode()
    12345678987654321  <-- Copy whatever is returned and replace 111111111 with this.

    Ensure .gitignore excludes ``secrets.py``.
    Finally, rename this file to ``secrets.py``.

    Compare uuid for the machine against the known uuid(s) of your development machine(s).
    :return: (bool) True if code is running on the production server, and False otherwise.
    """
    developer_machines = [111111111, ]
    return uuid.getnode() not in developer_machines