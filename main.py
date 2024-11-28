#загружаем в переменную read_file данные из fish.json
import json 
with open("fish.json","r", encoding="utf-8") as file:
    read_file = json.load(file)
count=0
id=0

while(True): #цикл для повторения меню и других операций 
    print("Меню".center(24,"~"))
    print("1) Вывести все записи","2) Вывести запись по полю", "3) Добавить запись", "4) Удалить запись по полю","5) Выйти из программы",sep = "\n")
 
    user_number=int(input("Для выбора введите номер пункта:"))
#если введённое с клавиатуры число равно 1, то выполняем первый пункт 
    if user_number==1:
        count+=1
        for i in read_file:
            for key, value in i.items():
                if key =='id':
                    print(f"Номер записи:{value}".center(36,"~"))
                elif key=='name':
                    print(f"Название рыбы:{value}")
               
                elif key=='latin_name':
                    print(f"Латинское название рыбы:{value}")
                elif key=='is_salt_water_fish':
                    # если value равно true, то присваиваем ему значение "да"
                    if value==True: 
                        value="да"
                    else:
                        value="нет"
                    print(f"Является ли рыба пресноводной:{value}")
                elif key=='sub_type_count':
                    print(f"Количество подвидов рыб:{value}")
                    print()

    
    #если введённое с клавиатуры число равно 2, то выполняем второй пункт       
    elif user_number==2:
        user_id=int(input("Введите поле записи,которую необходимо вывести:"))
        find=False #переменная для того ,чтобы узнать нашлась ли запись 
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
                        count+=1
                break
                            
                        
        if not find: #если запись не нашлась 
            print()
            print("Запись не найдена!")
            print()
 #если введённое с клавиатуры число равно 3, то выполняем третий пункт       
    elif user_number==3:
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
            while True: #цикл для проверки введено ли число в пременную user_sub
                user_sub = int(input("Введите количество подвидов рыб: "))
                if user_sub.isdigit():
                    user_sub = int(user_sub)
                    break
                else:
                    print("Это должно быть число!")


#создаём из полученных данных множество 
            new_fish={"id": id+1, "name":user_name, 
               "latin_name": user_Lname,
               "is_salt_water_fish":user_is_saltFish,
               "sub_type_count":user_sub
               }
         #добавляем к наши загруженным данным множество new_fish
            read_file.append(new_fish)
            with open("fish.json", 'w', encoding='utf-8') as out_file:
                json.dump(read_file, out_file,ensure_ascii=False,indent=2)
                print("Рыба успешно добавлена!")
                count+=1
     #если введённое с клавиатуры число равно 4, то выполняем четвёртый пункт       
    elif user_number == 4:
        user_remove = int(input("Введите номер для удаления: "))
        find=False #переменная для того ,чтобы узнать нашлась ли запись 
        for i in read_file:
            if i['id'] == user_remove:
                read_file.remove(i)
                with open("fish.json", "w",encoding="UTF-8") as new_file:
                    json.dump(read_file, new_file, ensure_ascii = False, indent=4)
                find=True
                print("Рыба успешно удалена!")
                count+=1
                break
        if not find: #если запись не нашлась
            print()
            print("Запись не найдена!")
            print()
         #если введённое с клавиатуры число равно 5, то выполняем пятый пункт           
    elif user_number==5:
        print(f"Количество выполненных операций:{count}")
        break
    else: # если пользователь вводит не 1-5, а что-то другое 
        print()
        print("ERROR! Please try again!")
        print()