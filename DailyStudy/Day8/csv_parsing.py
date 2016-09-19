# _*_ coding:utf-8 _*_
# list - dic
def read_csv(filename,sep):
    with open(filename,"r") as fp:
        data = fp.read()
        rows = data.split("\n")
        columns = rows[0].split(sep)
        
        elements = []

        for row in rows[1:-1]:
            fields = row.split(sep)

            element = {}
            for i in range(len(columns)):
                column = columns[i]
                field = fields[i]
                element[column] = field
                
            elements.append(element)
    return elements 


print(read_csv("student.csv",","))
