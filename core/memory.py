from core.history import History
from core.vault.json_vault import JSONVault


class Memory(History):

    def __init__(self, id: str, path):
        super().__init__()
        self.vault = JSONVault(id, path)
        self.logs = self.vault.get("logs", [])

    def add(self, role, message):
        self.logs.append({"role": role, "message": message})
        self.vault.set("logs", self.logs)
