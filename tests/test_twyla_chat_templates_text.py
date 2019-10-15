import pytest

from twyla.chat.templates.text import TextTemplate


@pytest.fixture
def text_template():
    template = {"payload": "This is just a string"}
    return template


def test_text_template(text_template):
    i = TextTemplate("This is just a string")
    assert i.asdict() == text_template
