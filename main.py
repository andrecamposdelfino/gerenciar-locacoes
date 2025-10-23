from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from models.db import lancar_locacao, listar_todas_as_locacoes, atualizar_locacao, listar_todas_as_locacoes_ativas, listar_todas_as_locacoes_finalizadas

def open_formulario_cadastro_de_locacao():
    form_cadastra_locacao.show()

def cadastar_locacao():
    try:
        cliente = form_cadastra_locacao.txtCliente.text()
        equipamento = form_cadastra_locacao.txtEquipamento.text()
        local = form_cadastra_locacao.txtLocal.text()
        referencia = form_cadastra_locacao.txtReferencia.text()
        qtde = form_cadastra_locacao.txtQtde.text()
        data = form_cadastra_locacao.txtData.text()
        nf_rem = form_cadastra_locacao.txtNfRem.text()
        nf_ret = form_cadastra_locacao.txtNfRet.text()
        status = form_cadastra_locacao.txtStatus.currentText()
        obs = form_cadastra_locacao.txtObs.toPlainText()

        if cliente == "" or equipamento == "" or local == "" or referencia == "":
            QMessageBox.warning(None, "Erro campos vazios", "Por favor preecher todos os campos")
            return
        else:
            lancar_locacao(cliente, equipamento, local, referencia, qtde, data, nf_rem, nf_ret, status, obs)
            QMessageBox.information(None, "Sucesso!", "Locação cadastrada com sucesso!")
            listar_locacoes()

    except Exception as error:
        QMessageBox.warning(None, "Erro", "Não foi possivel cadastrar.")

def listar_locacoes():
    dados = listar_todas_as_locacoes()
    form_dash.tabela.setRowCount(len(dados))
    form_dash.tabela.setColumnCount(11)
    for row in range(0, len(dados)):
        for column in range(0, 11):
            form_dash.tabela.setItem(row, column, QtWidgets.QTableWidgetItem(str(dados[row][column])))

    form_dash.tabela.resizeColumnsToContents()
    form_dash.tabela.resizeRowsToContents()
    form_dash.tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    form_dash.tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    form_dash.tabela.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

    form_dash.tabela.cellClicked.connect(carregar_dados_listagem)

def listar_locacoes_ativas():
    dados = listar_todas_as_locacoes_ativas()
    form_dash.tabela.setRowCount(len(dados))
    form_dash.tabela.setColumnCount(11)
    for row in range(0, len(dados)):
        for column in range(0, 11):
            form_dash.tabela.setItem(row, column, QtWidgets.QTableWidgetItem(str(dados[row][column])))

    form_dash.tabela.resizeColumnsToContents()
    form_dash.tabela.resizeRowsToContents()
    form_dash.tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    form_dash.tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    form_dash.tabela.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

    form_dash.tabela.cellClicked.connect(carregar_dados_listagem)

def listar_locacoes_fanalizadas():
    dados = listar_todas_as_locacoes_finalizadas()
    form_dash.tabela.setRowCount(len(dados))
    form_dash.tabela.setColumnCount(11)
    for row in range(0, len(dados)):
        for column in range(0, 11):
            form_dash.tabela.setItem(row, column, QtWidgets.QTableWidgetItem(str(dados[row][column])))

    form_dash.tabela.resizeColumnsToContents()
    form_dash.tabela.resizeRowsToContents()
    form_dash.tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    form_dash.tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    form_dash.tabela.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

    form_dash.tabela.cellClicked.connect(carregar_dados_listagem)

def carregar_dados_listagem():
    form_atualiza_locacao.show()

    row = form_dash.tabela.currentRow()
    if row >= 0:
        id = form_dash.tabela.item(row, 0).text()
        cliente = form_dash.tabela.item(row, 1).text()
        equipamento = form_dash.tabela.item(row, 2).text()
        local = form_dash.tabela.item(row, 3).text()
        referencia = form_dash.tabela.item(row, 4).text()
        qtde = form_dash.tabela.item(row, 5).text()
        data = form_dash.tabela.item(row, 6).text()
        nfe_rem = form_dash.tabela.item(row, 7).text()
        nfe_ret = form_dash.tabela.item(row, 8).text()
        status = form_dash.tabela.item(row, 9).text()
        obs = form_dash.tabela.item(row, 10).text()

        form_atualiza_locacao.txtId.setText(id)
        form_atualiza_locacao.txtCliente.setText(cliente)
        form_atualiza_locacao.txtEquipamento.setText(equipamento)
        form_atualiza_locacao.txtLocal.setText(local)
        form_atualiza_locacao.txtReferencia.setText(referencia)
        form_atualiza_locacao.txtQtde.setText(qtde)
        form_atualiza_locacao.txtData.setText(data)
        form_atualiza_locacao.txtNfRem.setText(nfe_rem)
        form_atualiza_locacao.txtNfRet.setText(nfe_ret)
        form_atualiza_locacao.txtStatus.setText(status)
        form_atualiza_locacao.txtObs.setPlainText(obs)
        # QMessageBox.information(None, "Oi bb lindo", "Deu certo meu amor")

def atualizar_locacoes():
    try:

        id = int(form_atualiza_locacao.txtId.text())
        cliente = form_atualiza_locacao.txtCliente.text()
        equipamento = form_atualiza_locacao.txtEquipamento.text()
        local = form_atualiza_locacao.txtLocal.text()
        referencia = form_atualiza_locacao.txtReferencia.text()
        qtde = form_atualiza_locacao.txtQtde.text()
        data = form_atualiza_locacao.txtData.text()
        nfe_rem = form_atualiza_locacao.txtNfRem.text()
        nfe_ret = form_atualiza_locacao.txtNfRet.text()
        status = form_atualiza_locacao.txtStatus.text()
        obs = form_atualiza_locacao.txtObs.toPlainText()

        if form_atualiza_locacao.txtNfRet.text() != "":
            status_finalizado = "FINALIZADO"
            atualizar_locacao(cliente, equipamento, local, referencia, qtde, data, nfe_rem, nfe_ret, status_finalizado, obs, id)

            # Feedback ao usuário
            QMessageBox.information(None, "Sucesso", "Locação atualizada com sucesso!")
            listar_locacoes()
            form_atualiza_locacao.close()
        else:
            atualizar_locacao(cliente, equipamento, local, referencia, qtde, data, nfe_rem, nfe_ret, status, obs, id)

            # Feedback ao usuário
            QMessageBox.information(None, "Sucesso", "Locação atualizada com sucesso!")
            listar_locacoes()
            form_atualiza_locacao.close()


    except Exception as error:
        QMessageBox.warning(None, "Error", f"Não foi possível atualizar a locação:{error}")


    

app = QtWidgets.QApplication([])

form_dash = uic.loadUi("views/frm_dash.ui")
form_cadastra_locacao = uic.loadUi("views/form_cadastra_locacao.ui")
form_atualiza_locacao = uic.loadUi("views/form_alterar_locacao.ui")
form_dash.btnNovaLocacao.clicked.connect(open_formulario_cadastro_de_locacao)

form_dash.btnTodos.clicked.connect(listar_locacoes)
form_dash.btnAtivos.clicked.connect(listar_locacoes_ativas)
form_dash.btnFinalizados.clicked.connect(listar_locacoes_fanalizadas)

form_cadastra_locacao.btnCadastrar.clicked.connect(cadastar_locacao)
form_atualiza_locacao.btnAlterar.clicked.connect(atualizar_locacoes)
form_dash.show()
listar_locacoes()

app.exec()