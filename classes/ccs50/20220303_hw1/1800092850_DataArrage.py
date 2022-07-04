import os

FILE_NAME = "ChinaAirportData.txt"
FILE_NAME_OUT_TMP = "tmp.txt"
FILE_NAME_OUT = "1800092850_cnAirport.txt"


### A) Delete 千分位 (10,000 -> 10000) ####

num_lines = 0
with open(FILE_NAME, "r", encoding="utf8") as f_in, open(FILE_NAME_OUT_TMP, "w", encoding="utf8") as f_out:
    for i, line in enumerate(f_in):
        items = line.split(",")
        assert len(items) in (4,5)
        # Remove rows w/o data
        if (not items[2]) or (items[-1].startswith("-100")):
            print("Removing: ",  items)
            continue

        # Remove ten thousand comma
        if len(items) == 5:
            items = items[:2] + ["".join(items[2:4])] + items[4:5]
        f_out.write(",".join(items))
        num_lines += 1

# Delete last empty line
with open(FILE_NAME_OUT_TMP, "r", encoding="utf8") as f_in, open(FILE_NAME_OUT, "w", encoding="utf8") as f_out:
    for i, line in enumerate(f_in):
        if i == (num_lines - 1):
            line = line.strip("\n")
        f_out.write(line)

os.remove(FILE_NAME_OUT_TMP)
