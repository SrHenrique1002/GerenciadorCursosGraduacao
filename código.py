import json
Cursos = []
ListaAlunos = list()
aluno = dict()


#Carregar arquivos com informações salvas previamente (Cursos, Alunos cadastrados)


print("Seja bem vindo ao GERENCIADOR DE CURSOS.")




#declarando as variáveis de soma e média, inicialmente, como zero
soma = media = 0
#lista para armazenar a idade para efetuar a média total dos alunos
#variáveis para armazenar quantidades por gênero
qtdF = 0
qtdM = 0
idades = list()
# Função Cadastrar Cursos
def CadastrarCurso(nomeCurso):
    if nomeCurso.upper() in Cursos:
        print("Erro: curso já cadastrado. ")
        return
    else:
        Cursos.append(nomeCurso.upper())
        print("Curso cadastrado!")
#Função calcular média de idade
def MediaIdade(ListaAlunos, nomeCurso):
    b = 0
    for a in ListaAlunos:
            if a['curso'] in nomeCurso.upper():
                b = a["idade"]
                idades.append(b)
    print(idades)

#Função quantidade de pessoas M/F
def qtdPessoas(ListaAlunos, nomeCurso):
    b = 0
    global qtdM
    global qtdF
    for a in ListaAlunos:
            if a['curso'] in nomeCurso.upper():
                b = a["genero"]
                if b == "M":
                    qtdM += 1
                elif b == "F":
                    qtdF += 1
# MENU
while True:
    print('-=' * 30)
    print(
        "GERENCIADOR DE CURSOS, escolha a opção que deseja:\n1 = Cadastrar um curso\n2 = Consultar Cursos cadastrados\n3 = Cadastrar Aluno\n4 = Consultar alunos matriculados em um curso\n5 = Verificar aluno matriculado\n6 = Remover aluno matriculado\n7 = Carregar base de alunos e cursos\n8 = Salvar informações de Alunos e Cursos\n9 = Apagar informações de Alunos e Cursos" )
    menu = int(input())
    # O programa começa com o cadastro de cursos:
    if menu == 1:
      while True:
        NovoCurso = str(input("Digite o nome do curso: "))
        CadastrarCurso(NovoCurso)
        while True:
            resp = str(input('Gostaria de cadastrar outro curso? [S/N] ')).upper()[0]
            if resp in 'SN':
              break
            print("ERRO: Resposta inválida.")
        if resp == 'N':
          break

    elif menu == 2:
        # Cursos cadastrados:
        if len(Cursos) != 0:
            print("Os cursos cadastrados são: ")
            for x in Cursos:
                print(x)
        else:
            print("ERRO: Não há cursos cadastrados.")
    elif menu == 3:
        # Cadastro de aluno:
        if len(Cursos) != 0:
            while True:
                aluno.clear()
                aluno['nome'] = str(input('Nome: ')).upper()
                while True:  # Gênero
                    print("Digite o gênero do aluno:")
                    print("'M' para Masculino / 'F' para Feminino / 'O' para outros")
                    aluno['genero'] = str(input('Gênero: ')).upper()[0]
                    if aluno['genero'] in 'MFO':
                        if aluno['genero'] == 'M':
                            break # MUDAR !!!!
                        elif aluno['genero'] == 'F':
                            break # MUDAR!!!
                        break
                    print('ERRO: Opção inválida. Digite apenas M, F ou O')
                    

                # ---
                while True:  # cpf
                    aluno_cpf = str(input('Digite o seu CPF: '))
                    if len(aluno_cpf) == 11:
                        aluno['cpf'] = aluno_cpf
                        break
                    else:
                        print('ERRO: CPF inválido!')
                while True:  # Curso
                    aluno['curso'] = str(input('Curso: ')).upper()
                    if aluno['curso'] in Cursos:
                        break
                    print('ERRO: Curso não cadastrado ou inexistente.')
                # Idade
                aluno['idade'] = int(
                    input('Idade: '))  # Aviso: falta colocar erro caso o usuário digite uma palavra, em vez de um número!!
                ListaAlunos.append(aluno.copy())
                while True:
                    resp = str(input('Gostaria de cadastrar outro aluno? [S/N] ')).upper()[0]
                    if resp in 'SN':
                        break
                    print("ERRO: Resposta inválida.")
                if resp == 'N':
                    break
            print('-=' * 30)
        else:
            print("Atenção: não há cursos cadastrados. Cadastre um curso e tente novamente.")

    elif menu == 4:
        # Lista de ALUNOS que cursam algum curso:
        contador = 0
        nomeCurso = str(input("Digite o nome do Curso para consultar alunos cadastrados: ")).upper()
        if nomeCurso in Cursos:
            print(f"Estudantes cadastrados - {nomeCurso.upper()} ")
            for a in ListaAlunos:
                if a['curso'] in nomeCurso.upper():
                    contador = contador + 1
                    print(f'{contador}. {a["nome"]} | {a["cpf"]} | {a["idade"]} anos | {a["genero"]}')
            print(f'O número total de alunos matriculados neste curso é: {contador}')

            resp = str(input("Gostaria de exportar para um arquivo? [S/N] "))

            if resp.upper() == 'S':
                contador = 0
                MediaIdade(ListaAlunos, nomeCurso)
                qtdPessoas(ListaAlunos, nomeCurso)
                media = sum(idades) / len(idades)
                with open(f'alunos_{nomeCurso}.txt', 'w') as f:
                    f.write(f"Estudantes cadastrados - {nomeCurso.upper()} \n")
                    for a in ListaAlunos:
                        if a['curso'] in nomeCurso.upper():
                            contador = contador + 1
                            f.write(f'{contador}. {a["nome"]} | {a["cpf"]} | {a["idade"]} anos | {a["genero"]} \n')
                    f.write(f'O número total de alunos matriculados neste curso é: {contador}')
                    f.write(f'\nA média de idade dos alunos é de {media:2f} anos')
                    f.write(f'\nTotal de alunos por gênero: \nMasculino: {qtdM} | Feminino: {qtdF}')
                    print(f"O arquivo foi salvo no diretório do programa, com o nome de 'alunos_{nomeCurso}.txt'")
        else:
            print("Curso não encontrado!")
    #Consulta de aluno
    elif menu == 5:
        if len(ListaAlunos) != 0:
            nome = str(input("Digite o nome do aluno para consultar: ")).upper()
            ConsultaAluno = [p for p in ListaAlunos if p['nome'] == nome]
            if len(ConsultaAluno) != 0:
                for a in ConsultaAluno:
                    print("Aluno cadastrado!")
                    print((f'Nome: {a["nome"]}\nCPF: {a["cpf"]}\nIdade: {a["idade"]} anos\nGênero: {a["genero"]}\n'))
            else:
                print("Aluno não encontrado.")
            ConsultaAluno.clear()
        else:
            print("Não há alunos cadastrados no sistema!")
            break
    #Remover aluno
    elif menu == 6:
        if len(ListaAlunos) != 0:
            nome = str(input("Digite o nome do aluno: ")).upper()
            for i in range(len(ListaAlunos)): 
                if ListaAlunos[i]['nome'] == nome:
                    print((f'Aluno encontrado: {nome}'))
                    confirmacao = str(input("Voce realmente deseja EXCLUIR esse aluno? A ação é irreversível. \n Para confirmar, digite 1: "))
                    if confirmacao == "1":
                        del ListaAlunos[i]
                        print("Aluno removido.")
                        break
                    else:
                        print("Retornando ao menu")
        else:
            print('Não há alunos cadastrados!')
    
    #Carregar informações de arquivos (Lista de Alunos e Cursos)
    elif menu == 7:
        with open("cursos.json") as file: 
            Cursos = json.load(file)
        with open("ListaAlunos.json") as file: 
            ListaAlunos = json.load(file)
        print("Informações recuperada com sucesso!")
        
    #Salvar as informações do programa em um arquivo (exportar)
    elif menu == 8:
        with open("cursos.json", "w") as outfile: 
            json.dump(Cursos, outfile)
        with open ("ListaAlunos.json", "w") as outfile:
            json.dump(ListaAlunos, outfile)
        print("As informações foram salvas com sucesso.")
    
    #Excluir a lista de alunos e cursos
    elif menu == 9:
        confirmacao = str(input("Voce realmente deseja EXCLUIR as informações de alunos e cursos previamente cadastrada? A ação é irreversível. \n Para confirmar, digite 1: "))
        if confirmacao == "1":
            ListaAlunos = []
            Cursos = []
            with open("cursos.json", "w") as outfile: 
                json.dump(Cursos, outfile)
            with open ("ListaAlunos.json", "w") as outfile:
                json.dump(ListaAlunos, outfile)
            print("As informações foram apagadas com sucesso.")
        else:
            print("Retornando ao menu.")

    
    else:
        print("Digite um valor válido!")