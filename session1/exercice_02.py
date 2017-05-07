# coding: utf-8

def print_unique_chars():
    """
        Détecte et affiche tous les caractères d'une chaîne de caractères
        saisie par l'utilisateur, en omettant les espaces et les doublons.
        
        On s'assure ici, avant l'exécution du parsing que cette saisie
        est correcte, qu'il s'agit bien d'une chaîne de caractères.
        Si ce n'est pas le cas, on invite l'utilisateur à réitérer sa saisie.
    """

    print('Commencez par préciser la chaîne à analyser.\n')
    x = None
    prompt = 'Chaîne à analyser : '
    
    while not isinstance(x, str):
        try:
            x = str(input(prompt))
        except:
            print('\nDésolé mais votre saisie ne semble ' \
                  'pas être une chaîne de caractères.')
            prompt = 'Confirmez la chaîne à analyser : '
        else:
            chars = []
            for char in x:
                if char != ' ' and char not in chars:
                    chars.append(char)
            print('Voici les caractères qui la composent, ' \
                  'hors espaces et doublons : ')
            print(chars)

if __name__ == '__main__':
    print_unique_chars()