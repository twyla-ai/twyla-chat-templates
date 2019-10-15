from dataclasses import dataclass, field
from typing import List

from twyla.chat.templates.base import ChatTemplate


@dataclass
class QuickReply:
    title: str
    payload: str
    content_type: str = field(default="text", init=None)


@dataclass
class QuickReplies(ChatTemplate):
    text: str
    quick_replies: List[QuickReply] = field(default_factory=list)
    template_type: str = "fbmessenger.quick_reply"

    def add(self, *quick_replies: QuickReply) -> None:
        """
        Add a quick reply
        :param quick_replies:
        """
        assert len(self.quick_replies) < 10, "Maximum 10 quick replies supported"
        self.quick_replies.extend(quick_replies)
