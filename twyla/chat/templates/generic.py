from dataclasses import dataclass, field, InitVar
from typing import List, Optional

from twyla.chat.templates.base import ChatTemplate
from twyla.chat.templates.buttons import ButtonTypes

__all__ = ["GenericElement", "GenericTemplate"]


@dataclass
class GenericElementDefaultAction(ChatTemplate):
    pass


@dataclass
class GenericWebUrlAction(GenericElementDefaultAction):
    url: str
    messenger_extensions: bool = field(default=False, init=False)
    type: str = field(default="web_url", init=False)
    webview_height_ratio: str = field(default="tall", init=False)


@dataclass
class GenericElement(ChatTemplate):
    title: str
    subtitle: Optional[str] = field(default=None)
    image_url: Optional[str] = field(default=None)
    action_url: InitVar[str] = field(default=None)
    default_action: GenericElementDefaultAction = field(default=None, init=False)
    buttons: List[ButtonTypes] = field(default_factory=list)

    def __post_init__(self, action_url: str):
        if action_url:
            self.default_action = GenericWebUrlAction(url=action_url)

    def add(self, *buttons: ButtonTypes):
        """
        Add a button
        :param buttons: List of url or postback type buttons
        """
        assert len(self.buttons) + len(buttons) <= 3, "Maximum 3 buttons supported"
        self.buttons.extend(buttons)


@dataclass
class GenericPayload(ChatTemplate):
    template_type: str = "generic"
    elements: List[GenericElement] = field(default_factory=list)

    def add(self, *elements: GenericElement) -> None:
        """
        Add a generic template element
        :param elements: List of generic template elements to be added
        """
        assert len(self.elements) + len(elements) <= 10, "Maximum 10 elements supported"
        self.elements.extend(elements)


@dataclass
class GenericTemplate(ChatTemplate):
    payload: GenericPayload = field(default_factory=GenericPayload, init=False)
    template_type: str = field(default="fbmessenger.generic", init=False)
    type: str = field(default="template", init=False)
    elements: InitVar[List[GenericElement]] = field(default=None)

    def __post_init__(self, elements: List[GenericElement]):
        if elements:
            self.add(*elements)

    def add(self, *elements: GenericElement) -> None:
        """
        Add a generic template element
        :param elements: List of generic template elements to be added
        """
        self.payload.add(*elements)
