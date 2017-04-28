#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/28 PM10:48
# @Author  : Shiloh Leung
# @Site    : 
# @File    : LexerAssignment.py
# @Software: PyCharm Community Edition

import Lexer.LexerBag as LexerBag
from Lexer.const import const

pName = 'test_program.txt'

# make, open *.dyd and *.err file with the same name of program file
dydOut = LexerBag.dydMakeOpen(pName)
errOut = LexerBag.errMakeOpen(pName)

# read in all codes in program file
program = LexerBag.ReadProgramIn(pName)
lineCount = 0


for line in program:
    lineCount = lineCount + 1
    LexerBag.Analysis(line, lineCount, dydOut, errOut)

# end of file
LexerBag.TuplePrinter('eof', const.ENDFILE, dydOut)

# close all of files
LexerBag.CloseAll(dydOut, errOut)
print("\n\n\n～～夸我啊～～")
print("╮(￣▽￣'')╭")





