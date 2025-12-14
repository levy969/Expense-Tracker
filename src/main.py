import json
import os

class expense:
    def __init__(self):
        self.names = []
        self.descriptions = []
        self.prices = []

    def Add(self,name,description,prices):
        self.names.append(name)
        self.descriptions.append(description)
        self.prices.append(prices)

    def view(self):
        if not self.names:
            print("no expenses yet.")
            return
        
        print("\nAll expenses:")
        for i, (name, desc ,price) in enumerate(zip(self.names, self.descriptions, self.prices),start = 1):
            print(f"{i}. {name} | {desc} | rs.{price}")
        print()

def load_expenses(x):
    if not os.path.exists('expenses.json'):
        return
    with open('expenses.json', 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print("⚠ JSON file corrupted. Resetting file.")
            data = []
    if data:
        for item in data:
            x.Add(item["name"], item["description"], item["price"])
    return

def main():
    print('hello want to add an expense??')
    x = expense()
    load_expenses(x)
    while True:
        print("\n1. Add expense\n2. view all expense\n3. view total amount\n4. save expenses\n5. exit\n")
        s = input('enter a number : ')
        
        if s == '1':
            temp1 = input('enter name : ').strip()
            temp2 = input('enter description : ').strip()
            while True:
                try :
                    temp3 = int(input("enter price : "))
                    break
                except ValueError:
                    pass
            x.Add(temp1,temp2,temp3)
                    
        elif s == '2':
            x.view()
      
        elif s == '3':
            total = 0
            for i in x.prices:
                total += i
            print(f"total spend : {total}")

        elif s == '4':
            exptemp =[]
            for name, desc, price in zip(x.names, x.descriptions, x.prices):
                exptemp.append({
                    "name": name,
                    "description": desc,
                    "price": price
                })

            with open ('expenses.json','w')as f:
                json.dump(exptemp, f, indent = 4)
            print("expenses saved to expenses.json")
                
        elif s == '5':
            print('exiting...')
            break

        else :
            print('enter no properly')

if __name__ == "__main__":
    main()
 
