import math

def test_f1(movements):
    print("OUTPUT")
    for movement in movements:
        print(movement)
    print("FINISH")

def test_f2(movements):
    x, y = 0, 0

    for movement in movements:
        direction, steps = movement.split()
        steps = int(steps)

        if direction == 'UP':
            y += steps
        elif direction == 'DOWN':
            y -= steps
        elif direction == 'LEFT':
            x -= steps
        elif direction == 'RIGHT':
            x += steps

    distance = round(math.sqrt(x**2 + y**2))
    print("OUTPUT")
    print(distance)
    print("FINISH")

# Example usage:
movements = ["UP 1", "DOWN 5", "LEFT 9", "RIGHT 12"]

print("1. Test f1 (2 marks)")
print("2. Test f2 (1 mark)")

selection = input("Your selection (1 -> 2): ")

if selection == "1":
    test_f1(movements)
elif selection == "2":
    test_f2(movements)
else:
    print("Invalid selection.")
