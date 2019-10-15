from dataclasses import dataclass

from twyla.chat.templates.base import ChatTemplate


@dataclass
class TextTemplate(ChatTemplate):
    payload: str
