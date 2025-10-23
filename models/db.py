import sqlite3

conexao = sqlite3.connect("db.db")
cursor = conexao.cursor()


def lancar_locacao(Cliente, Equipamento, Local, Referencia, Qtde, Data_inicio, Nota_remessa, Nota_retorno, Status, Obs):
    try:
        query = """
            INSERT INTO locacoes(Cliente, Equipamento, Local, Referencia, Qtde, Data_inicio, Nota_remessa, Nota_retorno, Status, Obs)
            VALUES(?,?,?,?,?,?,?,?,?,?)
        """
        cursor.execute(query, (Cliente, Equipamento, Local, Referencia, Qtde, Data_inicio, Nota_remessa, Nota_retorno, Status, Obs))
        conexao.commit()
    except Exception as error:
        print(error)

def listar_todas_as_locacoes():
    try:
        query = """
            SELECT * FROM locacoes
        """
        cursor.execute(query)
        dados = cursor.fetchall()
        return dados
    except Exception as error:
        print(error)


def atualizar_locacao(Cliente, Equipamento, Local, Referencia, Qtde, Data_inicio, Nota_remessa, Nota_retorno, Status, Obs, id):
    try:
        query = """
            UPDATE locacoes SET Cliente = ?, Equipamento = ?, Local = ?, Referencia = ?, Qtde = ?, Data_inicio = ? , Nota_remessa = ?, Nota_retorno = ?, Status = ?, Obs = ? WHERE id = ?
        """
        cursor.execute(query, (Cliente, Equipamento, Local, Referencia, Qtde, Data_inicio, Nota_remessa, Nota_retorno, Status, Obs, id))
        conexao.commit()
    except Exception as error:
        print(error)