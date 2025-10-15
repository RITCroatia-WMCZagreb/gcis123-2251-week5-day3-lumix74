##Reading advanced CSV (has """ inside) - do not use symple file reader
def names_and_addresses_01(filename:str):
    with open(filename) as csv_file:
        next(csv_file)##skipping first line
        for line in csv_file:
            #print(line)
            fileds = line.split(",")
            print("name:",fileds[0]," address:",fileds[1])

##Advanced CSV reader
import csv
def names_and_addresses_02(filename:str):
    with open(filename) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            print("name:",row[0]," address:",row[1])

def average(filename: str, column):
    with open(filename) as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        #print(headers[0])
        print("name:", headers[column])

def number_of_grades_greater_than_threashold(filename:str,column,threashold):
    with open(filename) as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader) #Last Name,First Name,Lab 1,Lab 2,Lab 3,Lab 4,Lab 5,Lab 6,Lab 7,Lab 8,Exam 1,Exam 2,Proj 1,Proj 2-1,Proj 2-2,Proj 2-3,Proj 2-4,Final Grade
        counter = 0
        for row in csv_reader:
            try:
                number = float(row[column])
                if number>threashold:
                    counter+=1
            except ValueError:
                print("Unable to convert ", row[column], "to number")
        print("name:",headers[column], end = " ")
        print(", number of grades:",counter)


def main():
    #names_and_addresses_01("data/full_grades_010.csv")
    #names_and_addresses_02("data/full_grades_010.csv")
    #average("data/grades_010.csv", 5)
    number_of_grades_greater_than_threashold("data/grades_010.csv", 4, 95)


if __name__ == "__main__":
    main()