class ClassName(object):
    def __init__(self):
        self.print_until_number(2)

    def print_until_number(self, number):
        i = 0
        while i < number:
            print(i + 1)
            i += 1


def main():
    #write your code below this line
    ClassName()

if __name__ == '__main__':
    main()
