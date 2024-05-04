PassWord = 'gyenios'
def get_password():
    def authenticate(password):
        if password == PassWord:
            print('--Login successful--')
            return True
        else:
            print('Wrong password')
            return False
        
    login = True
    tries = 3
    while True:
        if tries == 0:
            print('You entered the wrong password too many times')
            break
        else:
            password = input('Enter Admin password: ')
            login = authenticate(password)
            if login == True:
                break
            else:
                tries -= 1
    return login

class Admin:
    def __init__(self):
        pass
        
    def menu(self):
        print('''
                [1] View sales
                [2] View Inventory
                [3] Update inventory
                [4] Exit
            ''')

class Customer:
    def __init__(self):
        pass

    def menu(self):
        print('''
                [1] Search item
                [2] Purchase item
                [3] View Cart
                [4] Go to checkout
                [5] Exit
            ''')
    
def search():
    import csv
    # Define a function to read the CSV file and filter schools
    def filter_products(csv_file, option, Brand=None, Model=None, Unit_price=None):
        items, brands, models, unit_prices = [], [], [], []
        
        with open(csv_file, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if option == 1:
                    if row['Brand'] == Brand:
                        items.append(row['Item'])
                        brands.append(row['Brand'])
                        models.append(row['Model'])
                        unit_prices.append(row['Unit Price(USD)'])
                elif option == 2:
                    if row['Model'] == Model:
                        items.append(row['Item'])
                        brands.append(row['Brand'])
                        models.append(row['Model'])
                        unit_prices.append(row['Unit Price(USD)'])
                elif option == 3:
                    if Unit_price == '1':
                        x, y = 0.00, 99.99
                    elif Unit_price == '2':
                        x, y = 100.00, 299.99
                    elif Unit_price == '3':
                        x, y = 300.00, 499.99
                    elif Unit_price == '4':
                        x, y = 500.00, 799.99
                    elif Unit_price == '5':
                        x, y = 800.00, 2000.00
                    price = float(row['Unit Price(USD)'])
                    if x <= price <= y:
                        items.append(row['Item'])
                        brands.append(row['Brand'])
                        models.append(row['Model'])
                        unit_prices.append(row['Unit Price(USD)'])
                elif option == 4:
                    if row['Brand'] == Brand and row['Model'] == Model:
                        items.append(row['Item'])
                        brands.append(row['Brand'])
                        models.append(row['Model'])
                        unit_prices.append(row['Unit Price(USD)'])

    results = [items, brands, models, unit_prices]
    return results

    choice = '1'
    while choice == '1':
        Results = []
        print('''
        Search by:
        [1] Brand
        [2] Model
        [3] Price range
        [4] All
        ''')
        choice = input()
        if choice == '1':
            brand = input("Brand: ").title()
            Results = filter_products("inventory.csv", int(choice), Brand=brand)
        elif choice == '2':
            model = input("Model: ").title()
            Results = filter_products("inventory.csv", int(choice), Model=model)
        elif choice == '3':
            print('''
                    --PRICE RANGES--
                    [1] 0.00 - 99.99
                    [2] 100.00 - 299.99
                    [3] 300.00 - 499.99
                    [4] 500.00 - 799.99
                    [5] 800.00 - 2000.00
                    ''')
            price = input("Price range: ").title()
            Results = filter_products("inventory.csv", int(choice), Unit_price=price)
        elif choice == '4':
            brand = input("Brand: ").title()
            model = input("Model: ").title()
            Results = filter_products("inventory.csv", int(choice), Brand=brand, model=model)
        print("\n")
        items = Results[0]
        brands = Results[1]
        models = Results[2]
        unit_prices = Results[3]
        print("ITEMS\t\t\t\tBRANDS\t\t\t\tMODELS\t\t\t\tUNIT PRICE")
        for i in range(len(items)):
            print(f"{items[i]:<40} {brands[i]:<40} {models[i]:<40}",unit_prices[i])
        

        
