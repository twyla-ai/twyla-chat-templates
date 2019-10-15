import pytest
from dataclasses import asdict

from twyla.chat.templates.buttons import PostBackButton, UrlButton
from twyla.chat.templates.carousel import CarouselTemplate
from twyla.chat.templates.generic import GenericElement


@pytest.fixture
def carousel_template():
    template = {
        "template_type": "fbmessenger.generic",
        "type": "template",
        "payload": {
            "template_type": "generic",
            "elements": [
                {
                    "title": "Cheesecake",
                    "image_url": "https://cake.com/image.jpg",
                    "subtitle": "Cake with cheese",
                    "default_action": {
                        "type": "web_url",
                        "url": "https://cake.com",
                        "messenger_extensions": False,
                        "webview_height_ratio": "tall",
                    },
                    "buttons": [
                        {
                            "title": "I want Cheesecake",
                            "payload": "x_I_want_Cheesecake_gkvMPBXXxO_x",
                            "type": "postback",
                        },
                        {
                            "title": "Cheesecake, please",
                            "url": "https://cheesecakeplease.com",
                            "type": "web_url",
                        },
                    ],
                },
                {
                    "title": "Apple Pie",
                    "image_url": "https://applepie.com/image.jpg",
                    "subtitle": "Pie with apples",
                    "default_action": None,
                    "buttons": [
                        {
                            "title": "Give me apple pie",
                            "payload": "x_Give_me_apple_pie__MrgOfGJZ5m_x",
                            "type": "postback",
                        },
                        {
                            "title": "Apple Pie is good",
                            "url": "https://apple-pie.io",
                            "type": "web_url",
                        },
                    ],
                },
                {
                    "title": "Brownie",
                    "image_url": "https://brownie.com/image.jpg",
                    "subtitle": "Chocolate Brownie",
                    "default_action": {
                        "type": "web_url",
                        "url": "https://chocolate.com",
                        "messenger_extensions": False,
                        "webview_height_ratio": "tall",
                    },
                    "buttons": [
                        {
                            "title": "I like Brownies",
                            "payload": "x_I_like_Brownies_x",
                            "type": "postback",
                        },
                        {
                            "title": "Brownies are good",
                            "url": "https://brow-nie.io",
                            "type": "web_url",
                        },
                    ],
                },
            ],
        },
    }
    return template


def test_carousel_template(carousel_template):

    e1 = GenericElement(
        title="Cheesecake",
        subtitle="Cake with cheese",
        image_url="https://cake.com/image.jpg",
        action_url="https://cake.com",
        buttons=[
            PostBackButton(
                title="I want Cheesecake", payload="x_I_want_Cheesecake_gkvMPBXXxO_x"
            ),
            UrlButton(title="Cheesecake, please", url="https://cheesecakeplease.com"),
        ],
    )
    e2 = GenericElement(
        title="Apple Pie",
        subtitle="Pie with apples",
        image_url="https://applepie.com/image.jpg",
        buttons=[
            PostBackButton(
                title="Give me apple pie", payload="x_Give_me_apple_pie__MrgOfGJZ5m_x"
            ),
            UrlButton(title="Apple Pie is good", url="https://apple-pie.io"),
        ],
    )
    e3 = GenericElement(
        title="Brownie",
        subtitle="Chocolate Brownie",
        image_url="https://brownie.com/image.jpg",
        action_url="https://chocolate.com",
        buttons=[
            PostBackButton(title="I like Brownies", payload="x_I_like_Brownies_x"),
            UrlButton(title="Brownies are good", url="https://brow-nie.io"),
        ],
    )
    c = CarouselTemplate(elements=[e1, e2, e3])
    assert c.asdict() == carousel_template
