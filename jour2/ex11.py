nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#  Créer en une seule ligne : une liste des carrés, une liste des nombres pairs, et une liste des nombres > 5.
# 1. Transformer
# [expression for element in liste]

# 2. Filtrer
# [expression for element in liste if condition]

# 3. Transformer avec un choix
# [expression1 if condition else expression2 for element in liste]

care=[n*2 for n in nombres ] 
print(care)
pair=[n for n in nombres if n %2==0]
sup_cinq=[n for n in nombres if n>5]


print (care,pair,sup_cinq)