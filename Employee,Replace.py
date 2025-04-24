#serialize and deserialize this data of Employee.
import pickle

class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj
        self.salary = salary

emp = Employee(101, "John Doe", "2023-05-12", 50000)

''' Serialize '''
with open("employee.pkl", "wb") as file:
    pickle.dump(emp, file)

''' Deserialize '''
with open("employee.pkl", "rb") as file:
    loaded_emp = pickle.load(file)
    print(vars(loaded_emp))

#Deleting the word and replacing them with blank space.

with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        words = line.split()
        filtered_words = [word for word in words if word.lower() not in ['a', 'the', 'an']]
        outfile.write(" ".join(filtered_words) + "\n")
