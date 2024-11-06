import json
import os

class PersonalInfoManager():
    def __init__(self, file_path):
        self.file_path = file_path

    def load_info(self):
        if not os.path.exists(self.file_path):
            return {}
        with open(self.file_path, 'r') as file:
            try:
                return json.load(file) or {}  # Dosya boşsa boş bir sözlük döner
            except json.JSONDecodeError:
                return {}  # JSON hatasında da boş bir sözlük döner


    def save_info(self, info):
        with open(self.file_path, 'w') as file:
            json.dump(info, file, indent=4)


    def add_info(self,name,age,email,address):
        info = self.load_info()
        info[name] = {
            'age':age,
            'email':email,
            'address':address
        }
        with open(self.file_path, 'w') as file:
            json.dump(info, file, indent=4)
        

    def update_info(self):
        pass

    def remove_info(self):
        pass

     