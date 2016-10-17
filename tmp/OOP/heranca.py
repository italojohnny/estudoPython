#!/usr/python3.5
#-------------------------------------------------------------------------------
class BaseClass: #HERANÇA MULTIPLA
    num_base_calls = 0
    def call_me (self):
        print('Calling method on Base Class')
        self.num_base_calls += 1

class LeftSubclass (BaseClass):
    num_left_calls = 0
    def call_me (self):
        super().call_me()
        print('calling method on left subclass')
        self.num_left_calls += 1

class RightSubclass (BaseClass):
    num_right_calls = 0
    def call_me (self):
        super().call_me()
        print('calling method on right subclass')
        self.num_right_calls += 1

class Subclass (LeftSubclass, RightSubclass):
    num_sub_calls = 0
    def call_me (self):
        super().call_me()
        print('calling method on subclass')
        self.num_sub_calls += 1
s = Subclass()
s.call_me()
print(s.num_sub_calls, s.num_left_calls, s.num_right_calls, s.num_base_calls)

#-------------------------------------------------------------------------------
class A: #HERANÇA MULTIPLA
    var_a = 'a'
    def method_a (self):
        print('method a')
class B:
    var_b = 'b'
    def method_b (self):
        print('method b')
class C (A,B):
    var_c = 'c'
    def method_c (self):
        print('method c')

c = C()
c.method_a()
c.method_b()
c.method_c()
print(c.var_a, c.var_b, c.var_c)
#-------------------------------------------------------------------------------

