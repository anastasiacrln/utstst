import json
from fastapi import FastAPI,HTTPException
with open("menu.json", "r") as read_file: 
    data = json.load(read_file)
app = FastAPI() 
@app.get('/menu/{item_id}') 
async def read_menu(item_id: int): 
    for menu_item in data['menu']:
        if menu_item['id'] == item_id:
            return menu_item
    raise HTTPException(
        status_code=404, detail=f'Item not found'
)

from fastapi import FastAPI
from pydantic import BaseModel
class Item(BaseModel): # the data model
    id: int
    name: str 
@app.post('/menu') 
async def add_menu(menu_item: Item): 
    data['menu'].append({
        "id" : menu_item.id ,
        "name" : menu_item.name
    })
    
    with open("menu.json", "w") as w:
        json.dump(data , w)
    return menu_item

@app.get('/')
async def read_root():
    return {"Hello" : "World"}
@app.get('/menu/{item_id}')
async def read_menu(item_id : int):
    for menu_item in data['menu']:
        if menu_item['id']==item_id:
            
            return menu_item
    raise HTTPException(
        status_code = 404, detail = f'Item not found'
    )
@app.get('/menus')
async def show_menu():
    return data['menu']
@app.put ("/menu/")
async def update_item(item : Item):
    chosen_id = -1
    i = 0
    null = -1
    while (chosen_id == -1 and i < len(data['menu'])):
        if data['menu'][i]["id"] == item.id:
            chosen_id = i
        i-=-1
    if chosen_id != null :
        data['menu'][chosen_id]['name'] = item.name
        with open ("menu.json", "w") as w :
            json.dump(data, w)
            return item
    raise HTTPException(
        status_code = 404, detail=f'Item not found'
    )
@app.delete('/menu/{item_id}')
async def delete_menu(item_id : int):
    itemisreal = False
    null = None
    ii = null
    for i in range (len(data['menu'])):
        if data['menu'][i]['id'] == item_id:
            itemisreal = True
            ii = i 
    if (itemisreal):
        del(data['menu'][ii])
        with open ("menu.json", "w") as w :
            json.dump(data, w) 
        return (None)
    raise HTTPException(
        status_code = 404, detail = f'Item not found'
    )