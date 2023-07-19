#!/usr/bin/env python
# coding: utf-8

# In[4]:


from tinysmpc.tinysmpc.tinysmpc import VirtualMachine, PrivateScalar, SharedScalar
from tinysmpc.tinysmpc.finite_ring import MIN_INT64
from tinysmpc.tinysmpc.secret_sharing import Share
from random import random, randint, shuffle


# In[26]:


# x: PrivateScalar, y: PrivateScalar, l: list of parties (VMs)
def beaver_multiply(x, y, l):
    # Create a temporary VM
    tmp_vm = VirtualMachine('tmp_vm')
    
    # Generate triples
    s_a = PrivateScalar(randint(0, 2**32), tmp_vm).share(l)
    s_b = PrivateScalar(randint(0, 2**32), tmp_vm).share(l)
    s_c = PrivateScalar((s_a*s_b).reconstruct(tmp_vm).value, tmp_vm).share(l)
    
    # Share x and y shares
    s_x = x.share(l)
    s_y = y.share(l)
    
    # Calculate d and e
    s_d = s_x-s_a
    s_e = s_y-s_b
    
    d=s_d.reconstruct(tmp_vm).value
    e=s_e.reconstruct(tmp_vm).value
    
    s_z = d*e + d*s_b + e*s_a + s_c
    return s_z.reconstruct(tmp_vm)

