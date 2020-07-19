class MyExercise():
    def __init__(self, *args):
        pass

    def print_until_number(self, number):
        i = 0
        while i < number:
            print(i + 1)
            i += 1


def main():
    #write your code below this line
    MyExercise().print_until_number(2)

if __name__ == '__main__':
    main()
