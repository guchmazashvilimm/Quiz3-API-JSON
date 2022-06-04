# #1
# import requests
# req = requests.get('http://www.pythonchallenge.com/')
# print(req.status_code)
# print(req.headers)
# print(req.text)
#
# #2
# import json
# url = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita'
# r = requests.get(url)
# print(r.json())
# result = json.dumps(r.json(),indent=4)
# print(result)
# with open('margarita','w')as file:
#     file.write(result)
#
# #3
# res = json.loads(r.text)
# drink = res['drinks'][1]['strDrink']
# print('სასმლის დასახელება:',drink)
# drink_category = res['drinks'][1]['strCategory']
# print('სასმლის კატეგორია:',drink_category)
# list = []
# id = []
# for each in res['drinks']:
#     drink_name  = each['strDrink']
#     drink_id = each['idDrink']
#     list.append(drink_name)
#     id.append(drink_id)
# print('მარგარიტას სასმელების სია:',list)
#
# #4
# import sqlite3
# conn = sqlite3.connect("margarita_db")
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE cocktail
#                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                    drink_name varchar(50),
#                    drink_id FLOAT )''')
#
# cursor.executemany('INSERT INTO cocktail (drink_name,drink_id) VALUES (?,?)', list,id)
# conn.commit()