# Importons le module sympy et renommons le en sp
import sympy as sp 
# Définissons une fonction bezout prenant deux paramètres e1 et e2 représentant les clés publiques
def bezout(e1, e2):  
    # Calculons le PGCD étendu de e1 et e2, et récupèrons les coefficients de Bézout (u et v)
    g, u, v = sp.gcdex(e1, e2)  
    # Retourne les coefficients de Bézout u et v
    return u, v  
# Définissons une fonction att_mod_com comme attaque par module commun prenant cinq paramètres : 
    # c1 ( un chiffré ), c2 ( un deuxieme chiffré ), e1 (la clé publique utilisé pour qvoir le premier chiffré), 
    # e2 (la clé publique utilisé pour qvoir le deuxiéme chiffré), n (le module commun)
def att_mod_com(c1, c2, e, n):  
    # Appellons la fonction bezout pour obtenir les coefficients de Bézout u et v 
    u, v = bezout(e, e)  
    # Calculons le message déchiffré m en utilisant les coefficients de Bézout u et v, ainsi que les messages chiffrés c1 et c2 et le module n
    m = (pow(c1, int(u), n) * pow(c2, int(v), n)) % n
    # Retournons le message déchiffré m
    return m  

''' Bob a la clef publique (221, 11) et Catherine la clef (221, 11).
Oscar intercepte les chiffrés 210 et 58 à destinations respectives de Bob et Catherine. 
Retrouvons la différence entre les messages. '''

c1 = 210
c2 = 58
e = 11
n = 221

result = att_mod_com(c1, c2, e, n)
print('Le résultat correspond à la différence entre les messages déchiffrés m_diff :', result)
