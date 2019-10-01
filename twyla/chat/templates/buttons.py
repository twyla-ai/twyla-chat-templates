from dataclasses import dataclass, field, InitVar
from typing import List, Union

__all__ = ["PostBackButton", "UrlButton", "Buttons", "ButtonTypes"]


@dataclass
class Button:
    title: str


@dataclass
class PostBackButton(Button):
    payload: str
    type: str = "postback"


@dataclass
class UrlButton(Button):
    url: str
    type: str = "web_url"


ButtonTypes = Union[PostBackButton, UrlButton]


@dataclass
class ButtonsPayload:
    text: str
    buttons: List[Button] = field(default_factory=list)
    template_type: str = "button"

    def add(self, *buttons: ButtonTypes) -> None:
        """
        Add a button
        :param buttons:
        """
        assert len(self.buttons) + len(buttons) <= 3, "Maximum 3 buttons suppoerted"
        self.buttons.extend(buttons)


@dataclass
class Buttons:
    text: InitVar[str]
    payload: ButtonsPayload = field(default=None, init=False)
    type: str = "template"
    template_type: str = "fbmessenger.button_sub_template"

    def __post_init__(self, text):
        self.payload = ButtonsPayload(text=text)

    def add(self, *buttons: ButtonTypes) -> None:
        """
        Add a button
        :param buttons:
        """
        self.payload.add(*buttons)
