import pdfplumber
from datetime import datetime
from ingest.models import Invoice, Item

class PDFInvoiceReader:

    def extract_invoice(self, pdf_path: str) -> Invoice:
        with pdfplumber.open(pdf_path) as pdf:
            text = pdf.pages[0].extract_text()

        order_id = self._field(text, "Order ID")
        customer_id = self._field(text, "Customer ID")
        date = datetime.strptime(
            self._field(text, "Order Date"),
            "%Y-%m-%d"
        ).date()

        items = self._items(text)

        return Invoice(
            order_id=order_id,
            date=date,
            customer_id=customer_id,
            items=items
        )

    def _field(self, text, name):
        for line in text.splitlines():
            if line.startswith(name):
                return line.split(":")[1].strip()
        raise ValueError(f"{name} não encontrado")

    def _items(self, text):
        items = []
        start = False

        for line in text.splitlines():
            if line.startswith("Product ID"):
                start = True
                continue

            if start:
                if line.startswith("TotalPrice"):
                    break

                parts = line.split()
                product = " ".join(parts[1:-2])
                quantity = int(parts[-2])
                unit_price = float(parts[-1])

                items.append(
                    Item(
                        product=product,
                        quantity=quantity,
                        unit_price=unit_price
                    )
                )

        if not items:
            raise ValueError("Nenhum item encontrado")

        return items
