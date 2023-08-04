from fastapi import FastAPI
from pydantic import BaseModel

# Entidad users

class User(BaseModel): #al usar el basemodel retorna como un json sin la necesidad de usar un init
    id : int
    name : str
    surname : str
    url : str
    age : int

users = [User(id=1,name='Matias',surname='Lemos',url='http://matias_lemos.com',age=18),
         User(id=2,name='Hector',surname='Herrera',url='http://HHerrera.com',age=20),
         User(id=3,name='Gabriela',surname='Lopez',url='http://Glopez.com',age=21)]

app = FastAPI()

@app.get("/userjson")
async def usersjson():
    return [{'name':'Matias','surname':'Lemos','url':'http://matias_lemos.com','age': 18},
            {'name':'Hector','surname':'Herrera','url':'http://HHerrera.com','age': 20},
            {'name':'Gabriela','surname':'Lopez','url':'http://Glopez.com','age': 21}]

@app.get('/user')
async def userclass():
    return users

#Path
@app.get('/user/{id}')
async def user(id:int):     
    return search_user(id)

#Query
@app.get('/userquery/') #http://127.0.0.1:8000/userquery/?id=3
async def user(id:int): 
    return search_user(id)


#POST

@app.post('/user/')
async def user(user: User):
    if type(search_user(user.id)) == User:
        return {'Error':'este usuario ya existe'}
    else:
        users.append(user)


def search_user(id:int):

    user_id = filter(lambda user: user.id == id, users)

    try:
        return list(user_id)[0]
    except:
        return {'error':'No se ha encontrado el usuario'}
