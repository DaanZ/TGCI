import os

from core.util import json_read_file, json_write_file, sanitize_filename
from core.vault.data_vault import DataVault


class JSONVault(DataVault):

    def __init__(self, user_id: str, path: str):
        super().__init__(user_id)
        if not os.path.exists(path):
            os.mkdir(path)
        if len(user_id) > 50:
            user_id = user_id[:50]
        self.path = os.path.join(path, sanitize_filename(user_id + ".json"))
        print("JSONVault Access: ", self.path)
        if os.path.exists(self.path):
            self._restore()
        else:
            self.data = {"id": user_id}

    def _restore(self):
        self.data = json_read_file(self.path)

    def _save(self):
        json_write_file(self.path, self.data)

    def set(self, key, object):
        self.data[key] = object
        self._save()

    def get(self, key, default):
        if key in self.data:
            return self.data[key]
        self.data[key] = default
        return default

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            self._save()
