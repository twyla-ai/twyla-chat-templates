from dataclasses import dataclass

from twyla.chat.templates import BaseClass


@dataclass
class TextTemplate(BaseClass):
    payload: str
