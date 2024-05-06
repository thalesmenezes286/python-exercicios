
#Função verifica se é um ano bissexto retornando True 
def verifica_ano_bissexto(ano):
    """ 
     Verificar se um ano é bissexto usando uma função simples. 
     Um ano bissexto é aquele que é divisível por 4, exceto para os anos que são divisíveis por 100, 
     a menos que sejam divisíveis por 400.
    """

    if(ano % 4 == 00 and ano % 100 != 0) or (ano % 400 == 0):
        return True;
    else:
        return False;

#Loop For percorre os anos de 1900 até 2020 e imprime os anos bissextos
for ano in range(1900, 2031):

    if verifica_ano_bissexto(ano):
        print(f"{ano} é um ano bissexto.")
    