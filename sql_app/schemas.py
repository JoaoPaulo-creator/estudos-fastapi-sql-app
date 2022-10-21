from pydantic import BaseModel

'''

Esse arquivo vai conter os models utilizando Pydantic, que deve economizar umas linhas de códio

'''


class ItemBase(BaseModel):
    title: str
    descricao: str | None = None  # Parâmetro não obrigatório


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True

