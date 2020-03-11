#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sqlite3


class ConectarDB:
    """Classe."""

    def __init__(self):
        self.con = sqlite3.connect('db.sqlite3')

        self.cur = self.con.cursor()

        # Criando as tabelas.
        self.criar_tabela_cliente()
        self.criar_tabela_nutricionista()

    def criar_tabela_cliente(self):
        """Cria a tabela caso a mesma não exista."""
        try:
            self.cur.execute('''CREATE TABLE IF NOT EXISTS Cliente (
                nome TEXT,
                idade INTEGER,
                sexo TEXT,
                cpf INTEGER,
                endereco TEXT,
                cep INTEGER,
                email TEXT,
                telefone INTEGER,
                carteira_saude INTEGER,
                senha TEXT)''')
        except Exception as e:
            print(f'[x] Falha ao criar tabela [x]: {e}')
        else:
            print('[!] Tabela criada com sucesso [!]\n')

    def criar_tabela_nutricionista(self):
        try:
            self.cur.execute('''CREATE TABLE IF NOT EXISTS Nutricionistas (
                nome TEXT,
                idade INTEGER,
                sexo TEXT,
                cpf INTEGER,
                endereco TEXT,
                cep INTEGER,
                email TEXT,
                telefone INTEGER,
                curso TEXT,
                faculdade TEXT,
                experiencia TEXT,
                crn INTEGER,
                preco_consulta, 
                senha TEXT)''')
        except Exception as e:
            print(f'[x] Falha ao criar tabela [x]: {e}')
        else:
            print('[!] Tabela criada com sucesso [!]\n')


    def inserir_registro_cliente(self, usuario):
        """Adiciona uma nova linha na tabela.
        :param usuario (tuple): Tupla contendo os dados.
        """
        try:
            self.cur.execute(
                '''INSERT INTO Cliente VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', usuario)
        except Exception as e:
            print('\n[x] Falha ao inserir registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            # rollback desfaz(ctrl+z)
            self.con.rollback()
        else:
            # commit registra a operação(ctrl+s)
            self.con.commit()
            print('\n[!] Registro inserido com sucesso [!]\n')

    def inserir_registro_nutricionista(self, nutricionista):
        try:
            self.cur.execute(
                '''INSERT INTO Nutricionistas VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', nutricionista)
        except Exception as e:
            print('\n[x] Falha ao inserir registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            # rollback
            self.con.rollback()
        else:
            # commit
            self.con.commit()
            print('\n[!] Registro inserido com sucesso [!]\n')


    def consultar_registro_pela_id_cliente(self, rowid):
        #Consulta registro pela id do cliente
        return self.cur.execute('''SELECT * FROM Cliente WHERE rowid=?''', (rowid,)).fetchone()
    
    def consultar_registro_pela_id_nutricionista(self, rowid):
        #Consulta registro pela id do nutricionista
        return self.cur.execute('''SELECT * FROM Nutricionistas WHERE rowid=?''', (rowid,)).fetchone()

    def consultar_registros_cliente(self, limit=10):
        """Consulta todos os registros da tabela.
        limit: Parâmetro que limita a quantidade de registros
        """
        return self.cur.execute('''SELECT * FROM Cliente LIMIT ?''', (limit,)).fetchall()

    def consultar_registros_nutricionista(self, limit=10):
        """Consulta todos os registros ,da tabela.
        limit: Parâmetro que limita a quantidade de registros
        """
        return self.cur.execute('''SELECT * FROM Nutricionistas LIMIT ?''', (limit,)).fetchall()

    def alterar_registro_cliente(self, rowid, nome, sexo, idade, endereco, cep, email, telefone, carteira_saude, senha):
        #Alterar uma linha da tabela com base na id.
        try:
            self.cur.execute(
                '''UPDATE Cliente SET nome=?, sexo=?, idade=?, endereco=?, cep=?, email=?, telefone=?, carteira_saude=?, senha=? WHERE rowid=?''', (nome, sexo, idade, endereco, cep, email, telefone, carteira_saude, senha, rowid))
        except Exception as e:
            print('\n[x] Falha na alteração do registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            self.con.rollback()
        else:
            self.con.commit()
            print('\n[!] Registro alterado com sucesso [!]\n')

    def alterar_registro_nutricionista(self, rowid, nome, sexo, idade, endereco, cep, email, telefone, curso, faculdade, experiencia, crn, preco_consulta, senha):
        #Alterar uma linha da tabela com base na id.
        try:
            self.cur.execute(
                '''UPDATE Nutricionistas SET nome=?, sexo=?, idade=?, endereco=?, cep=?, email=?, telefone=?, curso=?, faculdade=?, experiencia=?, crn=?, preco_consulta=?, senha=?  WHERE rowid=?''', (nome, sexo, idade, endereco, cep, email, telefone, curso, faculdade, experiencia, crn, preco_consulta, senha, rowid))
        except Exception as e:
            print('\n[x] Falha na alteração do registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            self.con.rollback()
        else:
            self.con.commit()
            print('\n[!] Registro alterado com sucesso [!]\n')

    def remover_registro_cliente(self, rowid):
        """Remove uma linha da tabela com base na id da linha.
        :param rowid (id): id da linha que se deseja remover.
        """
        try:
            self.cur.execute(
                f'''DELETE FROM Cliente WHERE rowid=?''', (rowid,))
        except Exception as e:
            print('\n[x] Falha ao remover registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            self.con.rollback()
        else:
            self.con.commit()
            print('\n[!] Registro removido com sucesso [!]\n')

    def remover_registro_nutricionista(self, rowid):
        #Remove uma linha da tabela com base na id da linha.

        try:
            self.cur.execute(
                f'''DELETE FROM Nutricionistas WHERE rowid=?''', (rowid,))
        except Exception as e:
            print('\n[x] Falha ao remover registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            self.con.rollback()
        else:
            self.con.commit()
            print('\n[!] Registro removido com sucesso [!]\n')


if __name__ == '__main__':
    # Dados

    usuario = ('Maria', 40, 'Masculino', '04442220069', 'rua Loira bonita',
    '03020580', 'maria.teste@gmail.com', '11111-1111', '111222333333444', 'professorlindo123')

    nutricionista=('Lucas lindo', 50, 'Masculino', '04442220069', 'rua lindo programador',
    '06065260', 'lucas.teste@gmail.com', '11111-1111', 'Nutricao', 'Mackenzie', 
    'trabalhei em duas clinicas', '12345', '100', 'professornota10')

    
                

    # Criando a conexão com o banco
    banco = ConectarDB()

    # Inserindo nas tabelas
    banco.inserir_registro_cliente(usuario=usuario)
    banco.inserir_registro_nutricionista(nutricionista=nutricionista)

    # Consultando com filtro.
    # print(banco.consultar_registro_pela_id_cliente(rowid=1))
    # print(banco.consultar_registro_pela_id_nutricionista(rowid=1))

    # Consultando tudo
    # print(banco.consultar_registros_cliente())
    # print(banco.consultar_registros_nutricionista())

    # Alterações

    # #Clientes
    # # Verificando o antes
    # print(banco.consultar_registro_pela_id_cliente(rowid=1))
    # # Alterando
    # banco.alterar_registro_cliente(rowid=1, nome='Cristina', sexo='Feminino', idade='20', cep='11111222', email='cristina@lindona.com.br', endereco='rua dos abacaxis', telefone='11111-3333', carteira_saude='123456789124587', senha='professorlindao')
    # # pós mudança
    # print(banco.consultar_registro_pela_id_cliente(rowid=1))

    # #Nutricionista
    # # Verificando o antes
    # print(banco.consultar_registro_pela_id_nutricionista(rowid=1))
    # # Alterando
    # banco.alterar_registro_nutricionista(rowid=1, nome='Bruno', sexo='Masculino', idade='40', cep='11111555', email='bruno@lindao.com.br', endereco='um lugar longe', telefone='11111-5555', curso='Nutricao', faculdade='USP', experiencia='trabalhei em 5 clinicas', crn='54321', preco_consulta='150', senha='ricardao')
    # # pós mudança
    # print(banco.consultar_registro_pela_id_nutricionista(rowid=1))

    # # Removendo registro da tabela.
    # # Antes da remoção.
    # print(banco.consultar_registros_cliente())
    # #Realizando a remoção.
    # banco.remover_registro_cliente(rowid=2)
    # #Depois da remoção.
    # print(banco.consultar_registros_cliente())

    # # Antes da remoção.
    # print(banco.consultar_registros_nutricionista())
    # #Realizando a remoção.
    # banco.remover_registro_nutricionista(rowid=2)
    # #Depois da remoção.
    # print(banco.consultar_registros_nutricionista())
