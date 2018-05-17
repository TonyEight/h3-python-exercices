# coding: utf-8

def print_and_count_unique_chars():
    """
        Détecte et affiche tous les caractères d'une chaîne de caractères
        saisie par l'utilisateur, en omettant les espaces et les doublons.
        Calcule également le nombre d'occurences de chacun de ces caractères.
        
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
            chars = {}
            for char in x:
                if char != ' ':
                    if char not in chars.keys():
                        chars[char] = 1
                    else:
                        chars[char] += 1
            print('Voici les caractères qui la composent, ' \
                  'hors espaces : ')
            result = 'Le caractère "{0}" apparaît {1} fois.'
            for char, occur in chars.items():
                print(result.format(char, occur))

if __name__ == '__main__':
    print_and_count_unique_chars()
