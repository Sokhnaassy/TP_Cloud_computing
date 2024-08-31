import sympy as sp

def attaque_hastad(chiffrements, modules_publics):
    # Calcul du produit des modules publics
    n = sp.prod(modules_publics)  
    
    # Calcul de la somme des chiffrements
    somme_chiffrements = sum(chiffrements)  
    
    # Calcul de la somme des modules publics
    somme_modules = sum(modules_publics)  
    
    # Calcul de l'inverse modulaire de la somme des modules par rapport au produit des modules
    resultat, u, _ = sp.gcdex(somme_modules, n)  
    
    # Déchiffrement du message
    texte_clair = (somme_chiffrements * u) % n  
    
    return texte_clair

# Exemple d'utilisation
c1=345
c2=217
c3=502
n1=791
n2=883
n3=929

chiffrements = [c1, c2, c3] # Chiffrements du même message avec différents exposants
modules_publics = [n1, n2, n3] # Modules RSA correspondants

texte_clair = attaque_hastad(chiffrements, modules_publics)
print("Message déchiffré:", texte_clair)
