#!/usr/bin/env pytest

# DO NOT MODIFY

from data_types import UInt16

UINT16_MAX = (1 << 16) - 1

def test_UInt16_constructor():

    # default value should be 0
    assert (int(UInt16()) == 0)

    # initialize with arbitrary integer value
    assert (int(UInt16(1 << 8)) == (1 << 8))
        
    # initialize with arbitrary values that can be casted to integer 
    assert (int(UInt16(UInt16(1 << 8))) == (1 << 8))

    # boundary value test
    assert (int(UInt16(UINT16_MAX + 1)) == 0)
 

def test_UInt16_add_int():

    # add an arbitrary integer value
    assert (int(UInt16(1) + 1) == 2) 

    # boundary value test
    assert (int(UInt16(UINT16_MAX) + 1) == 0) 


def test_int_add_UInt16():

    # add to an arbitrary integer value
    assert (1 + int(UInt16(1)) == 2)


def test_UInt16_add_UInt16():
    
    # add an arbitrary UInt16
    assert (int(UInt16(1) + UInt16(1)) == 2) 

    # boundary value test
    assert (int(UInt16(UINT16_MAX) + UInt16(1)) == 0)

