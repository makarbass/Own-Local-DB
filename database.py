from typing import Dict, List


class Database:
    def __init__(self):
        self.data: Dict[str, str] = {}
        self.transactions: List[Dict[str, str]] = []

    def set(self, key: str, value: str) -> None:
        self.data[key] = value

    def get(self, key: str) -> str:
        return self.data.get(key, "NULL")

    def unset(self, key: str) -> None:
        self.data.pop(key, None)

    def count(self, value: str) -> int:
        return list(self.data.values()).count(value)

    def find(self, value: str) -> List[str]:
        return [key for key, val in self.data.items() if val == value]

    def begin(self) -> None:
        self.transactions.append(dict(self.data))

    def rollback(self) -> None:
        if self.transactions:
            self.data = self.transactions.pop()

    def commit(self) -> None:
        if self.transactions:
            self.transactions.clear()