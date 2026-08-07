"""OJ2981"""

def main():
    """main function"""
    first_name = input() # INPUT FIRSTNAME
    last_name = input() # INPUT LASTNAME
    short_name = first_name[:2] + last_name[:2] # CREATE SHORTNAME
    fullname = first_name + " " + last_name # COMBINED
    # OUTPUT
    print(f"Hello {fullname}")
    print(short_name)
main()
