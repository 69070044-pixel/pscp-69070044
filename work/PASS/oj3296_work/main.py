"""Mix Color RGB"""
def mixcolor(c1, c2):
    """Mix color 1, 2"""
    return (c1 + c2) // 2

def mixrgb(rgb1, rgb2):
    """return mix color value"""
    r1, g1, b1 = rgb1
    r2, g2, b2 = rgb2
    return [mixcolor(r1, r2), mixcolor(g1, g2), mixcolor(b1, b2)]

RGB1 = [int(x) for x in input().split()]
RGB2 = [int(x) for x in input().split()]
print(*mixrgb(RGB1, RGB2))
