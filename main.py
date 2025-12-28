import os
from ingest.pdf_reader import PDFInvoiceReader
from ingest.repository import InvoiceRepository
from analytics.analytics import InvoiceAnalytics

PASTASPDF = "invoices"

reader = PDFInvoiceReader()
repo = InvoiceRepository()

for file in os.listdir(PASTASPDF):
    if file.endswith(".pdf"):
        invoice = reader.extract_invoice(
            os.path.join(PASTASPDF, file)
        )
        repo.save(invoice)

analytics = InvoiceAnalytics()

print("Média das faturas:", analytics.average_invoice_value())
print("Produto mais vendido:", analytics.most_frequent_product())
print("Total por produto:")
print(analytics.total_spent_per_product())
print("Produtos:")
print(analytics.list_products())
