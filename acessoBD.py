from unicodedata import name
import sqlalchemy

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('sqlite:///buteco.DB',echo=False)
Base = declarative_base
SessaoBD = sessionmaker(bind=engine)


class Produto(Base):
    __tablename__ ='tb_produtos'
    idProd = Column(Integer, primary_key = True)
    descProd = Column(String(30))
    vaUnitProd = Column(Float(6.2))

class Conta(Base):
    __tablename__ ='tb_contas'
    idConta = Column(Integer, primary_key = True)
    mesaConta = Column(Integer)
    statusConta = Column(String(10))

class Pedidos(Base):
    __tablename__ ='tb_pedidos'
    idPed = Column(Integer, primary_key = True)
    idContaPed= Column(Integer)
    idProdutoPed = Column(Float(6.2))
    qtdPed = Column(Integer)


Base.metadata.create_all(engine)

def app():

    if __name__ =='__main__':
        app()
    else:
        print("Não é o moduo prinipal")
        exit()




