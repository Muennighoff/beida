import urllib.request
import pandas as pd
import sqlite3

url = "http://quotes.money.163.com/trade/lsjysj_000001.html?year=2020&season=2"

YEARS = [2015, 2016, 2017, 2018, 2019, 2020, 2021]
STOCKS = ["000001", "000002", "000003", "000004", "000005"]
SEASONS = [1, 2, 3, 4]

conn = sqlite3.connect("stocks.db")
c = conn.cursor()

for statement in open("stocks.sql").read().split("\n\n"):
    c.execute(statement)

for stock in STOCKS:
    for y in YEARS:
        for s in SEASONS:
            cur_url = f"http://quotes.money.163.com/trade/lsjysj_{stock}.html?year={y}&season={s}"
            try:
                with urllib.request.urlopen(cur_url) as i:
                    html = i.read()
            except Exception as e:
                print(f"Could not find {cur_url}")
                continue
            
            tables = pd.read_html(html)
            price_table = tables[3]

            if len(price_table) == 0:
                continue

            price_table.columns = [
                "datum",
                "opening",
                "highest",
                "lowest",
                "closing",
                "incr",
                "incrpct",
                "volume",
                "amount",
                "amplitude",
                "changed",
            ]

            price_table["stock"] = stock
            price_table["year"] = y
            price_table["season"] = s

            def get_month(row):
                return int(str(row.datum).split("-")[1])

            price_table["month"] = price_table.apply(lambda x: get_month(x), axis=1)

            price_table.to_sql(name="stocks", con=conn, index=False, if_exists="append")

conn.commit()
conn.close()
