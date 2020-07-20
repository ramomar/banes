import os
import pytest


@pytest.fixture
def load_email():
    def _load_email(email_path):
        data_dir = os.path.join(os.path.dirname(__file__), 'emails')
        filepath = os.path.join(data_dir, email_path)

        with open(filepath) as email_file:
            html = email_file.read()

        return html

    return _load_email
