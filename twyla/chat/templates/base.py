from dataclasses import dataclass, asdict


@dataclass
class ChatTemplate:
    def asdict(self):
        return asdict(self)
