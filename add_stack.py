import argparse
__description__ = 'combine stack and app space att address 0xf000'

def main():
    """combine stack and app space att address 0xf000"""
    result = True
    parser = argparse.ArgumentParser(description=__description__)

    parser.add_argument('-a', '--app_name', type=str, default="simple_peripheral_cc2650lp_app.bin",
                        help=('path to global location app'
                              '(default: %(default)s)'))
    parser.add_argument('-s', '--stack_name', type=str, default="simple_peripheral_cc2650lp_stack.bin",
                        help=('path to global location stack'
                              '(default: %(default)s)'))
    args = parser.parse_args()
    print("app name {}".format(args.app_name))
    print("stack name {}".format(args.stack_name))
    file_bin_new = open(args.app_name[:-4]+'_with_stack.bin', 'wb')
    file_app = open(args.app_name, 'rb')
    app = file_app.read()
    file_stack = open(args.stack_name, 'rb')
    stack = file_stack.read()
    app_list = list(app)
    stack_list = list(stack)
    for i in range(0xffff):
        app_list[0xf000+i] = stack_list[i]
    print("inserted")
    app = bytearray(app_list)
    file_bin_new.write(app)
    file_bin_new.close()
    file_app.close()
    file_stack.close()


if __name__ == "__main__":
    main()
