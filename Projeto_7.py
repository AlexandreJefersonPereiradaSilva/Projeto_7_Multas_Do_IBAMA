import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('arrecadacao_de_bens_tutelados.csv',
                 sep=';', decimal=',')


#df.info()
maiores_multas = df.groupby('Nome ou Razão Social')['Valor Pago'].sum().sort_values(ascending=False).head(10) #numero de linhas a serem inseridas
print(maiores_multas)

menores_multas = df.groupby('Nome ou Razão Social')['Valor Pago'].sum().sort_values(ascending=False).tail(10) #numero de linhas a serem inseridas
print(maiores_multas)


grafico = pd.concat([maiores_multas, menores_multas])

plt.figure(figsize=(12,8))
grafico.plot(kind='barh')
plt.title('Arrecadação de Bens Tutelados')
plt.xlabel('Nome ou razão Social')
plt.ylabel('Valor Pago')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('analise_bens_tutelados.png')
plt.show()
print("Grafico salvo com Sucesso!")