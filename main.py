import sqlite3
from time import *
x=True
try:
    #Тут подключение к БД
    try:
        conn=sqlite3.connect('BD.db')
        print ('Connection database')
    except Exception as e:
        print ('Error connecting to database')
        print (e)
        x=False
    sleep(1)

    #Тут курсор    
    try:
        cur=conn.cursor()

        print ('Connecting to cursor')
    except Exception as e:
        print('Error connecting to cursor')
        print (e)
        x=False

    sleep(1)

    if x==True:
        print('Database is ready to go')
    else:
        print('Database is not ready to go')

    sleep(1)
    job= True   

    while job==True:
        print('\n Что Вы хотите сделать?')
        print('     1) Добавить заметки')
        print('     2) Показать все заметки')
        print('     3) Редактировать заметки')
        print('     4) Удалить заметку')
        print('     5) Выйти из приложения')

        key=int(input("\n Введите необходимую цифру - "))

        if key==1:
            insert_sql= "INSERT INTO users (name, text) VALUES (?, ?)"
            name_zametok=str(input('\n Введите название заметки - '))
            text_zametok=str(input('\n Введите текст заметки - '))
            cur.execute(insert_sql, (name_zametok, text_zametok))
            conn.commit()
            str(input('Для продолжения введите Enter'))
            continue

        elif key==2:
            cur.execute('SELECT name, text FROM users;')
            rows=cur.fetchall()
            for row in rows:
                name,text= row
                print(name, ' - ', text)
                print('--------')
            str(input('Для продолжения введите Enter'))
            continue

        elif key==3:
            cur.execute('SELECT name, text FROM users;')
            rows=cur.fetchall()
            num=0
            for row in rows:
                num+=1
                name,text= row
                print(num, ') ',name, ' - ', text)
            
            print('Какую заметку Вы хотите редактировать?')
            nums=int(input('Введите необходимую цифру - '))
            if nums <= num:
                query='Update users SET text = ? WHERE id = ?'
                text_zametok_1 = str(input("Введите необходимые изменения - "))
                cur.execute(query, (text_zametok_1, nums))
                print('Вы уверены, что хотите сохранить измененния? Введите Y/N')
                n=str(input())
                if n == 'Yes' or n == 'yes' or n == 'y' or n == 'Y':
                    conn.commit()
                else:
                    print ('Error')
            else:
                print("Такой заметки не существует, попробуйте еще раз")            
            str(input('Для продолжения введите Enter'))
            continue

        elif key==4:
            cur.execute('SELECT name, text FROM users;')
            rows=cur.fetchall()
            num=0
            for row in rows:
                num+=1
                name,text= row
                print(num, ') ',name, ' - ', text)
            
            print('Какую заметку Вы хотите удалить?')
            nums=int(input('Введите необходимую цифру - '))
            if nums <= num:
                cur.execute(f"DELETE FROM users WHERE id={nums};")
                print('Вы уверены, что хотите удалить заметку? Введите Y/N')
                n=str(input())
                if n == 'Yes' or n == 'yes' or n == 'y' or n == 'Y':
                    conn.commit()
            else:
                print("Такой заметки не существует, попробуйте еще раз") 
            str(input('Для продолжения введите Enter'))
            continue
        elif key==5:
            cur.close()
            conn.close()
            break
        else:                
            print('\n Такого действия нет, попробуйте еще раз')
            str(input('Для продолжения введите Enter'))
            continue

except Exception as ex:
    print("Error ")
    print(ex)

