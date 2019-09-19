def velocidade(espaco, tempo);
    v = espaco/tempo
    return 'velocidade: {} m/s'.format(v)

def dados(nome, idade=None):
    if(idade is not None):
        return 'idade: {}'.format(idade)
    else:
        return 'idade: nao informada'
    
