import json
from pathlib import Path
from ingest.models import Invoice

class InvoiceRepository:

    def __init__(self, db_path="database.json"):
        self.db_path = Path(db_path)
        self.data = self._load()

    def _load(self):
        if self.db_path.exists():
            return json.loads(self.db_path.read_text())
        return []

    def save(self, invoice: Invoice):
        if any(i["order_id"] == invoice.order_id for i in self.data):
            return

        self.data.append(invoice.model_dump())
        self.db_path.write_text(
            json.dumps(self.data, indent=4, default=str)
        )
