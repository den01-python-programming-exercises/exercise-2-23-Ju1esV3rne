class MyExercise():
    def __init__(self, number):
        self.number = number

    def pprint_until_number(self):
        i = 0
        while i < self.number:
            print(i + 1)
            i += 1

def print_until_number():
    #write your code below this line
    MyExercise(3).pprint_until_number()

if __name__ == '__main__':
    main()
