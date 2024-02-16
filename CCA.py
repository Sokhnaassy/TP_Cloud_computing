import libnum  # Importe la bibliothèque libnum pour les opérations numériques en cryptographie

e = 79  # Définit la clé publique exponentielle
d = 1019  # Définit la clé privée exponentielle
N = 3337  # Définit le module de chiffrement
r = 3  # Définit un nombre aléatoire
M = 8  # Définit le message à chiffrer

# Affiche les valeurs en entrée
print('== Valeur en entrées ====')
print('e =', e, 'd =', d, 'N =', N)
print('message =', M, 'r =', r)
print('\n=============')

# Calcule le chiffré
cipher = M ** e % N
print('\nChiffré:\t', cipher)

# Simule une demande de déchiffrement de la part d'Eve
cipher_dash = (cipher * pow(r, e, N)) % N
print('Eve demande à Bob de déchiffrer:\t', cipher_dash)

# Simule la tentative de déchiffrement de Bob
decipher = pow(cipher_dash, d, N)
print('Bob dit que le résultat est erroné:', decipher)

# Calcule le résultat correct en utilisant le module inversé
res = (decipher * libnum.invmod(r, N)) % N
print('Eve détermine comme:', res)

# Vérifie si Eve a correctement déchiffré le message
if res == M:
    print('Eve a craqué le message, car le résultat est le même que le message')
else:
    print('''Eve n'a pas craqué le message''')
