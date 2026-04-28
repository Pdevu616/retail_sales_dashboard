import pandas as pd

class KPIAnalyzer:
    def __init__(self, df):
        self.df = df.copy()
        self.kpis = {}



    def total_sales(self):
        self.kpis["Total Sales"] = self.df["Sales"].sum()
        return self

    def total_profit(self):
        self.kpis["Total Profit"] = self.df["Profit"].sum()
        return self

    def total_orders(self):
        self.kpis["Total Orders"] = self.df["Order ID"].nunique()
        return self

    def average_order_value(self):
        if "Total Sales" not in self.kpis:
            self.total_sales()
        if "Total Orders" not in self.kpis:
            self.total_orders()

        self.kpis["Average Order Value"] = (
            self.kpis["Total Sales"] / self.kpis["Total Orders"]
        )
        return self

    def profit_margin(self):
        if "Total Sales" not in self.kpis:
            self.total_sales()
        if "Total Profit" not in self.kpis:
            self.total_profit()

        self.kpis["Profit Margin"] = (
            self.kpis["Total Profit"] / self.kpis["Total Sales"]
        )
        return self


    def sales_growth(self, time_col="Year"):
        yearly_sales = self.df.groupby(time_col)["Sales"].sum()
        self.kpis["Sales Growth"] = yearly_sales.pct_change().to_dict()
        return self

    def category_sales(self):
        self.kpis["Sales by Category"] = (
            self.df.groupby("Category")["Sales"].sum().to_dict()
        )
        return self

    def category_profit(self):
        self.kpis["Profit by Category"] = (
            self.df.groupby("Category")["Profit"].sum().to_dict()
        )
        return self


    def run_all(self):
        return (
            self.total_sales()
                .total_profit()
                .total_orders()
                .average_order_value()
                .profit_margin()
                .sales_growth()
                .category_sales()
                .category_profit()
        )

    def get_kpis(self):
        return self.kpis

    def to_dataframe(self):
        return pd.DataFrame(list(self.kpis.items()), columns=["Metric", "Value"])