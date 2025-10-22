# Pandas (Manipulacion y analisis de datos)

import pandas as pd

example = pd.read_excel("example1.xlsx")

print(example.head)
# Returns all dataframe data

# Get only a column elements
names = example["Nombre completo"]
print(names,"\n")
# Returns all "Nombre completo" elements, and its type

# Get "Dirección" and "Telefono" 
id_name = example[["Dirección","Teléfono"]] # Double bracket
print(id_name,"\n")

# dataframe.shape: Returns the total number of (rows, columns)
print("Total rows , colums",example.shape,"\n")

# Get rows
dataA = example[example["Grupo de clientes"] == 'A'] # < , >= , <= , != , == ; can work too
print(dataA,"\n")
# This is similar to SQL queries; search for all rows that match the condition, and returns all true rows in the output
print("Total elements in dataA: ",dataA.shape,"\n")

# .isin() condition; compare rows conditions to returns all true elements
client_group = example[example["Grupo de clientes"].isin(['B','D'])]
print("Only B and D groups",client_group)
