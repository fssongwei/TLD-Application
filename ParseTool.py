

def MORGANSFUNCTION(variablesList, block):
    print(block)


def parse_tool(file):
    block = "1"
    f = open(file)
    for line in f:
        variablesList = []
        if(line[0] == "."):
            fields = line.split(" ")
            block = fields[1]
        else:
            line = line.replace('\n', "")
            line = line.replace("[", "")
            line = line.replace("]", "")
            variables = line.split(",")
            for i in variables:
                variablesList.append(i)
            MORGANSFUNCTION(variablesList, block)
    f.close()



parse_tool("ECFR_1hour_data_dump.txt")


