import random

"""This File contains defines operations classes to be used for generating
random art"""


def main():
    print(generate_expression())

def generate_expression(probability=0.99):

    if random.random() < probability:
        return random.choice([sin_pi,
                              cos_pi,
                              average,
                              sin_x_cos,
                              abs_val,
                              square,
                              cube,
                              sin_square,
                              mult,
                              root,
                              cos_square,
                              sin_tan,
                              cos_tan,
                              sin_pi_plus,
                              cos_pi_plus,
                              average_3,
                              invert,
                              arctan,
                              well])(probability)
    else:
        return random.choice(["x", "y"])

def sin_pi_plus(probability):
    return "sin(pi+" + str(generate_expression(probability**2)) + ")"

def cos_pi_plus(probability):
    return "cos(pi+" + str(generate_expression(probability**2)) + ")"

def sin_tan(probability):
    return "sin(pi*tan(" + str(generate_expression(probability**2)) + "))"

def cos_tan(probability):
    return "cos(pi*tan(" + str(generate_expression(probability**2)) + "))"

def sin_x_cos(probability):
    return ("sin(pi*" + str(generate_expression(probability**2)) + ")*cos(pi*"
           + str(generate_expression(probability**2)) + ")")

def sin_pi(probability):
    return "sin(pi*" + str(generate_expression(probability**2)) + ")"

def sin_square(probability):
    return "(sin(pi*" + str(generate_expression(probability**2)) + ")**2)"

def cos_square(probability):
    return "(cos(pi*" + str(generate_expression(probability**2)) + ")**2)"

def cos_pi(probability):
    return "cos(pi*" + str(generate_expression(probability**2)) + ")"

def average(probability):
    return ("avg(" + str(generate_expression(probability)) + "," +
            str(generate_expression(probability)) + ")")

def square(probability):
    return "square(" + str(generate_expression(probability**2)) + ")"

def cube(probability):
    return "cube(" + str(generate_expression(probability**2)) + ")"

def root(probability):
    return "root(" + str(generate_expression(probability**2)) + ")"

def abs_val(probability):
    return "abs(" + str(generate_expression(probability**2)) + ")"

def mult(probability):
    return ("(" + str(generate_expression(probability**2)) + "*"
           + str(generate_expression(probability**2)) + ")")

def average_3(probability):
    return ("average_3(" + str(generate_expression(probability)) + "," +
            str(generate_expression(probability)) + "," +
            str(generate_expression(probability)) + ")")

def invert(probability):
    return "(" + str(generate_expression(probability**2)) + "*-1)"

def arctan(probability):
    return "(.5*atan(" + str(generate_expression(probability**2)) + "))"

def well(probability):
    return "(1-(2/(1+" + str(generate_expression(probability**2)) + "**2))**8)"

def tent(probability):
    return "(1-(2*abs(" + str(generate_expression(probability**2)) + "))"

if __name__ == '__main__':
    main()
