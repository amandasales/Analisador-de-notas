def notas(*n, sit=False):
    """
    -> Analisa notas
    :param n: números a serem analisados
    :param sit: mostra ou não a situação das notas
    :return: a análise em um dicionário
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(3.4, 2.2, 8.9, 10, sit=True)
print(resp)
help(notas)
