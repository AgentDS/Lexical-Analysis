#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/28 PM8:53
# @Author  : Shiloh Leung
# @Site    : 
# @File    : const.py
# @Software: PyCharm Community Edition


class _const:
  class ConstError(TypeError): pass
  class ConstCaseError(ConstError): pass

  def __setattr__(self, name, value):
      if name in self.__dict__:
          raise self.ConstError("can't change const %s" % name)
      if not name.isupper():
          raise self.ConstCaseError('const name "%s" is not all uppercase' % name)
      self.__dict__[name] = value

const = _const()

# define type with integers
const.BEGIN = 1
const.END = 2
const.INTEGER = 3
const.IF = 4
const.THEN = 5
const.ELSE = 6
const.FUNCTION = 7
const.READ = 8
const.WRITE = 9
const.SYMBOL = 10
const.CONSTANT = 11
const.E = 12    # =
const.NE = 13    # <>
const.LE = 14    # <=
const.L = 15    # <
const.GE = 16    # >=
const.G = 17    # >
const.SUB = 18    # -
const.MUL = 19    # *
const.ASSIGN = 20    # :=
const.LPAR = 21    # (
const.RPAR = 22    # )
const.SEM = 23    # ;
const.ENDLINE = 24
const.ENDFILE = 25

