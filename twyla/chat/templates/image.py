from dataclasses import dataclass, field, InitVar

from twyla.chat.templates.base import ChatTemplate


@dataclass
class ImagePayload:
    url: str
    is_reusable: bool = True


@dataclass
class ImageTemplate(ChatTemplate):
    payload: ImagePayload = field(default=None, init=False)
    url: InitVar[str] = field(default=None)
    is_reusable: InitVar[bool] = field(default=True)
    template_type: str = field(default="fbmessenger.image", init=False)
    type: str = field(default="image", init=False)

    def __post_init__(self, url, is_reusable):
        self.payload = ImagePayload(url=url, is_reusable=is_reusable)
