from dataclasses import dataclass, field
from typing import List, Union
from twyla.chat.templates.buttons import Button, PostBackButton, UrlButton


@dataclass
class GenericElementDefaultAction:
    url: str
    messenger_extensions: bool = False
    type: str = "web_url"
    webview_height_ratio: str = "tall"


@dataclass
class GenericElement:
    title: str
    image_url: str
    default_action: GenericElementDefaultAction
    buttons: List[Button] = field(default_factory=list)

    def add(self, *buttons: Union[PostBackButton, UrlButton]) -> None:
        """
        Add a button
        :param buttons:
        """
        assert len(self.buttons) + len(buttons) <= 3, "Maximum 3 buttons supported"
        self.buttons.extend(buttons)


@dataclass
class GenericPayload:
    template_type: str = "generic"
    elements: List[GenericElement] = field(default_factory=list)

    def add(self, *elements: GenericElement) -> None:
        """
        Add a generic template element
        :param elements:
        """
        self.elements.extend(elements)


@dataclass
class GenericTemplate:
    payload: GenericPayload
    template_type: str = "fbmessenger.generic"
    type: str = "template"
