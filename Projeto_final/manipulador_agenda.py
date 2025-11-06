# Tupla que contém os contatos suportados pelo sistema
contatos_suportados = ("telefone", "email", "endereco")

# Dicionário de exemplo, com alguns dados padrão
agenda = {
    "Pessoa 1":{
        "telefone": ["11 1234-56789"],
        "email": ["pessoa@email.com", "email@profissional.com"],
        "Endereco": ["Rua 123"]
    },
    "Pessoa 2": {
        "telefone": ["11 9874-5678"],
        "email": ["pessoa2@email.com", "pessoa2@profissional.com"],
        "Endereco": ["Rua 345"]
    }
}

def contato_para_texto(nome_contato: str, **formas_contato):
    """Recebe um nome de contato com string e um dicionário com as formas de contato.
       Retorna uma string com os dados recebidos."""
    formato_texto = f"{nome_contato}"
    for meio_contato, contato in formas_contato.items():
        formato_texto = f"{formato_texto}\n{meio_contato.upper()}"
        contador_formas = 1
        for valor in contato:
            formato_texto = f"{formato_texto}\n\t{contador_formas} - {valor.upper()}"
            contador_formas = contador_formas + 1

    return formato_texto

# Função de visualização da agenda completa
def agenda_para_texto(**agenda_completa):
    """Recebe um dicionário de dicionários com a agenda que será
       exibida e retorna uma string com este dicionário formatado"""
    formato_texto = ""
    for nome_contato, formas_contato in agenda_completa.items():
        formato_texto = f"{formato_texto} {contato_para_texto(nome_contato, **formas_contato)}\n"
        formato_texto = f"{formato_texto}--------------------------------\n"
    return formato_texto

# Função para alterar o nome de um contato
def altera_nome_contato(agenda_original: dict, nome_original: str, nome_atualizado: str):
    """Recebe a agenda original em forma de dicionário, o nome_original e o
       nome atualizado em forma de string.
       Busca o nome original no dicionário e retorna False se não encontrar.
       Retorna True se encontrar o nome original no dicionário e fizer
       a exclusão do contato antigo e inclusão do novo."""
    if nome_original in agenda_original.keys():
        copia_contatos = agenda_original[nome_original].copy()
        agenda_original.pop(nome_original)
        agenda_original[nome_atualizado] = copia_contatos
        return True
    return  False

# Função para alterar a forma de contato de alguém
def altera_forma_contato(lista_contatos: list, valor_antigo: str, novo_valor: str):
    """Recebe uma lista lista_contatos, o valor antigo que será substituído e o novo valor.
       Caso o valor antigo não esteja na lista, retornará False.
       Caso o valor antigo esteja na lista, será removido, o novo valor será incluído e retornará True."""

    if valor_antigo in lista_contatos:
        posicao_valor_antigo = lista_contatos.index(valor_antigo)
        lista_contatos.pop(posicao_valor_antigo)
        lista_contatos.insert(posicao_valor_antigo, novo_valor)
        return True
    return False

def exclui_contato(agenda: dict, nome_contato: str):
    """Recebe uma agenda completa como dicionário e o nome do contato como string.
       Caso o nome do contato não esteja nas chaves do dicionário, retornará False.
       Caso o nome do contato esteja nas chaves, o registro correspondente será
       removido e retornará True."""
    if nome_contato in agenda.keys():
        agenda.pop(nome_contato)
        return True
    return False

# Função para incluir um contato
def inclui_contato(agenda: dict, nome_contato: str, **formas_contato):
    """Recebe uma agenda completa como dicionário, o nome do novo contato
       como string e as formas de contato em um dicionário como **kwargs.
       Não é feita nenhuma verificação, portanto se já existir um contato
       com o mesmo nome, será sobrescrito."""
    #print(formas_contato)
    agenda[nome_contato] = formas_contato

inclui_contato(agenda, "Juquinha", telefone=["123456"], email=["a@b.com"])
print(agenda_para_texto(**agenda))