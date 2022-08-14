from random import randint


def main():
    print('Command line:')
    done = True
    while done:
        new_data = input()
        args = get_list_of_commands_from_line(new_data)
        print(args)
        if args == ['']:
            done = False


class Person:
    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name
        self.u_id = randint(0, 10000)


def print_u_id(self):
    print(self.u_id)


def get_list_of_commands_from_line(text_line, sep=' '):
    """
    Function return the list of commands from the string text_line with separators
    :param text_line: text contain string
    :param sep: separator
    :return:
    """
    list_of_args = []
    sep_pos = text_line.rfind(sep)
    while sep_pos > -1:
        list_of_args.append(text_line[sep_pos + 1:])
        text_line = text_line[:sep_pos]
        sep_pos = text_line.rfind(sep)
    list_of_args.append(text_line)
    return list_of_args


main()
