from math import gcd  # Importe la fonction gcd (pgcd) depuis le module math
from sympy import *  # Importe toutes les fonctions et constantes de sympy
from random import randint  # Importe la fonction randint pour générer des nombres aléatoires

# Génération des nombres premiers p et q
p, q = nextprime(2^50), nextprime(2^30)

# Calcul du module de chiffrement N
N = p * q

# Calcul de la fonction d'Euler φ(N)
phi = ((p - 1) * (q - 1))

# Choix de l'exposant de chiffrement e
e = randint(2, phi - 1)
while gcd(e, phi) != 1:
    e = randint(2, phi - 1)

# Calcul de la clé privée d
d = pow(e, -1, phi)

# Affichage des paramètres du système de chiffrement
print('p = {}\nq = {}\nN = {}\nphi(N) = {}\n'.format(p, q, N, phi))
print("Clé privée de Bob : d = {}, Clé publique : e = {}".format(d, e))

# Alice envoie un message à Bob
m = 39
c = pow(m, e, N)
print('Alice envoie m = {} à Bob comme m^e = {}'.format(m, c))

# Bob déchiffre le message
m_decrypted = pow(c, d, N)
print('Bob déchiffre c = {} en m = c^d = {}'.format(c, m_decrypted))

# Attaque à texte clair choisi sur le chiffrement RSA de type "Textbook RSA"
espace_texte_clair = range(200)
for t in espace_texte_clair:
    if pow(t, e, N) == c:
        print('Eve a trouvé le message : {}'.format(t))
