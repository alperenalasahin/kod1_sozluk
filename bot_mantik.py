import random
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def flip_coin():
    flip = random.randint(0, 1)
    if flip == 0:
        return "Tura"
    else:
        return "Yazı"