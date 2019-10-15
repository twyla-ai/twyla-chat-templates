import pytest

from twyla.chat.templates.image import ImageTemplate


@pytest.fixture
def image_template():
    template = {
        "payload": {"is_reusable": True, "url": "https://pictures.com/picture.jpg"},
        "template_type": "fbmessenger.image",
        "type": "image",
    }
    return template


def test_image_template(image_template):
    i = ImageTemplate(url="https://pictures.com/picture.jpg").asdict()
    assert i == image_template
