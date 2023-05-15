import os
from cmd import Cmd


def columnify(iterable):
    strings = [repr(x) for x in iterable]
    widest = max(len(x) for x in strings)
    padded = [x.ljust(widest) for x in strings]
    return padded


class MyPrompt(Cmd):

    def do_hello(self, args):
        """Says hello. If you provide a name, it will greet you with it."""
        if len(args) == 0:
            name = 'stranger'
        else:
            name = args
        print(f'Hello, {name}')  #

    def do_quit(self, args):
        """Quits out of the command line."""
        print('Quitting.')
        raise SystemExit

    def do_exit(self, args):
        """Exits out of the command line."""
        print('Exiting.')
        raise SystemExit

    def do_ls(self, args):
        if len(args) == 0:
            path = '.'
        else:
            path = args

        files = os.listdir(path)

        for file in files:
            full_path = os.path.join(path, file)
            print(f'{file}')

if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.prompt = '>'
    prompt.cmdloop('Starting prompt...')
