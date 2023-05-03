from infra.configs.base import Base
from sqlalchemy import Column, String, Integer

class Cliente(Base):
    #Nome da tabela criada
    __tablename__ = 'cliente'
    #Colunas da tabela que serão criadas na tabela
    cpf = Column(String(100), primary_key=True)
    nome = Column(String(100), nullable=False)
    telefone_fixo = Column(String(100), nullable=False)
    telefone_celular = Column(String(100), nullable=False)
    numero = Column(Integer, nullable=False)
    sexo = Column(String(100), nullable=False)
    cep = Column(String(100), nullable=False)
    logradouro = Column(String(100), nullable=False)
    complemento = Column(String(100), nullable=False)
    bairro = Column(String(100), nullable=False)
    municipio = Column(String(100), nullable=False)
    estado = Column(String(100), nullable=False)

#Função que sobrescreve a maneira de 'printar' o objeto
def __repr__(self):
    return f'Nome do cliente = {self.nome}, id = {self.cpf}'