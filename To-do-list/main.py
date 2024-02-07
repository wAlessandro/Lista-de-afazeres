import os
def vazio(arquivo):
    return os.stat(arquivo).st_size == 0

#criar arquivos
with open("listdata.txt",'a') as create:
    create.write('')
with open("save.txt",'a') as create2:
    create2.write('')

#verificar se o save ta vazio
if vazio("save.txt"):
    with open("save.txt", 'w') as none:
        none.write(str(1))
#armazenar o valor do save na variavél e converter para numero
with open("save.txt", 'r') as save:
    count = int(save.readline().strip())

with open('listdata.txt', 'r+') as file:
    lista = file.read()

print('Anotações')
print('--'*40)
print(lista)
print('--'*40)

run = True

while run:
    user = f'{count}: '
    user_input = input(f'{count}: ').strip()
    #sair
    if user_input.lower() == 'exit':
        run = False
        count -= 1
    #deletar lista
    if user_input.lower() == 'del':
        with open('listdata.txt','w') as delete:
            delete.write('')
        count = 0
    user += user_input + '\n'
    count += 1
    if (user_input not in 'exitdel') and (user not in 'exitdel'):
        with open('listdata.txt', 'a') as file:
            file.write(user)
if (user not in 'del'):
    with open('save.txt', 'w') as salvar:
        salvar.write(str(count))

