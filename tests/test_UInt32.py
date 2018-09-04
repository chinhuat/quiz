#!/usr/bin/env pytest

# DO NOT MODIFY

from data_types import UInt32

UINT32_MAX = (1 << 32) - 1

def test_UInt32_constructor():

    # default value should be 0
    assert (int(UInt32()) == 0)

    # initialize with arbitrary integer value
    assert (int(UInt32(1 << 16)) == (1 << 16))
        
    # initialize with arbitrary values that can be casted to integer 
    assert (int(UInt32(UInt32(1 << 16))) == (1 << 16))

    # boundary value test
    assert (int(UInt32(UINT32_MAX + 1)) == 0)
 

def test_UInt32_add_int():

    # add an arbitrary integer value
    assert (int(UInt32(1) + 1) == 2) 

    # boundary value test
    assert (int(UInt32(UINT32_MAX) + 1) == 0) 


def test_int_add_UInt32():

    # add to an arbitrary integer value
    assert (1 + int(UInt32(1)) == 2)


def test_UInt32_add_UInt32():
    
    # add an arbitrary UInt32
    assert (int(UInt32(1) + UInt32(1)) == 2) 

    # boundary value test
    assert (int(UInt32(UINT32_MAX) + UInt32(1)) == 0)

