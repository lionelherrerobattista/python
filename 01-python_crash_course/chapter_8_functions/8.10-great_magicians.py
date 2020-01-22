def show_magicians(magicians):
    """Shows magicians in a list"""
    print("List of magicians:")
    for magician in magicians:
        print(magician.title())
        
def make_great(magicians):
    """Makes every magician in the list a Great Magician"""
    great_magicians = []
    
    while magicians:
        magician = magicians.pop()
        magician = "the Great " + magician
        great_magicians.append(magician)
    
    while great_magicians:
        magician = great_magicians.pop()
        magicians.append(magician)
        
        
        
magicians = ['merlin', 'harry potter', 'gandalf']
make_great(magicians)
show_magicians(magicians)
