from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey


# Declaração das Classes para o Modelo ORM
Base = declarative_base()


class Client(Base):
    __tablename__ = "client"
    # atributos
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    cpf = Column(String(9))
    address = Column(String(30))

    def __repr__(self):
        return f"Client(id={self.id}, name={self.name}, address={self.address})"


class Account(Base):
    __tablename__ = "account"
    # atributos
    id = Column(Integer, primary_key=True)
    type = Column(String(2))
    agency = Column(Integer)
    number = Column(Integer)
    balance = Column(Float)
    client_id = Column(Integer, ForeignKey("client.id"), nullable=False)

    def __repr__(self):
        return f"Account(id={self.id}, type={self.type}, saldo={self.balance})"


# Realiza a conexão com o banco de dados
engine = create_engine("sqlite://")


# Cria as classes como tabelas no banco de dados
Base.metadata.create_all(engine)


# Faz a persistência das Informações no Banco de Dados SQLite
with Session(engine) as session:
    matheus = Client(name='Joao da Silva',
                     cpf='999.999.999.99',
                     address='Av Mal Tito, 1512'
                     )

    sandy = Client(name='Roque Júnior',
                   cpf='888.888.888.88',
                   address='Rua 14, S/N'
                   )

    patrick = Client(name='Mathew Cruz',
                     cpf='123.456.789.44',
                     address='Av Mogi das Cruzes, 5500'
                     )

    account1 = Account(client_id='1',
                     type='cc',
                     agency=22,
                     number=10231,
                     balance=2132131
                     )
    account2 = Account(client_id='2',
                     type='cp',
                     agency=10,
                     number=13231,
                     balance=32156
                     )
    account3 = Account(client_id='3',
                       type='cc',
                       agency=351,
                       number=98422,
                       balance=4566
                       )

    # Envia as informações para o BD (persitência de dados)
    session.add_all([matheus, sandy, patrick])
    session.add_all([account1, account2, account3])
    session.commit()


# Consulta as Informações Salvas no Banco de Dados SQLite
stmt_clients = select(Client).where(Client.name.in_(['Joao da Silva', 'Mathew Cruz']))
for result in session.scalars(stmt_clients):
    print(result)


stmt_order = select(Client).order_by(Client.name.desc())
for result in session.scalars(stmt_order):
    print(result)


stmt_accounts = select(Account).order_by(Account.type.desc())
for result in session.scalars(stmt_accounts):
    print(result)


stmt_join = select(Client.name, Account.type, Account.balance).join_from(Client, Account)
connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
for result in results:
    print(result)

session.close()