#!/usr/bin/env python
# coding: utf-8

# In[42]:


import numpy as dsa

class Calculations():
    def __init__(self, dados):
        self.dados_vendas = dados
        
    def sales_total(self):
        print(f'\033[34mrendas mensais:\033[m')
        for p, v in enumerate(self.dados_vendas):
            sum_total = dsa.cumsum(v)
            print(f'No mês {p + 1} a renda mensal foi de: {sum_total[3]}')
    
    def price_products(self):
        print('\033[32mProdutos\033[m')
        lst = []
        for p, v in enumerate(self.dados_vendas.T):
            sum_products = dsa.cumsum(self.dados_vendas[:12, p - 1])
            lst.append(sum_products)
            print(f'O produto {p + 1} faturou: {sum_products[len(sum_products) - 1]}')
             

def main():
    #dados
    dados_vendas = dsa.array([
    [100, 150, 200, 120],
    [120, 130, 180, 110],
    [90, 160, 210, 100],
    [80, 140, 190, 130],
    [110, 170, 220, 150],
    [130, 180, 230, 120],
    [150, 200, 250, 140],
    [140, 190, 240, 160],
    [120, 170, 210, 110],
    [110, 160, 200, 90],
    [130, 180, 220, 120],
    [140, 190, 230, 130]
])
    
    company = Calculations(dados_vendas)

    #calcula a soma mensal dos produtos
    company.sales_total()
    
    print('')
    
    #calcula o valor de cada produto
    company.price_products()
    
    
#código principal
if __name__ == '__main__':
    main()

