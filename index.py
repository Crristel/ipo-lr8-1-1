import json
def num1(read_file):
    for i in read_file:
        for key, value in i.items():
            if key == 'id':
                print(f"Номер записи: {value}".center(36, "~"))
            elif key == 'name':
                print(f"Название рыбы: {value}")
            elif key == 'latin_name':
                print(f"Латинское название рыбы: {value}")
            elif key == 'is_salt_water_fish':
                if value:
                    value = "да"
                else:
                    value = "нет"
                print(f"Является ли рыба пресноводной: {value}")
            elif key == 'sub_type_count':
                print(f"Количество подвидов рыб: {value}")
        print()  

def num2(read_file):
    user_id=int(input("Введите поле записи,которую необходимо вывести:"))
    find=False
    for i in read_file:
        if i['id'] == user_id:
            for key, value  in i.items(): 
                if key =='id':
                    print(f"Номер записи:{value}".center(36,"~"))
                        
                elif key=='name':
                    print(f"Название рыбы:{value}")
                elif key=='latin_name':
                    print(f"Латинское название рыбы:{value}")
                elif key=='is_salt_water_fish':
                    if value==True:
                        value="да"
                    else:
                        value="нет"
                    print(f"Является ли рыба пресноводной:{value}")
                elif key=='sub_type_count':
                    print(f"Количество подвидов рыб:{value}")
                    print()
                    find=True    
            break
    if not find:
        print()
        print("Запись не найдена!")
        print()
        

def num3(read_file):
    id=0
    for i in read_file:
        if i['id']:
            id+=1
    user_name=input("Введите название рыбы:")
    user_Lname=input("Введите латинское название рыбы:")
    user_is_saltFish=input("Введите является ли рыба пресноводной:")
    if user_is_saltFish.lower() =='да':
        user_is_saltFish=True
    else:
        user_is_saltFish=False
    while True:
        user_sub = input("Введите количество подвидов рыб: ")
        if user_sub.isdigit():  # Проверяем, является ли ввод числом
            user_sub = int(user_sub)
            break  # Выходим из цикла, если ввод корректен
        else:
            print("Это должно быть число!")
     

    new_fish={"id": id+1, "name":user_name, 
               "latin_name": user_Lname,
               "is_salt_water_fish":user_is_saltFish,
               "sub_type_count":user_sub
               }
    read_file.append(new_fish)
    with open("fish.json", 'w', encoding='utf-8') as out_file:
        json.dump(read_file, out_file,ensure_ascii=False,indent=2)
    print("Рыба успешно добавлена!")
                
def num4(read_file):
    user_remove = int(input("Введите номер для удаления: "))
    find=False
    for i in read_file:
        if i['id'] == user_remove:
            read_file.remove(i)
            with open("fish.json", "w",encoding="UTF-8") as new_file:
                json.dump(read_file, new_file, ensure_ascii = False, indent=4)
                find=True
                print("Рыба успешно удалена!")
                break
    if not find:
        print()
        print("Запись не найдена!")
        print()

with open("fish.json", "r", encoding="utf-8") as file:
    read_file = json.load(file)
count=0

while True:
    print("Меню".center(24, "~"))
    print("1) Вывести все записи")
    print("2) Вывести запись по полю")
    print("3) Добавить запись")
    print("4) Удалить запись по полю")
    print("5) Выйти из программы")

    user_number = int(input("Для выбора введите номер пункта: "))
    
    if user_number == 1:
        num1(read_file)
        count+=1
    elif user_number==2:
        num2(read_file)
        count+=1
    elif user_number==3:
        num3(read_file)
        count+=1
    elif user_number==4:
        num4(read_file)
        count+=1
    elif user_number == 5:
        print(f"Количество выполненных операций:{count}")
        break  
    else:
        print("ERROR! please try again!")
