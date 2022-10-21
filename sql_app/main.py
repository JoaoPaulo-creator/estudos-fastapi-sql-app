from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


'''
SQLAlchemy não tem compatibilidade com await, sendo assim as funcões não possuem a declaração async na frente
como se é utilizado em rotas padrões do FastAPI
'''


@app.post('/users/', response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail='Email já existe')
    return crud.create_user(db=db, user=user)


@app.get('/users/', response_model=list[schemas.User])
def consultar_lista_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    user = crud.get_users(db, skip=skip, limit=limit)
    return user


@app.get('/users/{user_id}', response_model=schemas.User)
def ler_usuario_por_id(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail='Usuário não encontrado')
    return db_user


@app.post('/users/{user_id}/items/', response_model=schemas.Item)
def criar_item_para_usuario(user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get('/items/', response_model=list[schemas.Item])
def ler_itens(skip: int = 0, limit: int = 100, db: SessionLocal = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
