# Palindrome

## Objectif :
Produire un script en python permettant de calculer le plus grand palindrome issu de la multiplication de 4 entiers à 4 chiffres.

## Problématique :
Afin de déterminer quel est le plus grand palindrome nous devons calculer toutes les combinaisons possibles, c'est-à-dire les 6.561e+15 possibilités.
Pour cela nous pouvons utiliser une boucle for, cependant la complexité de notre code augmenterait drastiquement et serait de l'ordre de O(n^4). 

## Optimisations :
### Première optimisation :
En ce qui concerne notre première optimisation nous allons changer la façon dont les boucles for vont générer notre résultat.
```py
for i in range(1000, 10000):
    for j in range(1000, 10000):
        for k in range(1000, 10000):
            for l in range(1000, 10000):
```
Nous allons passer d'une boucle qui calcule dans un ordre croissant à une boucle qui calcule dans un ordre décroissant.
```py
for i in range(9999, 999, -1):
    for j in range(9999, 999, -1):
        for k in range(9999, 999, -1):
            for l in range(9999, 999, -1):
```
Suite à cela nous allons modifier le départ des boucles inférieures pour essayer de réduire le nombre d'opérations effectuées par notre programme.
```py
for i in range(9999, 999, -1):
    for j in range(i, 999, -1):
        for k in range(j, 999, -1):
            for l in range(k, 999, -1):
```
### Deuxième optimisation :
Afin de rendre le code le plus lisible possible nous allons créer une fonction qui nous permettra d'identifier les palindromes :
```py
def is_palindrome(product):
    return str(product) == str(product)[::-1]
```
Ensuite nous allons créer une deuxième fonction qui comprendra notre boucle for et nous permettra de générer des palindromes, nous allons l'appeler generate_palindrome : 
```py
def generate_palindrome():
    palindrome = []
    for i in range(9999, 999, -1):
        for j in range(i, 999, -1):
            for k in range(j, 999, -1):
                for l in range(k, 999, -1):
                    product = i * j * k * l
                    if is_palindrome(product):
                        palindrome.append(product)
    return palindrome
```
Cependant le temps d'exécution de cette fonction reste pharamineux, nous allons donc modifier son comportement.
### Troisième optimisation :
La logique adoptée pour la suite du projet est assez simple, on considère que les palindromes qui sont trouvés sur les intervalles les plus proches de 9999 sont plus larges que ceux sur les intervalles éloignés de 9999.  
Nous allons donc raccourcir le temps d'exécution de notre fonction en ne testant que les intervalles les plus proches de 9999.  
Pour ce faire nous allons modifier la fonction generate_palindrome() :
```py
def generate_palindrome(limit=999):
    max_palindrome = 0
    palindrome_finder = 0
    for i in range(9999, limit, -1):
        for j in range(i, limit, -1):
            for k in range(j, limit, -1):
                for l in range(k, limit, -1):
                    product = i * j * k * l
                    if max_palindrome < product and is_palindrome(product):
                        max_palindrome = product
    return (max_palindrome, palindrome_finder)
```
Maintenant notre fonction generate_palindrome() nous retournera uniquement le plus grand palindrome sur un intervalle donné, de plus il nous retournera aussi le nombre de palindrome trouvé.
### Dernière optimisation :
Pour notre dernière optimisation nous allons créer une fonction qui va appeler generate_palindrome() sur plusieurs intervalles.
```py
def max_palindrome():

    max_generated_palindrome = 0
    for i in range(99, 1, -1):
        (generated_palindrome, palindrome_finder) = generate_palindrome(i * 100)
        if generated_palindrome > max_generated_palindrome:
            max_generated_palindrome = generated_palindrome
        elif (
            generated_palindrome == max_generated_palindrome
            and generated_palindrome != 0
            and palindrome_finder > 1
        ):
            break
    return max_generated_palindrome
```
Notre fonction va donc appeler generate_palindrome() sur un intervalle et récupérer le plus grand palindrome généré s'il est supérieur au plus gros palindrome actuel.  
En ce qui concerne notre condition d'arrêt, notre programme va cesser de fonction une fois qu'il aura récupéré plusieurs fois le même résultat et que plusieurs palindromes auront été généré.  
Cette dernière vérification nous permet de ne pas rater un potentiel palindrome se trouvant dans un intervalle plus bas.

## Solution : 
Lors de mon premier commit j'ai pu obtenir le bon résultat avec un temps moyen de 56 secondes.  
Cependant j'ai rajouté une dernière vérification qui compte le nombre de palindromes retourné afin d'être sûr que notre palindrome soit bien le plus grand. Cette modification force le programme à faire une itération de plus sur un intervalle encore plus imposant et le temps moyen d'exécution est passé à 180 secondes.