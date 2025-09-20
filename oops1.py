class employee:
    def __init__(self):
        print("started excuting attributes")
        self.id = 123
        self.designation = "sde"
        self.salary = 50000
        print("attributes excuted successfully")
    
    def travel(self,destination):
        print("this travel mtd was called manually")
        print(f"employee is travelling to {destination}")

#creating the instance/object
sam = employee()
#accesssing the attributes
#print(sam.id)
#accessing the methods
#sam.travel("bangalore")
print(type(sam))