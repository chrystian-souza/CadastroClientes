from infra.configs.connection import DBConnectionHandler
from infra.entities.cliente import Cliente


class ClienteRepository:

    # Método para
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Cliente).all()
            return data

    # Método para inserir nota no banco de dados
    def insert(self, cpf, nome, telefone_fixo, telefone_celular, numero, sexo, cep,
               logradouro, complemento, bairro, municipio, estado):
        with DBConnectionHandler() as db:
            data_inset = Nota(cpf=cpf, nome=nome, telefone_fixo=telefone_fixo, telefone_celular=telefone_celular,
                              numero=numero, sexo=sexo, cep=cep, logradouro=logradouro, complemento=complemento,
                              bairro=bairro, municipio=municipio, estado=estado)
            db.session.add(data_inset)
            db.session.commit()

    # Mètodo para realizar a remoção de uma nota do banco de dados
    def delete(self):
        with DBConnectionHandler() as db:
            db.session.query(Cliente).filter(Cliente.id == id).delete()
            db.session.commit()

    # Método para atualizar uma nota

    def update(self , nome, telefone_fixo, telefone_celular, numero, sexo, cep,
               logradouro, complemento, bairro, municipio, estado):
        with DBConnectionHandler() as db:
            db.session.query(Cliente).filter(Cliente.id == id).update \
                ({'nome': nome, 'telefone_fixo': telefone_fixo, 'telefone_celular': telefone_celular, 'numero': numero, 'sexo': sexo,
                  'cep': cep, 'logradouro': logradouro, 'complemento': complemento, 'bairro': bairro,
                  'municipio': municipio,
                  'estado': estado})
            db.session.commit()
