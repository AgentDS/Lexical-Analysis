#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/28 PM8:40
# @Author  : 梁司其
# @Site    : 
# @File    : LexerBag.py
# @Software: PyCharm Community Edition

from Lexer.const import const




def ReadProgramIn(fname):
    fr = open(fname)
    strArray = [line for line in fr.readlines()]
    return strArray


# make and open *.dyd file with the same name of program file
def dydMakeOpen(pName):
    dydName = '.'.join(pName.split('.')[0:-1]) + '.dyd'
    dydOut = open(dydName, 'w')
    return  dydOut


# make and open *.err file with the same name of program file
def errMakeOpen(pName):
    errName = '.'.join(pName.split('.')[0:-1]) + '.err'
    errOut = open(errName, 'w')
    return  errOut


def CloseAll(dydOut, errOut):
    dydOut.close()
    errOut.close()


# find, return TypeId if singleWord is reserved word or variable name
def FindTypeId(singleWord):
    if singleWord == 'begin':
        TypeId = const.BEGIN
    elif singleWord == 'end':
        TypeId = const.END
    elif singleWord == 'integer':
        TypeId = const.INTEGER
    elif singleWord == 'if':
        TypeId = const.IF
    elif singleWord == 'then':
        TypeId = const.THEN
    elif singleWord == 'else':
        TypeId = const.ELSE
    elif singleWord == 'function':
        TypeId = const.FUNCTION
    elif singleWord == 'read':
        TypeId = const.READ
    elif singleWord == 'write':
        TypeId = const.WRITE
    else:
        TypeId = const.SYMBOL

    return TypeId


def TuplePrinter(word, TypeId, dydOut):
    print((16 - len(word)) * ' ' + word + ' ', file=dydOut, end='')
    print("%2d\n" % (TypeId), file=dydOut, end='')


def ErrPrinter(lineCount, errMessage, errOut):
    print('***LINE:', file=errOut, end='')
    print("%3d  " % (lineCount), file=errOut, end='')
    print(errMessage, file=errOut)


def Analysis(line, lineCount, dydOut, errOut):
    #print(line, file=dydOut, end='')
    wordList = line.strip().split()

    for word in wordList:
        wordLength = len(word)
        First = 0
        Second = 0
        while First < wordLength:
            if word[First].isalpha():
                Second = Second + 1
                while (Second < wordLength and (word[Second].isalpha() or word[Second].isdigit())) :
                    Second = Second + 1
                singleWord = word[First:Second]
                TypeId = FindTypeId(singleWord)
                TuplePrinter(singleWord, TypeId, dydOut)
                First = Second

            elif word[First].isdigit():
                Second = Second + 1
                while Second < wordLength and word[Second].isdigit():
                    Second = Second + 1
                constant = word[First:Second]
                TypeId = const.CONSTANT
                TuplePrinter(constant, TypeId, dydOut)
                First = Second

            elif word[First] == '(':
                TypeId = const.LPAR
                singleWord = '('
                TuplePrinter(singleWord, TypeId, dydOut)
                First = First + 1
                Second = Second + 1

            elif word[First] == ')':
                TypeId = const.RPAR
                singleWord = ')'
                TuplePrinter(singleWord, TypeId, dydOut)
                First = First + 1
                Second = Second + 1

            elif word[First] == '*':
                TypeId = const.MUL
                singleWord = '*'
                TuplePrinter(singleWord, TypeId, dydOut)
                First = First + 1
                Second = Second + 1

            elif word[First] == '-':
                TypeId = const.SUB
                singleWord = '-'
                TuplePrinter(singleWord, TypeId, dydOut)
                First = First + 1
                Second = Second + 1

            elif word[First] == ';':
                TypeId = const.SEM
                singleWord = ';'
                TuplePrinter(singleWord, TypeId, dydOut)
                First = First + 1
                Second = Second + 1

            elif word[First] == '<':
                Second = Second + 1
                if word[Second] == '=':
                    singleWord = '<='
                    TypeId = const.LE
                    TuplePrinter(singleWord, TypeId, dydOut)
                    Second = Second + 1
                    First = Second
                    break
                elif word[Second] == '>':
                    singleWord = '<>'
                    TypeId = const.NE
                    TuplePrinter(singleWord, TypeId, dydOut)
                    Second = Second + 1
                    First = Second

                else:
                    singleWord = '<'
                    TypeId = const.L
                    TuplePrinter(singleWord, TypeId, dydOut)
                    First = Second

            elif word[First] == '>':
                Second = Second + 1
                if word[Second] == '=':
                    singleWord = '>='
                    TypeId = const.GE
                    TuplePrinter(singleWord, TypeId, dydOut)
                    Second = Second + 1
                    First = Second

                else:
                    singleWord = '>'
                    TypeId = const.G
                    TuplePrinter(singleWord, TypeId, dydOut)
                    First = Second

            elif word[First] == ':':
                Second = Second + 1
                if word[Second] == '=':
                    singleWord = ':='
                    TypeId = const.ASSIGN
                    TuplePrinter(singleWord, TypeId, dydOut)
                    Second = Second + 1
                    First = Second

                else:
                    ErrPrinter(lineCount, "词法错误, 赋值语句只能使用':='", errOut)
                    First = First + 1
                    Second = Second +1

            else:
                ErrPrinter(lineCount, "词法错误, 不支持当前字符 '" + word[First] + "'", errOut)
                First = First + 1
                Second = Second + 1


    # end of line
    TuplePrinter('eoln', const.ENDLINE, dydOut)







