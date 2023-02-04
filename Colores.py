def red(text):
    print("\033[31m {}" .format(text))


def green(text):
    print("\033[32m {}" .format(text))


def white(text):
    print("\033[0m {}" .format(text))


def yellow_c(text):
    print('\033[33m\033[3m {}' .format(text))


def yellow(text):
    print('\033[33m {}' . format(text))


def lightblue(text):
    print('\033[36m {}' .format(text))


def purple(text):
    print('\033[35m {}'.format(text))


def money(text):
    print('\033[33m {}' .format(text), end="")


def reward(text):
    print('\033{0m {}' .format(text), end="")

