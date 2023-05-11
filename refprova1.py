class Lancamentos:

    def __init__(self):
        pass
        


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
        

    def salvar_valor_arquivo(self, linha):
         with open('salario.txt', 'a+') as arquivo:
                               
            arquivo.write(linha)
            arquivo.write('\n')

   
    
    def incluir_salario(self):
                       
            ano = self.informar_inteiro('Informe o ano: ')
            mes =  self.informar_inteiro('Informe o mês: ')
            salario = self.informar_valor('Informe o salário: ')
            
            linha = str(ano) + ',' + str(mes) + ',' + str(salario)
            self.salvar_valor_arquivo(linha)
           
    def alterar_salario(self):
        ano = self.informar_inteiro('Informe o ano: ')
        mes =  self.informar_inteiro('Informe o mês: ')
        salario = self.informar_valor('Informe o novo salário: ')
        linha_alterada = 0
        linhas = []
        with open('salario.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                registro = linha.split(',')
                if (ano == int(registro[0]) and mes == int(registro[1])):
                    linha_alterada = linhas.index(linha)          

            linhas[linha_alterada] = str(ano) + ',' + str(mes) + ',' + str(salario) + '\n'

        with open('salario.txt', 'w') as arquivo:
            arquivo.writelines(linhas)


    def retornar_saldo(self, ano, mes):
        with open('salario.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                registro = linha.split(',')
                if (ano == int(registro[0]) and mes == int(registro[1])):
                    return registro[2]
                

    def incluir_despesa (self):
        ano = self.informar_inteiro('Informe o ano: ')
        mes =  self.informar_inteiro('Informe o mês: ')
        despesa = self.informar_valor('Informe a despesa: ')
        
        saldo_mes = float(self.retornar_saldo(ano, mes))
        
        if despesa > saldo_mes:
            print('Saldo insuficiente!')
        else:   
            with open('despesa.txt', 'a+') as arquivo:
                linha = str(ano) + ',' + str(mes) + ',' + str(despesa) + ';'
                arquivo.write(linha)
                arquivo.write('\n')        

class Menu (Lancamentos):

    def __init__(self):
        pass


pedro = Lancamentos()
#pedro.incluir_salario()
#pedro.alterar_salario()
pedro.incluir_despesa()




#    def incluir_despesas():

#    ano = informar_inteiro('Informe o ano: ')
#    mes =  informar_inteiro('Informe o mês: ')
#    salario = informar_float('Informe o novo salário: ')
##    linha_alterada = 0
##    linhas = []
##    with open('salario.txt', 'r') as arquivo:
 #       linhas = arquivo.readlines();
 #       for linha in linhas:
 #           registro = linha.split(',')
 #           if (ano == int(registro[0]) and mes == int(registro[1])):
 #               linha_alterada = linhas.index(linha)          
 #       
 #       linhas[linha_alterada] = str(ano) + ',' + str(mes) + ',' + str(salario) + '\n'
 #       
 #   with open('salario.txt', 'w') as arquivo:
 #       arquivo.writelines(linhas)
#
#lass Menu:


