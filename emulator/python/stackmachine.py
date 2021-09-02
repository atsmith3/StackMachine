#!/usr/bin/python3

import sys
import os
import argparse

class StackMachine:
  def __init__(self,STACK_SIZE=1024):
    self.STACK_SIZE = STACK_SIZE

    self.pc = 0
    self.ir_imm = 0
    self.ir_optype = 0
    self.ir_opcode = 0
    self.ir_nzp = 0
    self.sp = 0
    self.stack = [0]*STACK_SIZE
    self.acum = 0
    self.gsr = {'N':0,'Z':0,'P':0}

  def clock(self):
    # TODO: Consume instruction and dispatch op
    pass

  def print_state(self):
    print("{:<20}: {}".format("pc",self.pc))
    print("{:<20}: {}".format("ir_imm",self.ir_imm))
    print("{:<20}: {}".format("ir_optype",self.ir_optype))
    print("{:<20}: {}".format("ir_opcode",self.ir_opcode))
    print("{:<20}: {}".format("ir_nzp",self.ir_nzp))
    print("{:<20}: {}".format("sp",self.sp))
    print("{:<20}: {}".format("acum",self.acum))
    print("{:<20}: {}".format("gsr",self.gsr))
    print("{:<20}: {}".format("stack",self.stack))
    print("")

  ## push
  #  Helper function to move the s[sp] -> acum
  def pop(self):
    self.sp_decr()
    self.acum = self.stack[self.sp]
    self.stack[self.sp] = 0

  ## push
  #  Helper function to move the accumulator into the stack
  def push(self):
    self.stack[self.sp] = self.acum
    self.sp_incr()

  def sp_decr(self):
    self.sp = max(0, self.sp-1)

  def sp_incr(self):
    self.sp = min(self.STACK_SIZE-1, self.sp+1)

  def set_gsr(self):
    if self.acum == 0:
      self.gsr["N"] = 0
      self.gsr["Z"] = 1
      self.gsr["P"] = 0
    elif self.acum > 0:
      self.gsr["N"] = 0
      self.gsr["Z"] = 0
      self.gsr["P"] = 1
    else:
      self.gsr["N"] = 1
      self.gsr["Z"] = 0
      self.gsr["P"] = 0

  def add(self):
    self.pop()
    self.sp_decr()
    self.acum += self.stack[self.sp]
    self.set_gsr()
    self.push()
    #self.stack[self.sp] = self.acum

  def addi(self):
    self.pop()
    self.acum += self.ir_imm
    self.set_gsr()
    self.push()
    #self.stack[self.sp] = self.acum

  def sub(self):
    self.pop()
    self.acum -= self.stack[self.sp]
    self.set_gsr()
    self.stack[self.sp] = self.acum

  def subi(self):
    self.pop()
    self.acum -= self.ir_imm
    self.set_gsr()
    self.stack[self.sp] = self.acum

  def br(self):
    # TODO: Implement the Branch op
    pass


  def bri(self):
    # TODO: Implement the Branch Immediate op
    pass

def unit_test(tests):
  m = StackMachine(8)

  # Unit Test ADD:
  if "ADD" in tests:
    m.acum = 10
    m.push()
    m.acum = 15
    m.push()
    m.add()
    m.print_state()

    #for i in range(10):
    #  m.acum = i
    #  m.push()
    #m.print_state()

    #for i in range(10):
    #  m.pop()
    #m.print_state()

  # Unit Test ADDI:
  m = StackMachine(8)
  if "ADDI" in tests:
    m.ir_imm = 10
    m.acum = 10
    m.push()
    m.addi()
    m.print_state()

    m.ir_imm = -300
    m.addi()
    m.print_state()

    m.ir_imm = 126749236
    m.addi()
    m.print_state()

if __name__ == "__main__":
  tests = [
    "ADD",
    "ADDI",
    "SUB",
    "SUBI",
    "BR",
    "BRI"
  ]
  unit_test(tests)


