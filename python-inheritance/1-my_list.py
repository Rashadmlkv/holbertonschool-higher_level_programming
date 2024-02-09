#!/usr/bin/python3
''' a class MyList that inherits from list: '''


class MyList(list):
    ''' def print_sorted(self):prints sorted list '''
    def print_sorted(self):
        copylist = self[:]
        copylist.sort()
        print(copylist)
