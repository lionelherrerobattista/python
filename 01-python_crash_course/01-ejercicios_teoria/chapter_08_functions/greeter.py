def get_formatted_name(first_name, last_name): #valor opcional
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    
    return full_name.title()
    
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    
    first_name = input("First name: ")
    if first_name == 'q':
        break
        
    last_name = input("Last name: ")
    if last_name == 'q':
        break
        
    formatted_name = get_formatted_name(first_name, last_name)
    print("\nHello, " + formatted_name + "!")