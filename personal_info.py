import json
import os

class PersonalInfoManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_info()

    def load_info(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("Error decoding JSON file. Starting with an empty data structure.")
                return {}
        else:
            return {}

    def save_info(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=4)


    def add_info(self,name,age,email,phone,address):
        if name in self.data:
            print("This name allready exists. Usu update to change info.")
            return 
        else:
            self.data[name] = {
                    'age':age,
                    'email':email,
                    'phone':phone,
                    'address':address
                    }
        self.save_info()
        print(f"Information for {name} has been added.")

    def view_info(self, name):
        if name in self.data:
            return self.data[name]
        else:
            print(f"No information found for {name}")
            return None
    def update_info(self, name, age=None, email=None, phone=None, address=None):
        if name in self.data:
            choise_for_update = input(f"please chouse wich info do you want to change for {name}\n1. age:\n2. email:\n3. phone:\n4. address: ")
            if choise_for_update == 'age':
                age = input('age: ')
                self.data[name]['age'] = age
            elif choise_for_update == 'email':
                email = input('email: ')
                self.data[name]['email'] = email
            elif choise_for_update == 'phone':
                phone = input('phone: ')
                self.data[name]['phone'] = phone
            elif choise_for_update == 'address':
                address = input('address: ')
                self.data[name]['address'] = address
            self.save_info()
            print((f"Information for {name} has been updated."))
        else:
            print(f"No information found for {name}. Consider adding it first.")

    def delete_info(self, name):
        if name in self.data:
            del self.data[name]
            self.save_info()
            print((f"Information for {name} has been updated."))
        else:
            print(f"No information found for {name}.")
        

     