import math

def compute_circle_area(radius):
    return math.pi * radius * radius

print(compute_circle_area(11))
print(compute_circle_area(-11))

def non_negative_arguments(decorated_fn):

    def check_non_negative(*args):
        for arg in args:
            if arg < 0:
                raise ValueError("Input argment cannot be negative")

        return decorated_fn(arg)

    return check_non_negative

@non_negative_arguments
def compute_circle_area(radius):
    return math.pi * radius * radius

@non_negative_arguments
def compute_circle_perimeter(radius):
    return 2 * math.pi * radius

print(compute_circle_area(11))
#print(compute_circle_area(-11))

#print(compute_circle_perimeter(-11))