x=0

class employee:
    
    empid = 0
    empname = ''
    empadress = ''
    empsalary = 0


    def __init__(self):
        global x
        x += 1
        
    def getdata(self):
        return str(self.empid) +";"+ self.empname + ";" + self.empadress + ";" + str(self.empsalary)

    def printdata(self):
        print(self.getdata())
emp1 =employee()
emp2 =employee()
emp3 =employee()
emp4 =employee()
emp5 =employee()

print(x)

