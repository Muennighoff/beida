FILE_NAME = "1800092850_cnAirport.txt"

airport_list = []
with open(FILE_NAME, "r", encoding="utf8") as f_in:
    for i, line in enumerate(f_in):
        if i == 0:
            continue
        num, name, pass_2018, growth  = line.split(",")
        pass_2018, growth = float(pass_2018), float(growth)
        # (pass_2018-pass_2017) / pass_2017 = growth
        # -> pass_2017 = pass_2018 / (growth+1)
        pass_2017 = round(pass_2018 / ((growth/100)+1), 1)
        airport_list.append((name, pass_2018, pass_2017, growth))

print("2017 年吞吐量")
for i, item in enumerate(sorted(airport_list, key=lambda x: x[2], reverse=True), start=1):
    print(f"{i},{','.join(str(x) for x in item[:-1])}")
print("-" * 50)
print("2018 年增量")
for i, item in enumerate(sorted(airport_list, key=lambda x: x[1] - x[2], reverse=True), start=1):
    print(f"{i},{','.join(str(x) for x in item[:-1])}")
print("-" * 50)
print("2018 年增长率")
for i, item in enumerate(sorted(airport_list, key=lambda x: x[3], reverse=True), start=1):
    print(f"{i},{','.join(str(x) for x in item[:-1])}")