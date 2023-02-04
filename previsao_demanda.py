import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Carregar os dados em um DataFrame do Pandas
df = pd.read_excel("Dados.xlsx")
df['Data'] = pd.to_datetime(df['Data'], errors='coerce')
df['Data_num'] = (df['Data'] - df['Data'].min()) / np.timedelta64(1, 'D')

# Selecionar as colunas relevantes para o modelo de previsão
X = df[['Data_num']].values
y = df['Demanda'].values

# Treinar o modelo de regressão linear
model = LinearRegression()
model.fit(X, y)

# Criar um DataFrame com as próximas 5 datas
today = pd.to_datetime('today').date()
futura_datas = pd.DataFrame({'Data': pd.date_range(start='21-1-23', periods=5)})
futura_datas['Data_num'] = (futura_datas['Data'] - df['Data'].min()) / np.timedelta64(1, 'D')

# Adicionar as previsões de demanda ao DataFrame de datas futuras
futura_demanda = model.predict(futura_datas[['Data_num']].values)
futura_datas['Demanda prevista'] = futura_demanda

print(futura_datas)
