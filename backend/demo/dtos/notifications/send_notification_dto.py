from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class SendNotificationDTO:
    title: str
    type: str
    description: str
    url: str
    recipients: List
    username: str
    seen: bool