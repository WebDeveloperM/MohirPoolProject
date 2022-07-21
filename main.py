from university import University


def main():
    choice = ''
    while choice != 'exit':
        print('System for Students !!! For adding Student type = A, '
              'For removing Student type = D, For finding Student type = F '
              'For show all data about students type = S ')
        choice = input('Choose some method: ')

        university = University()
        if choice == 'A':
            university.add()
        elif choice == 'F':
            university.find()
        elif choice == 'S':
            university.display_all()
        elif choice == 'D':
            university.remove()
        else:
            print('Wrong choice, You are going exist.')


if __name__ == '__main__':
    main()
