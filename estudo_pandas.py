# %% [markdown]
# # AceleraDev Codenation - Módulo 02
# ## Tiago Ferreira

# ## Manipulando dados

# %%
import pandas as pd 
import numpy as np
# %%
pd?

# %% [markdown]
# ## Dicionários
# %%
dados = {
    'canal_vendas' : ['facebook','twitter','instagram','linkedin','facebook'],
    'acessos' : [100,200,300,400,500],
    'site' : ['site1','site2','site3','site4','site5'],
    'vendas' : [1000.52,1032.34,2002,5000,30]
}

# %%
#visualizando dicionário
dados

# %%
#verificando o tipo da variável
type(dados)

# %%
#acessando uma chave específica
dados['canal_vendas']

# %%
#acessando as chaves do dicionário
dados.keys()

# %%
#acessando uma posição específica do dicionário
dados['site'][3]

# %%
#acessando uma fatia do dicionário
dados['canal_vendas'][:3]

# %% [markdown]
# ## Listas


# %%
#criando uma
lista = [200,200,300,800,200]

# %%
#passando uma lista para dentro de um dicionário
dados['lista'] = lista
dados

# %% [markdown]
# ## DataFrames

# %%
#crir um data frame a partir de um dict
dataframe = pd.DataFrame(dados)

# %%
#acessando o dataframe
dataframe

# %%
#printando os primeiros casos do dataframe
dataframe.head(3)

# %%
#verificando o formato do DataFrame
dataframe.shape

# %%
#acessando o índice
dataframe.index

# %%
#verificando os tipos dos dados do dataframe
dataframe.dtypes.value_counts()

# %%
#verificando se existem valores faltantes
dataframe.isna().sum()

# %%
#acessando uma coluna específica
dataframe.columns

# %%
#acessando uma coluna específica
dataframe['canal_vendas']

# %%
#criando uma lista de uma coluna
list(dataframe['canal_vendas'])

# %%
#criando uma nova coluna
dataframe['nova_coluna'] = [1,2,3,4,5]
dataframe

# %%
#removendo colunas
dataframe.drop(columns='nova_coluna', inplace=True)
dataframe

# %%
aux = dataframe.pivot(index='canal_vendas',columns='site',values='acessos').fillna(0)

# %%
aux.melt(id_vars='canal_venda',value_vars=['site1','site2','site3'])