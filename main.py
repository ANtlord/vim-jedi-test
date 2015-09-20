#!/usr/bin/python2
# -*- coding: utf-8 -*-
from .base import BaseProgram


class Program(BaseProgram):
    def __init__(self):
        pass

    def start(self):
        # self.| here jedi suggest cases of methods from parent classes.
        pass

    #def sto| here it doesn't suggest method `stop` from BaseProgram

if __name__ == '__main__':
    program = Program()
