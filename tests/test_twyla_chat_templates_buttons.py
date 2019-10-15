import pytest

from twyla.chat.templates.buttons import Buttons, PostBackButton, UrlButton


@pytest.fixture
def button_template():
    template = {
        "payload": {
            "buttons": [
                {
                    "title": "Margherita",
                    "payload": "x_Margherita_oaWVAeasEK_x",
                    "type": "postback",
                },
                {"title": "Hawaii", "url": "https://google.com", "type": "web_url"},
            ],
            "template_type": "button",
            "text": "What is your favourite type of pizza?",
        },
        "template_type": "fbmessenger.button_sub_template",
        "type": "template",
    }
    return template


def test_button_template(button_template):
    buttons = Buttons(text="What is your favourite type of pizza?")
    buttons.add(
        PostBackButton(title="Margherita", payload="x_Margherita_oaWVAeasEK_x"),
        UrlButton(title="Hawaii", url="https://google.com"),
    )
    assert buttons.asdict() == button_template
