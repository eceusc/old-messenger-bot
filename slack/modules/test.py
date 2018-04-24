import sys
from importlib import import_module

def main():
    if len(sys.argv) < 2:
        print('You must pass in a name of a module to test! ex `python3 test.py galex`')
        return

    cmd_test = sys.argv[1]

    args = []
    if len(sys.argv) > 2:
        args = sys.argv[2:]
    #args.insert(0, cmd_test)

    print('\n================== BEGIN TEST =====================')
    print('Testing the process function inside "{}"...'.format(cmd_test))

    try:
        module = import_module(cmd_test)# + '.py')

        print('Calling `{}.process({})`...'.format(cmd_test, args))

        res = module.process(args)
    except Exception as e:
        print('oh No! Unknown error: "{}"'.format(e))
        print('Test Failed :(')
        print('================== END TEST =======================')
        return
    print('Message to send: "{}"'.format(res))
    print('Test Successful!')
    print('================== END TEST =======================\n')

if __name__ == '__main__':
    main()
