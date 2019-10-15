from dataclasses import dataclass, field, InitVar
from typing import List, Union

from twyla.chat.templates.base import ChatTemplate

__all__ = ["PostBackButton", "UrlButton", "Buttons", "ButtonTypes"]


@dataclass
class Button:
    title: str


@dataclass
class PostBackButton(Button):
    payload: str
    type: str = field(default="postback", init=False)


@dataclass
class UrlButton(Button):
    url: str
    type: str = field(default="web_url", init=False)


ButtonTypes = Union[PostBackButton, UrlButton]


@dataclass
class ButtonsPayload:
    text: str
    buttons: List[Button] = field(default_factory=list)
    template_type: str = field(default="button", init=False)

    def add(self, *buttons: ButtonTypes) -> None:
        """
        Add a button
        :param buttons:
        """
        assert len(self.buttons) + len(buttons) <= 3, "Maximum 3 buttons supported"
        self.buttons.extend(buttons)


@dataclass
class Buttons(ChatTemplate):
    text: InitVar[str]
    payload: ButtonsPayload = field(default=None, init=False)
    type: str = field(default="template", init=False)
    template_type: str = field(default="fbmessenger.button_sub_template", init=False)

    def __post_init__(self, text):
        self.payload = ButtonsPayload(text=text)

    def add(self, *buttons: ButtonTypes) -> None:
        """
        Add a button
        :param buttons:
        """
        self.payload.add(*buttons)
