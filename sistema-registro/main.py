import pandas as pd
import os

while True:
    print('Escolha uma opção', end='\n')
    print('1. Cadastro', end='\n')
    print('2. Listagem', end='\n')
    print('3. Editar cadastro', end='\n')
    print('4. Remover cadastro', end='\n')
    print('5. Sair', end='\n')
    

    opcao = int(input('Digite a opção: '))


    match(opcao):
        case 1:
            print('Tela de Cadastro', end='\n')
            nome = input('Digite seu nome: ')
            email = input('Digite seu e-mail: ')
            idade = input('Digite sua idade: ')

            dados = {
                'Nome': [nome],
                'E-mail': [email],
                'Idade': [idade]
            }

            df = pd.DataFrame(dados)
            df.to_csv('listagem.csv', index=False, mode='a', header=not os.path.exists('listagem.csv'))

        case 2:
            df = pd.read_csv('listagem.csv')
            print(df.to_string(index=False))

        case 3:
            df = pd.read_csv('listagem.csv')
            email_update = input('Digite o e-mail do registro para atualizar seu registro: ')

            if email_update in df['E-mail'].values:
                df = df[df['E-mail'] != email_update]
                df.to_csv('listagem.csv', index=False)

                print('Digite os dados novos!')
                nome = input('Nome: ')
                email = input('E-mail: ')
                idade = input('Idade: ')

                dados = {
                'Nome': [nome],
                'E-mail': [email],
                'Idade': [idade]
                }   

                df_update = pd.DataFrame(dados)
                df_update.to_csv('listagem.csv', index=False, header=not os.path.exists('listagem.csv'), mode='a')
                print('Registro atualizado com sucesso!')
            else:
                print('E-mail não encontrado.')
        
        case 4:
            df = pd.read_csv('listagem.csv')
            email = input('Digite o e-mail do registro para exclusão: ')
            
            if email in df['E-mail'].values:
                df = df[df['E-mail'] != email]
                df.to_csv('listagem.csv', index=False)
                print('Registro removido com sucesso!')
            else:
                print('E-mail não encontrado.')
        case 5:
            break