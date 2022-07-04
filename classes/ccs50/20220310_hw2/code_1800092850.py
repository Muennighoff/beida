# Requirements:
# pip install pandas 
# pip install openpyxl 
import pandas as pd

STD_NUMBER = "1800092850"


data = pd.read_csv('asmData.txt', sep="\t", header=None, names=["a", "b", "c", "cmdname"] + [f"param{x}" for x in range(15)], on_bad_lines="warn")

# Drop columns without cmdname
data = data[data['cmdname'].notna()]

### PART 1 ###
cmd_counts = data['cmdname'].value_counts().reset_index()
cmd_counts.columns = ["Instruction", "Count"]
cmd_counts.to_excel(f'Instruction_{STD_NUMBER}.xlsx', sheet_name='instructionCount', index=False)


### PART 2 ###

null_counts = data[["param1", "param2", "param3"]].isnull().sum(axis=1)

null_counts = null_counts.value_counts()

assert sum(null_counts) == len(data), f"Got {sum(null_counts)}, {len(data)}"

# If 3x null -> no_param_cmd; If 2x null -> single_param_cmd ...
map_dict = {3: 'no_param_cmd', 2: 'single_param_cmd', 1: 'double_param_cmd', 0: 'multi_param_cmd'}

null_counts.index = null_counts.index.map(map_dict)
null_counts = null_counts.reset_index()

with pd.ExcelWriter(f'Instruction_{STD_NUMBER}.xlsx', if_sheet_exists="overlay", mode="a") as writer:  
    null_counts.to_excel(writer, sheet_name='instructionType', index=False, header=False)


### PART 3 ###

null_counts = data[["param1", "param2", "param3"]].isnull().sum(axis=1)
map_dict = {3: 'no_param_cmd', 2: 'single_param_cmd', 1: 'double_param_cmd', 0: 'multi_param_cmd'}
null_counts = null_counts.map(map_dict)

data["type"] = null_counts

data = data.merge(cmd_counts, left_on="cmdname", right_on='Instruction', how='left')

data = data.drop('cmdname', 1)
data = data.sort_values(by=['Count'], ascending=False)
with pd.ExcelWriter(f'Instruction_{STD_NUMBER}_.xlsx', if_sheet_exists="overlay", mode="a") as writer:  
    data[["Instruction", "Count", "type"]].drop_duplicates().to_excel(writer, sheet_name='Summary', index=False, header=True)


### PART 4 ###

# > Directly in Excel File




