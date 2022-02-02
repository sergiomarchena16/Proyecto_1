# 'Proyecto 1 - Deteccion de Ataques'
# Sergio Marchena - 16387
# Project: SIMARGL
# February 2022

# Librerias a utlizar
import numpy as np
import pandas as pd

# Load the dataset
df_part1 = pd.read_csv("D:\datasets\dataset-part1.csv", encoding='utf-8')
df_part2 = pd.read_csv("D:\datasets\dataset-part2.csv", encoding='utf_8')

df_part1.head()