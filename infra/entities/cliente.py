from infra.configs.base import Base
from sqlalchemy import Column, String, Integer

class Cliente(Base):
    #Nome da tabela criada
    __tablename__ = 'cliente'
    #Colunas da tabela que serão criadas na tabela
    cpf = Column(Integer, autoincrement=True, primary_key=True)
    nome = Column(String(length=100), nullable=False)
    telefone_fixo = Column(String(length=100), nullable=False)
    telefone_celular = Column(String(length=100), nullable=False)
    numero = Column(String(length=100), nullable=False)
    sexo = Column(String(length=100), nullable=False)
    cep = Column(String(length=100), nullable=False)
    logradouro = Column(String(length=100), nullable=False)
    complemento = Column(String(length=100), nullable=False)
    bairro = Column(String(length=100), nullable=False)
    municipio = Column(String(length=100), nullable=False)
    estado = Column(String(length=100), nullable=False)

#Função que sobrescreve a maneira de 'printar' o objeto
def __repr__(self):
    return f'Nome do cliente = {self.nome}, id = {self.cpf}'