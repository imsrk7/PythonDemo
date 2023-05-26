import csv

with open('C:\\Users\\Srk\\PycharmProjects\\PythonDemo\\Utilities\\loanapp.csv') as csvFile:
    csvReader = csv.reader(csvFile)
    # print(list(csvReader))
    names = []
    status = []
    for row in csvReader:
        names.append(row[0])
        status.append(row[1])

print(names)
print(status)

i = names.index('Jon')
loanStatus = status[i]
print("Jon Loan Status is " + loanStatus)


with open('C:\\Users\\Srk\\PycharmProjects\\PythonDemo\\Utilities\\loanapp.csv', 'a') as wFile:
    write = csv.writer(wFile)
    write.writerow(["Bob", "Rejected"])