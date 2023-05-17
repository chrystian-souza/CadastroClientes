from infra.configs.connection import DBConnectionHandler
from infra.entities.cliente import Cliente


class ClienteRepository:

    # Método para
    def select_all(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Cliente).all()
            return data

    def select(self, cpf):
        with DBConnectionHandler() as db:
            data = db.session.query(Cliente).filter(Cliente.cpf == str(cpf)).first()
            return data

    # Método para inserir cliente no banco de dados
    def insert(self, cliente):
        with DBConnectionHandler() as db:
            try:
                db.session.add(cliente)
                db.session.commit()
                return 'ok'
            except Exception as e:
                db.session.rollback()
                return e

    # Mètodo para realizar a remoção de uma nota do banco de dados
    def delete(self):
        with DBConnectionHandler() as db:
            db.session.query(Cliente).filter(Cliente.cpf == id).delete()
            db.session.commit()
            return 'ok'

    # Método para atualizar uma nota

    def update(self, cliente):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Cliente).filter(Cliente.cpf == cliente.cpf).update \
                ({'nome': cliente.nome, 'telefone_fixo': cliente.telefone_fixo, 'telefone_celular': cliente.telefone_celular, 'numero': cliente.numero, 'sexo': cliente.sexo,
                  'cep': cliente.cep, 'logradouro': cliente.logradouro, 'complemento': cliente.complemento, 'bairro': cliente.bairro,
                  'municipio': cliente.municipio,
                  'estado': cliente.estado})
                db.session.commit()
                return 'ok'
            except Exception as e:
                db.session.rollback()
                return e
