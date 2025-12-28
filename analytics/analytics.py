import pandas as pd


class InvoiceAnalytics:

    def __init__(self, db_path="database.json"):
        self.df = pd.read_json(db_path)

        if "items" not in self.df.columns:
            raise ValueError(
                "JSON inválido: coluna 'items' não encontrada. "
                "Execute a ingestão novamente."
            )

        self.items_df = self.df.explode("items")

        self.items_df = pd.concat(
            [
                self.items_df.drop(columns=["items"]),
                self.items_df["items"].apply(pd.Series)
            ],
            axis=1
        )

        self.items_df["total"] = (
            self.items_df["quantity"] * self.items_df["unit_price"]
        )

    def average_invoice_value(self):
        totals = self.items_df.groupby("order_id")["total"].sum()
        return totals.mean()

    def most_frequent_product(self):
        return self.items_df["product"].value_counts().idxmax()

    def total_spent_per_product(self):
        return self.items_df.groupby("product")["total"].sum()

    def list_products(self):
        return self.items_df[["product", "unit_price"]].drop_duplicates()
