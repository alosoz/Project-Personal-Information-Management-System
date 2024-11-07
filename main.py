from personal_info import PersonalInfoManager
import os
import json

class Main():
    def main():
        manager = PersonalInfoManager('data/personal_info.json')

        while True:
            print(" \n1. Add Info:\n2. View Info:\n3. Update Info:\n4. Delete Info:\n5. Exit")
            choice = input("Choose an option")

            if choice == '1':
                name = input("Enter name: ")
                age = input("Enter age: ")
                email = input("Enter email: ")
                phone = input("Enter phone: ")
                address = input("Enter address: ")

                manager.add_info(name,age,email,phone,address)
                
            elif choice == '2':
                name = input('Enter name to view: ')
                info = manager.view_info(name)

                if info:
                    print(f'Name: {name}')
                    for name, details in info.items():
                        print(f'{name.capitalize()}: {details}')
                else:
                   print("No information found.") 
            elif choice == '3':
                #choise_for_update = input(f"please chouse wich info do you want to change for {name}\n
                #                          1. age:\n2. email:\n3. phone:\n4. address: ")
                name = input("Enter name to update")
                manager.update_info(name)
            elif choice == '4':
                name = input("Enter name to delete")
                manager.delete_info(name)
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    if __name__ == '__main__':
        main()