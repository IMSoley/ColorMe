#!/usr/bin/env python3
# Author: Soleyman
# Title: ColorMe python3 colored output


import ctypes
import platform

if platform.system() == 'Windows':
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


color = {
    'fg': {
        'black': '30',
        'red': '31',
        'green': '32',
        'yellow': '33',
        'blue': '34',
        'purple': '35',
        'cyan': '36',
        'white': '37',
        'reset': '0'
    },
    'bg': {
        'black': '40',
        'red': '41',
        'green': '42',
        'yellow': '43',
        'blue': '44',
        'purple': '45',
        'cyan': '46',
        'white': '47',
        'reset': '0'
    },
    'lab': {
        'warning': '31;1m[-]',
        'info': '33;1m[!]',
        'success': '32;1m[+]',
        'question': '34;1m[?]',
        'running': '97;1m[~]'
    },
    'dec': {
        'bold': '1m',
        'underline': '4m',
        'reversed': '7m',
        'reset': '0m'
    }
}

color_func_key = (
    'black', 'red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'white')

label_func_key = ('warning', 'info', 'success', 'question', 'running')


class ColorMe:
    pass


def item_iterate(temp):
    data = []
    for i in temp:
        i = i.strip().lower()
        data.append(i)
    return data


def make_method(name):

    def _method(self, string, color_name=name, **kwargs):

        if name in label_func_key:
            return u"\u001b[{}\u001b[0m".format(color['lab'][color_name]) + string

        elif name in color_func_key:
            dec = kwargs.get('dec', None)
            bg = kwargs.get('bg', None)
            args = ['dec', 'bg']

            if bool(kwargs):
                if len(kwargs) == 2:
                    dec_list = kwargs[args[0]].split(',')
                    bg_col_name = kwargs[args[1]]

                    if len(dec_list) == 2:
                        temp = item_iterate(dec_list)
                        return u"\u001b[{}\u001b[{}\u001b[{}m\u001b[{}m".format(color['dec'][temp[0]], color['dec'][temp[1]], color['bg'][bg_col_name], color['fg'][color_name]) + string + "\u001b[0m"
                    elif len(dec_list) == 3:
                        temp = item_iterate(dec_list)
                        return u"\u001b[{}\u001b[{}\u001b[{}\u001b[{}m\u001b[{}m".format(color['dec'][temp[0]], color['dec'][temp[1]], color['dec'][temp[2]], color['bg'][bg_col_name], color['fg'][color_name]) + string + "\u001b[0m"
                    else:
                        i = dec_list[0].lower()
                        return u"\u001b[{}\u001b[{}m\u001b[{}m".format(color['dec'][i], color['bg'][bg_col_name], color['fg'][color_name]) + string + "\u001b[0m"

                elif len(kwargs) == 1:
                    try:
                        key1 = kwargs['bg'].lower()
                        return u"\u001b[{}m\u001b[{}m".format(color['bg'][key1], color['fg'][color_name]) + string + "\u001b[0m"
                    except KeyError:
                        key1 = None

                    try:
                        key2 = kwargs['dec']
                        key2 = key2.split(',')

                        if len(key2) == 2:
                            temp = item_iterate(key2)
                            return u"\u001b[{}\u001b[{}\u001b[{}m".format(color['dec'][temp[0]], color['dec'][temp[1]], color['fg'][color_name]) + string + "\u001b[0m"
                        elif len(key2) == 3:
                            temp = item_iterate(key2)
                            return u"\u001b[{}\u001b[{}\u001b[{}\u001b[{}m".format(color['dec'][temp[0]], color['dec'][temp[1]], color['dec'][temp[2]], color['fg'][color_name]) + string + "\u001b[0m"
                        else:
                            i = key2[0].lower()
                            return u"\u001b[{}\u001b[{}m".format(color['dec'][i], color['fg'][color_name]) + string + "\u001b[0m"
                    except KeyError:
                        key2 = None
            else:
                return u"\u001b[{}m".format(color['fg'][color_name]) + string + "\u001b[0m"
    return _method

for name in color_func_key:
    _method = make_method(name)
    setattr(ColorMe, name, _method)

for name in label_func_key:
    _method = make_method(name)
    setattr(ColorMe, name, _method)


ColorMe = ColorMe()
