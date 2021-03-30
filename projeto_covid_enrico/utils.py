import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def scatter_dois_dados(dados, x, y, typex='single', typey='single', padrao='location'):
    """
    
    
    dados - DataFrame
    x - Coluna desejada para o eixo X
    y - Coluna desejada para o eixo Y
    typex - Tipo de Dado da coluna destinada na variavel x ('single'- dados da linha; 'share' - dados que todas linhas compatilham; 'last'- dado que atualiza a cada linha)
    typey - Tipo de Dado da coluna destinada na variavel y ('single'- dados da linha; 'share' - dados que todas linhas compatilham; 'last'- dado que atualiza a cada linha)
    padrao - Coluna para o agrupamento de dados
    
    return - None
    """
    if typex == 'single':
        eixox = list(dados.groupby([padrao])[x].sum())
    elif typex == 'share':
        eixox = list(dados.groupby([padrao])[x].mean())
    elif typex == 'last':
        eixox = list(dados.groupby([padrao])[x].last())
    if typey == 'single':
        eixoy = list(dados.groupby([padrao])[y].sum())
    elif typey == 'share':
        eixoy = list(dados.groupby([padrao])[y].mean())
    elif typey == 'last':
        eixoy = list(dados.groupby([padrao])[y].last())
    plt.scatter(eixox, eixoy)
    x = x.replace("_", " ").upper() 
    y = y.replace("_", " ").upper()
    
    arrx=np.array(eixox)
    arry=np.array(eixoy)
    arrx[np.isnan(arrx)] = 0
    arry[np.isnan(arry)] = 0
    #regressão linear simples
    m, b = np.polyfit(arrx, arry, 1)
    #m = slope, b=intercept
    plt.plot(arrx, m*arrx + b)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(f"{x} X {y}")
    plt.show()
    return None
                     
def histog_dado(dados, h, typeh='single', padrao='continent'):
    """
    dados - DataFrame
    h - Coluna desejada para o eixo X
    typeh - Tipo de Dado da coluna destinada na variavel h ('single'- dados da linha; 'share' - dados que todas linhas compatilham; 'last'- dado que atualiza a cada linha)
    padrao - Coluna para o agrupamento de dados
    
    return - None
    """
    
    index = list((dados.groupby([padrao])[h].sum()).index)
    if typeh == 'single':
        h = list(dados.groupby([padrao])[h].sum())
    elif typeh == 'share':
        h = list(dados.groupby([padrao])[h].mean())
    elif typeh == 'last':
        h = list(dados.groupby([padrao])[h].last())
    plt.bar(index, h)
    plt.ylabel(h.replace("_", " ").upper())
    plt.xlabel(padrao.replace("_", " ").upper())
    plt.title(h.replace("_", " ").upper())
    return None 