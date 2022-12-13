# Script do Exercício Prático sobre Programação por Metas
# Adaptação retirada do livro: Pesquisa Operacional. Autor: Taha, H.A.

# Anúncio de propaganda. 

# Importar as bibliotecas
import numpy as np
import pandas as pd
import pyomo.environ as pyo

# Declaração do Modelo
modelo = pyo.ConcreteModel()

# Variáveis de desvios: 
modelo.d1menos = pyo.Var(within = pyo.NonNegativeReals) ## desvio da meta 1 negativo
modelo.d1mais = pyo.Var(within = pyo.NonNegativeReals)  ## desvio da meta 1 positivo
modelo.d2menos = pyo.Var(within = pyo.NonNegativeReals) ## desvio da meta 2 negativo
modelo.d2mais = pyo.Var(within = pyo.NonNegativeReals)  ## desvio da meta 2 positivo

# Variáveis de descisão:
modelo.x1 = pyo.Var(within = pyo.NonNegativeReals)  ## Total de Dados/minuto no rádio
modelo.x2 = pyo.Var(within = pyo.NonNegativeReals)  ## Total de Dados/minuto na televisão
modelo.x3 = pyo.Var(within = pyo.NonNegativeReals)  ## Total de Dados/minuto na internet

# Função Objetivo
modelo.z = pyo.Objective(expr = 3*modelo.d1menos + 1.5*modelo.d2mais + 0*modelo.d1mais + 0*modelo.d2menos, sense = pyo.minimize)

# Restrições
## 5x1 + 7x2 + 9x3 + d1menos - d1mais = 60 (Meta de Exposição)
modelo.exposicao = pyo.Constraint(expr = 5*modelo.x1 + 7*modelo.x2 + 9*modelo.x3 + modelo.d1menos - modelo.d1mais == 60)

## 10x1 + 30x2 + 25x3 + d2menos - d2mais = 170 (Meta Orçamentaria)
modelo.orcamentaria = pyo.Constraint(expr = 10*modelo.x1 + 30*modelo.x2 + 25*modelo.x3 + modelo.d2menos - modelo.d2mais == 170)

## 2x1 + 3x2 + 4x3 <= 20 (Limite de Pessoal)
modelo.pessoal = pyo.Constraint(expr = 2*modelo.x1 + 3*modelo.x2 + 4*modelo.x3 <= 20)

## x1 <= 6 (Limite de rádio)
modelo.radio = pyo.Constraint(expr = modelo.x1 <= 6)

## x2 <= 4 (Limite de televisão)
modelo.televisao = pyo.Constraint(expr = modelo.x2 <= 4)

## x3 >= 1 (Limite de internet)
modelo.internet = pyo.Constraint(expr = modelo.x3 >= 1)


# modelo.pprint()

# Resolvendo o Modelo de PO - Solver
resultado = pyo.SolverFactory('glpk').solve(modelo)

# Escrevendo o resultado
resultado.write()

## valor de minimização
print(f'Custo final: {modelo.z()}')

print(f' x1: {modelo.x1()}, x2: {modelo.x2()}, x3: {modelo.x3()}')

print(f'd1menos: {modelo.d1menos()}, d1mais: {modelo.d1mais()}, d2menos: {modelo.d2menos()}, d2mais:{modelo.d2mais()}')


