
def processPlayerCol(text):
    """
    This function extracts name, position and club from the player column
    """
    name, rest = text.split('\n')
    position, club = [x.strip() for x in rest.split('—')]
    return Series([name, position, club], index=['player', 'position', 'club'])