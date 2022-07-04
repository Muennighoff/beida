import random
import string
import sqlite3

from flask import Flask, render_template, request

TABLE_HEAD = """
<thead>
    <tr>
            <th>日期</th>
            <th>开盘价</th>
            <th>最高价</th>
            <th>最低价</th>
            <th>收盘价</th>
            <th>涨跌额</th>
            <th>涨跌幅(%)</th>
            <th>成交量(手)</th>
            <th>成交金额(万元)</th>
            <th>振幅(%)</th>
            <th>换手率(%)</th>
    </tr>
</thead>
"""

COLUMNS = ["stock", "year", "month", "season", "datum", "opening", "highest", "lowest", 
"closing", "incr", "incrpct", "volume", "amount", "amplitude", "changed"]

GET_STOCK_QUERY = """
SELECT *
FROM "stocks"
WHERE stock = '%s' AND year = '%s' AND month = '%s'
"""

conn = sqlite3.connect("stocks.db", check_same_thread=False)
c = conn.cursor()

webapp = Flask(__name__)

# Necessaary for use of flask.session
webapp.secret_key = ''.join(random.choice(string.printable) for _ in range(20))

webapp.config.update(
    TESTING=True,
    TEMPLATES_AUTO_RELOAD=True
)

def get_colored_row(is_red):
    if is_red:
        return '<td style="color:red">'
    else:
        return '<td style="color:green">'

def get_first_prev_close_val(stock, year, month):

    # Adjust
    if month > 1:
        month -= 1
    elif year > 2015:
        year -= 1
        month = 12
    else:
        return 0

    c.execute(GET_STOCK_QUERY % (stock, year, month))

    records = c.fetchall()

    if records:
        return records[0][8]
    else:
        return 0


def create_table(records):
    table = '<table>' + TABLE_HEAD
    table += '<tbody>'
    rows = []
    if records:
        prev_close_val = get_first_prev_close_val(*records[0][:3])
    # Reverse to be able to infer colors
    for line in reversed(records):
        row = '<tr>'
        open_val = line[5]
        for i, col in enumerate(COLUMNS):
            # Skip what's known
            if i < 4:
                continue
            if col in ["opening"]:
                row += get_colored_row(open_val > prev_close_val)
            elif col in ["highest", "lowest", "closing"]:
                row += get_colored_row(line[i] > open_val)
            elif col in ["incr", "incrpct"]:
                row += get_colored_row(line[i] > 0)
            else:
                row += '<td>'
            row += str(line[i])
            row += '</td>'
        prev_close_val = line[8]
        row += '</tr>'
        rows.append(row)
    # Reverse again to have most recent at the top
    table += "".join(reversed(rows))
    table += '</tbody></table>'
    return table

@webapp.route("/")
def root():
	return render_template("stocks.html", placeContent="")

@webapp.route("/getData", methods=['POST'])
def getData():
    stock = request.form["stock"]
    year = request.form["year"]
    month = request.form["month"]
    c.execute(GET_STOCK_QUERY % (stock, year, month))
    records = c.fetchall()
    data = create_table(records)
    return render_template("stocks.html", placeContent=data)


if __name__=="__main__":
	webapp.run(host="0.0.0.0", port=80, debug=True)
