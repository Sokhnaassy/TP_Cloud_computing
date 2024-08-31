import random  # Importe le module random pour générer des nombres aléatoires

e = 79  # Clé publique exponentielle
d = 1019  # Clé privée exponentielle
N = 3337  # Module de chiffrement
M = 8  # Message à chiffrer

# Affiche les valeurs en entrée
print('== Valeur en entrées ====\n')
print('e =', e, 'd =', d, 'N =', N)
print('message =', M)
print('\n=============')

# Fonction pour chiffrer le message
def chiffrer_message(message, exponent, modulo):
    return message ** exponent % modulo

# Fonction pour déchiffrer le message
def dechiffrer_message(chiffre, exponent, modulo):
    return chiffre ** exponent % modulo

# Simule l'attaque Adaptive CCA
def attaque_adaptive_cca(chiffre, exponent, modulo):
    messages_dechiffres = []  # Initialise une liste pour stocker les messages déchiffrés
    for _ in range(10000):  # Répète le processus un grand nombre de fois pour simuler une attaque
        r = random.randint(1, modulo - 1)  # Génère un nombre aléatoire entre 1 et N - 1
        chiffre_dash = (chiffre * pow(r, exponent, modulo)) % modulo  # Simule la transformation du texte chiffré
        message_dechiffre = dechiffrer_message(chiffre_dash, exponent, modulo)  # Déchiffre le texte modifié
        messages_dechiffres.append(message_dechiffre)  # Ajoute le texte déchiffré à la liste
    return messages_dechiffres  # Retourne la liste des messages déchiffrés

# Chiffre le message
chiffre = chiffrer_message(M, e, N)  # Chiffre le message M avec la clé publique e et le module N
print('\nChiffré:\t', chiffre)  # Affiche le texte chiffré

# Attaque Adaptive CCA
messages_dechiffres = attaque_adaptive_cca(chiffre, d, N)  # Lance une attaque Adaptive CCA sur le texte chiffré

# Vérifie si Eve a correctement déchiffré le message
if any(message_dechiffre == M for message_dechiffre in messages_dechiffres):  # Vérifie si l'un des messages déchiffrés correspond au message original M
    print('Eve a craqué le message, car elle a obtenu au moins un résultat identique au message')  # Affiche un message si Eve a réussi à déchiffrer le message
    for message_dechiffre in messages_dechiffres:  # Parcourt tous les messages déchiffrés
        if message_dechiffre == M:  # Si le message déchiffré correspond au message original M
            print("Message déchiffré après l'attaque:", message_dechiffre)  # Affiche le message déchiffré correspondant
            break
else:
    print("Eve n'a pas craqué le message")  # Affiche un message si Eve n'a pas réussi à déchiffrer le message
