from dataclasses import dataclass, field
from typing import List


@dataclass
class QuickReply:
    title: str
    payload: str
    content_type: str = "text"


@dataclass
class QuickReplies:
    text: str
    quick_replies: List[QuickReply] = field(default_factory=list)
    template_type: str = "fbmessenger.quick_reply"

    def add(self, title: str) -> None:
        """
        Add a quick reply
        :param title: The title to display for the quick reply button
        """
        assert len(self.quick_replies) < 10, "Maximum 10 quick replies supported"
        self.quick_replies.append(QuickReply(title=title))
