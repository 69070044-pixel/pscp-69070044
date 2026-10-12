"""Turnstile""" 
def main():
    """main funcion"""
    is_locked, pass_count = True, 0
    while True:
        action = input()
        if action == "C":
            is_locked = False
        elif action == "P" and not is_locked:
            pass_count += 1
            is_locked = True
        elif action == "END":
            break
    print(pass_count)

main()
