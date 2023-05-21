class Lancamentos:

    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
       
    
    def adicionar_lancamento(self, lancamento):
        with open(self.nome_arquivo, 'a+') as arquivo:
            arquivo.write(str(lancamento) + '\n')

    def salvar_lancamentos(self, lancamentos):
        with open(self.nome_arquivo, 'w') as arquivo:
            for lancamento in lancamentos:
                arquivo.write(str(lancamento) + '\n')
    
    def informar_valor(self, mensagem):
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print('inválido!') 
            return self.informar_valor(mensagem)


    def informar_inteiro(self, mensagem):
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print('inválido!') 
            return self.informar_inteiro(mensagem)
        
    def buscar_lancamento(self, ano, mes):
        with open(self.nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                registro = linha.strip().split(',')
                if int(registro[0]) == ano and int(registro[1]) == mes:
                    return linha
        return None
    
    def alterar_lancamento(self, ano, mes, novo_valor):
        linhas = []
        with open(self.nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for i, linha in enumerate(linhas):
                registro = linha.strip().split(',')
                if int(registro[0]) == ano and int(registro[1]) == mes:
                    linhas[i] = f"{ano},{mes},{novo_valor}\n"
                    break

        with open(self.nome_arquivo, 'w') as arquivo:
            arquivo.writelines(linhas)

    def excluir_lancamento(self, ano, mes):
        linhas = []
        with open(self.nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()

        linha_excluida = None
        for linha in linhas:
            registro = linha.split(',')
            if int(ano) == int(registro[0]) and int(mes) == int(registro[1]):
                linha_excluida = linha
                break

        if linha_excluida:
            linhas.remove(linha_excluida)

        with open(self.nome_arquivo, 'w') as arquivo:
            arquivo.writelines(linhas)  

    def listar_lancamentos(self):
        lancamentos=[]
        with open(self.nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
        for linha in linhas:
            registro = linha.strip().split(',')
            lancamento = {
                'ano': int(registro[0]),
                'mes': int(registro[1]),
                'valor': float(registro[2])
            }
            lancamentos.append(lancamento)

        lancamentos_ordenados = sorted(lancamentos, key=lambda x: (x['ano'], x['mes']))
        for lancamento in lancamentos_ordenados:
            print(f"Ano: {lancamento['ano']}, Mês: {lancamento['mes']}, Valor: {lancamento['valor']}")                    



class Salario(Lancamentos):

    def __init__(self, nome_arquivo):
        super().__init__(nome_arquivo)
        self.ano = None
        self.mes = None
        self.valor = None


    def incluir_salario(self):
        self.ano = self.informar_inteiro('Informe o ano: ')
        self.mes = self.informar_inteiro('Informe o mês: ')
        self.valor = self.informar_valor('Informe o salário: ')
        self.linha = f"{self.ano},{self.mes},{self.valor}"
        

    def salvar_salario(self):
        self.adicionar_lancamento(self.linha)

    def alterar_salario(self):
        self.ano = self.informar_inteiro('Informe o ano: ')
        self.mes = self.informar_inteiro('Informe o mês: ')
        self.novo_valor = self.informar_valor('Informe o novo salário: ')
        self.alterar_lancamento(self.ano, self.mes, self.novo_valor)        

    def excluir_salario(self):
        self.ano = self.informar_inteiro('Informe o ano: ')
        self.mes = self.informar_inteiro('Informe o mês: ')
        self.excluir_lancamento(self.ano, self.mes)

    
class Despesa(Lancamentos):

    def __init__(self, nome_arquivo):
        super().__init__(nome_arquivo)
        self.ano = None
        self.mes = None
        self.valor = None

    def incluir_despesas(self):
        self.ano = self.informar_inteiro('Informe o ano: ')
        self.mes = self.informar_inteiro('Informe o mês: ')
        self.valor = self.informar_valor('Informe a despesa: ')
        self.linha = f"{self.ano},{self.mes},{self.valor}"


    def salvar_despesa(self):
        self.adicionar_lancamento(self.linha)

    def alterar_despesa(self):
        self.ano = self.informar_inteiro('Informe o ano: ')
        self.mes = self.informar_inteiro('Informe o mês: ')
        self.novo_valor = self.informar_valor('Informe a nova despesa: ')
        self.alterar_lancamento(self.ano, self.mes, self.novo_valor)       

    def excluir_despesa(self):
        self.ano = self.informar_inteiro('Informe o ano: ')
        self.mes = self.informar_inteiro('Informe o mês: ')
        self.excluir_lancamento(self.ano, self.mes)


class Resultados(Lancamentos):
    def __init__(self, nome_arquivo):
        super().__init__(nome_arquivo)
        

    def calcular_saldo(self, ano, mes):
        salario = 0
        despesa = 0

        
        with open('salarios.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                registro = linha.strip().split(',')
                if int(registro[0]) == ano and int(registro[1]) == mes:
                    salario += float(registro[2])

        
        with open('despesa.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                registro = linha.strip().split(',')
                if int(registro[0]) == ano and int(registro[1]) == mes:
                    despesa += float(registro[2])
        
        if despesa > salario:
            print('Erro favor rever lancamento')
        else:
            saldo = salario-despesa 
        return saldo   
    

def exibir_menu():
    print("Menu:")
    print("1. Incluir Salário")
    print("2. Incluir Despesas")
    print("3. Alterar Salário")
    print("4. Alterar Despesas")
    print("5. Excluir Salário")
    print("6. Excluir Despesas")
    print("7. Calcular Saldo")
    print("8. Sair")

meu_salario = Salario('salarios.txt')
minha_despesa = Despesa('despesa.txt')
meu_resultado = Resultados('lancamentos.txt')
while True:
    exibir_menu()
    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        meu_salario.incluir_salario()
        meu_salario.salvar_salario()
    elif escolha == "2":
        minha_despesa.incluir_despesas()
        minha_despesa.salvar_despesa()
    elif escolha == "3":
        meu_salario.alterar_salario()
        meu_salario.salvar_lancamentos()
    elif escolha == "4":
        minha_despesa.alterar_despesa()
        minha_despesa.salvar_lancamentos()
    elif escolha == "5":
        meu_salario.excluir_salario()
        meu_salario.salvar_lancamentos()
    elif escolha == "6":
        minha_despesa.excluir_despesa()
        minha_despesa.salvar_lancamentos()
    elif escolha == "7":
        ano = meu_salario.informar_inteiro('Informe o ano: ')
        mes = meu_salario.informar_inteiro('Informe o mês: ')
        saldo = Resultados('lancamentos.txt').calcular_saldo(ano, mes)
        print(f"Saldo: R${saldo}")
    elif escolha == "8":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Digite um número válido do menu.")




