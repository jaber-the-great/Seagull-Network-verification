#!/usr/bin/env python
# coding: utf-8

# In[78]:


'''
Purpose: Equality check on SharedScalars for TinySMPC
Input: x_sh: SharedScalar with 2 owners, pub: public integer
Output: PrivateScalar
Name: Sucheer Maddury, Leland High School, CA
@UCSB RMP '23
'''

from tinysmpc.tinysmpc.tinysmpc import VirtualMachine, PrivateScalar, SharedScalar
from tinysmpc.tinysmpc.finite_ring import MIN_INT64
from tinysmpc.tinysmpc.secret_sharing import Share
from random import random, randint, shuffle
from tinysmpc.tinysmpc.shared_comparison import greater_than, _private_compare, _share_bitwise, _get_bits, _randlist, _fixed_shuffle


# In[90]:


def equal_to(x_sh, pub):
    assert len(x_sh.owners) == 2
    tmp_vm = VirtualMachine('tmp_vm')
    x = x_sh.reconstruct(tmp_vm).value
    if pub < 0 or x < 0: pub += -MIN_INT64; x += -MIN_INT64
    
    x_sh1 = _share_bitwise(x, list(x_sh.owners))
    x_sh2 = _share_bitwise(pub, list(x_sh.owners))
    
    r1 = _private_compare(x_sh1, pub).value
    r2 = _private_compare(x_sh2, x).value
    
    return ((not r1) and (not r2))
    

