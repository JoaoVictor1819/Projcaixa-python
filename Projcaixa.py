# fazendo um caixa 
import json
import os
import getpass

# Dados globais
funcionarios = {} # Armazenar CPF, nome e senha dos funcionarios

TOTAL_VENDAS_DIA = 0 # Soma todas as vendas do dia
QUANTIDADE_VENDAS = 0 # Conta quantas vendas por dia
TOTAL_IMPOSTO = 0  # Total de imposto a pagar no dia
TAXA_IMPOSTO = 0.10 # 10% imposto 
ARQUIVO_FUNCIONARIO = "Funcionario.json"

# Cadastro de funcionario
def cadastro_funcionario():
    print("\n== cadastro do Funcionario ==")
    cpf = input("Digite o CPF do funcionário(a) (Apenas numero): ")

    if cpf in funcionarios:
       print("Este CPF já está cadastrado.")
       return
    
    nome = input("Digite o nome do funcionario(a): ")
    senha = getpass.getpass("Digite a senha: ")

    funcionarios[cpf] = {
       "nome": nome,
       "senha": senha
    }

    print("Fincionario(a) cadastrado com sucesso!")


def login():
    print("\n=== Login do funcionario(a) ===")
    cpf = input("Digite o cpf (so numero): ")

    if cpf not in funcionarios:
       print("CPF não Cadastrado.")
       return None
    
    senha = getpass.getpass("Digite a senha: ")

    if senha == funcionarios[cpf]["senha"]:
         print(f"Login realizado com sucesso. bem vindo  {funcionarios[cpf]['nome']}")
         return cpf
    else:
       print("Senha incorreta.")
       return None

def caixa(cpf_logado):
    global TOTAL_VENDAS_DIA, QUANTIDADE_VENDAS, TOTAL_IMPOSTO

    while True:
     
     valor = 1
     contador = 1
     total = 0.0

     while valor != 0:
      try:
        valor = float(input(f"produto {contador}: R$"))
        if valor < 0:
           print("O valor não pode ser negativo")
           continue
        total += valor
        contador += 1
      except ValueError:
       print("Digite um valor valido")

    # Calculo do imposto
      imposto = total * TAXA_IMPOSTO
      total_com_imposto = total + imposto

     print(f"Total: {total:.2f}R$")
     dinheiro = float(input("Dinheiro Recebido: R$"))
     troco = dinheiro - total

     print(f"O troco sera de: {troco:.2f}R$")

     # Aqui onde sera atualizado as vendas
     TOTAL_VENDAS_DIA += total_com_imposto
     TOTAL_IMPOSTO += imposto
     QUANTIDADE_VENDAS += 1

     nova = input("Deseja iniciar uma nova venda: (s/n)").strip().lower()
     if nova != 's':
       print("Caixa encerrado")
       break

def mostrar_relatorio():
   print("-" * 30)
   print("Relatorio do dia")
   print(f"Total de vendas realizadas: {QUANTIDADE_VENDAS}")   
   print(f"Total arrecadado (com imposto): R${TOTAL_VENDAS_DIA:.2F}") 
   print(f"Total de impostos pago: R$ {TOTAL_IMPOSTO:.2f}")
   print("-" * 30)

def menu():
 while True:
    print("\n=== Loja Tabajara ===")
    print("1- Cadastrar Funcionario(a)")
    print("2- Login para vendas")
    print("3- Ver ralatorio do Dia")
    print("4- Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
       cadastro_funcionario()
    elif opcao == '2':
       cpf_logado = login()
       if cpf_logado:
          caixa(cpf_logado)
    elif opcao == '3':
       mostrar_relatorio()
    elif opcao == '4':
       print("Fim da operação. Ate a proxima.")
       break
    else:
       print("Opção invalida. tente novamente")
    
# inicio do sistema
menu()