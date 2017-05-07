# coding: utf-8

def print_table():
    """
        Affiche la table de multiplication du nombre saisi par l'utilisateur.
        
        On s'assure ici, avant l'exécution du calcul que cette saisie
        est correcte, qu'il s'agit bien d'un entier.
        Si ce n'est pas le cas, on invite l'utilisateur à réitérer sa saisie.
    """
    
    print('Commencez par préciser le nombre dont vous souhaitez la table.\n')
    x = None
    prompt = 'Table de multiplication voulue : '
    
    while not isinstance(x, int):
        try:
            x = int(input(prompt))
        except:
            print('\nDésolé mais votre saisie ne semble ' \
                  'pas être un nombre entier.')
            prompt = 'Confirmez le numéro de la ' \
                     'table de multiplication voulue : '
        else:
            print('\nVoici la table de multiplication de {0} : '.format(x))
            for i in range(0, 11):
                # Méthode à retenir
                print('{0} * {1} = {2}'.format(x, i, x*i))
                # Autre méthode de chaine formatée :
                # print('%d * %d = %d' % (x, i, x*i))
                # Autre méthode de concaténation
                # print(str(x) + " * " + str(i) + " = " + str(x*i))
    
    print('\nEt voila !')

if __name__ == '__main__':
    print_table()