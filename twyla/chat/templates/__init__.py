from dataclasses import asdict, dataclass


@dataclass
class BaseClass:
    def asdict(self):
        return asdict(self)
