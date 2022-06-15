#!/usr/bin/python3

def split_args(args):
    args_dict = {}
    for i in range(len(args)):
        splitted = args[i].split('=',1)
        args_dict[splitted[0]] = splitted[1]
    return args_dict