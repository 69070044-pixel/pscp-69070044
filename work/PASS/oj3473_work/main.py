"""FourDirections"""
lines = ["", "", "", "", ""]

def create_arrow(*parts):
    """build arrow"""
    for i, v in enumerate(parts):
        lines[i] += v

for ch in input().upper():
    if ch == "U":
        create_arrow("  *   ", " ***  ", "* * * ", "  *   ", "  *   ")
    if ch == "D":
        create_arrow("  *   ", "  *   ", "* * * ", " ***  ", "  *   ")
    if ch == "L":
        create_arrow("  *   ", " *    ", "***** ", " *    ", "  *   ")
    if ch == "R":
        create_arrow("  *   ", "   *  ", "***** ", "   *  ", "  *   ")

print(*lines, sep="\n")
