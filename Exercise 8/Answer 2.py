import json
# ============================================================================================
class Food_Menu:
    def __init__(self, food_Code, food_Name, food_Price):
      self.food_Code = food_Code
      self.food_Name = food_Name
      self.food_Price = food_Price
      self.ingredient_list = []
      
    def add_to_ingredient_list(self,ingredient):
        self.ingredient_list.append(ingredient)
        return self.ingredient_list

    def __str__(self):
        return f"Code:{self.food_Code}\tName:{self.food_Name}\tPrice:{self.food_Price}\tIngredients:{self.ingredient_List}"
# ==========================================================================================
class File:
    def __init__(self, file_path, file_mode):
      self.file_path = file_path
      self.file_mode = file_mode
      self.file_object = None
      
    def __enter__(self):
        self.file_object = open(self.file_path,self.file_mode)
        return self.file_object
    
    def __exit__(self,*exc):
        if self.file_object:
            self.file_object.close()     
# ============================================= main program ===========================================
## یک فایل جیسونی ایجاد می کنیم
### داده ها را از این فایل می خوانیم
def read_from_json_file():
    try:
      with File("foodMenu.json","r") as file1:
          menu = json.load(file1)
    except:
        menu = []
    return menu 
# --------------------------------------------------------------------------------------
### داده ها را در این فایل می نویسیم
def write_to_json_file(menu):
    with File("foodMenu.json","w") as file1:
        json.dump(menu,file1,indent=4)
# --------------------------------------------------------------------------------------
### تعریف نمونه از کلاس منوی غذا، اضافه کردن آن به داده هایی که از فایل جیسون خواندیم و نوشتن داده های نهایی در فایل جیسون
def create_food_menu():
   while True:
        code = input("Enter Food Code: ")
        if code != "0":
            name = input("Enter Food Name: ")
            price = input("Enter Food Price: ")
            ingredients = input("Enter ingredients (For Example:meat,tomato,mushroom): ")
            fm = Food_Menu(code,name,price)
            for ingredient in ingredients.split(","):
                fm.add_to_ingredient_list(ingredient)
            menu = read_from_json_file()
            menu.append(fm.__dict__)
            write_to_json_file(menu)
        else:
            break
    
create_food_menu()   
        




