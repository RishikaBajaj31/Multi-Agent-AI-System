import pandas as pd
import matplotlib.pyplot as plt

class DataAgent:
    def __init__(self, file_path):
        # Read CSV or Excel
        if file_path.endswith(".csv"):
            self.df = pd.read_csv(file_path)
        else:
            self.df = pd.read_excel(file_path)

    def handle(self, query: str):
        query = query.lower()

        # Show column names
        if "columns" in query or "headers" in query:
            return list(self.df.columns)

        # Show first 5 rows
        if "head" in query or "first" in query:
            return self.df.head().to_dict(orient="records")

        # Show summary stats for numeric columns
        if "summary" in query or "describe" in query:
            return self.df.describe().to_dict()

        # Plot top 5 numeric columns if "top 5" in query
        if "top 5" in query:
            numeric_cols = self.df.select_dtypes(include="number").columns
            if len(numeric_cols) == 0:
                return "No numeric columns to plot."
            for col in numeric_cols[:5]:
                self.df[col].plot(kind="bar", title=f"Top 5 values of {col}")
                plt.savefig(f"/content/top5_{col}.png")
                plt.clf()
            return "Charts saved for top numeric columns."

        # Default: show first 5 rows
        return self.df.head().to_dict(orient="records")
