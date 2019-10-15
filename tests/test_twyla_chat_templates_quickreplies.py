import pytest

from twyla.chat.templates.quickreplies import QuickReplies, QuickReply


@pytest.fixture
def quick_replies_template():
    template = {
        "text": "Which kind of chocolate do you prefer?",
        "quick_replies": [
            {"title": "Dark", "payload": "dark_chocolate", "content_type": "text"},
            {"title": "Milk", "payload": "milk_chocolate", "content_type": "text"},
        ],
        "template_type": "fbmessenger.quick_reply",
    }
    return template


def test_quick_replies(quick_replies_template):
    quick_replies = QuickReplies(text="Which kind of chocolate do you prefer?")
    quick_replies.add(QuickReply(title="Dark", payload="dark_chocolate"))
    quick_replies.add(QuickReply(title="Milk", payload="milk_chocolate"))
    assert quick_replies.asdict() == quick_replies_template
