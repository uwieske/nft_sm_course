#!/usr/bin/python3
import brownie
from brownie.exceptions import VirtualMachineError
from pytest import fail

def test_num_molecules(accounts, kadushi):    
    assert kadushi.numMolecules() == 0

def test_clash(accounts, kadushi):    
    tx =  kadushi.clash(4,5) 
    assert kadushi.numMolecules() == 9

'''
This test should fail and throw an error because of a data overflow if the Kadushi has been compiled based on a 
version from than 8.x.x.
'''
def test_clash_throw_error_when_overflow_since_compiler_v8(accounts, kadushi):       
    try:
        tx =  kadushi.clash(80,90)
        fail('Should have thrown an data overflow error by the EVM')         
    except VirtualMachineError as e:        
        assert kadushi.numMolecules() == 0
        


'''
This test should fail if you have compiled Kadushi with for version lower than version 8.
Try it out by uncommenting the test below and change the pragma line in Kadushi to ^0.7.0
'''
# def test_clash_throw_error_when_overflow_before_compiler_v8(accounts, kadushi):    
#     tx =  kadushi.clash(80,90) 
#     assert kadushi.numMolecules() == 170


# -------- Types -----------

# ----- Address / Payable
def test_payout_payable_person_will_succeed(accounts, kadushi):
    accounts[4].transfer(accounts[0],100000)
    kadushi.setPayablePerson(accounts[1])
    kadushi.setNonPayablePerson(accounts[2])
    assert kadushi.nonPayableAddress() == accounts[2].address
    assert kadushi.payableAddress() == accounts[1].address
    accounts[0].transfer(kadushi.address,100)
    tx = kadushi.payOutPayablePerson10()
     

# ------ Refefence Types ------
# Currently, reference types comprise structs, arrays and mappings. 
#  If you use a reference type, you always have to explicitly provide the data area where the type is stored: memory (whose lifetime is limited to an external function call), storage (the location where the state variables are stored, where the lifetime is limited to the lifetime of a contract) or calldata (special data location that contains the function arguments).

def test_add_pilar(accounts, kadushi):
    kadushi.addPilar((1,3))
    (h, d) = kadushi.hedge(0)
    assert h == 1
    assert d == 3

# def test_sender_balance_decreases(accounts, token):
#     sender_balance = token.balanceOf(accounts[0])
#     amount = sender_balance // 4

#     token.transfer(accounts[1], amount, {'from': accounts[0]})

#     assert token.balanceOf(accounts[0]) == sender_balance - amount


# def test_receiver_balance_increases(accounts, token):
#     receiver_balance = token.balanceOf(accounts[1])
#     amount = token.balanceOf(accounts[0]) // 4

#     token.transfer(accounts[1], amount, {'from': accounts[0]})

#     assert token.balanceOf(accounts[1]) == receiver_balance + amount


# def test_total_supply_not_affected(accounts, token):
#     total_supply = token.totalSupply()
#     amount = token.balanceOf(accounts[0])

#     token.transfer(accounts[1], amount, {'from': accounts[0]})

#     assert token.totalSupply() == total_supply


# def test_returns_true(accounts, token):
#     amount = token.balanceOf(accounts[0])
#     tx = token.transfer(accounts[1], amount, {'from': accounts[0]})

#     assert tx.return_value is True


# def test_transfer_full_balance(accounts, token):
#     amount = token.balanceOf(accounts[0])
#     receiver_balance = token.balanceOf(accounts[1])

#     token.transfer(accounts[1], amount, {'from': accounts[0]})

#     assert token.balanceOf(accounts[0]) == 0
#     assert token.balanceOf(accounts[1]) == receiver_balance + amount


# def test_transfer_zero_tokens(accounts, token):
#     sender_balance = token.balanceOf(accounts[0])
#     receiver_balance = token.balanceOf(accounts[1])

#     token.transfer(accounts[1], 0, {'from': accounts[0]})

#     assert token.balanceOf(accounts[0]) == sender_balance
#     assert token.balanceOf(accounts[1]) == receiver_balance


# def test_transfer_to_self(accounts, token):
#     sender_balance = token.balanceOf(accounts[0])
#     amount = sender_balance // 4

#     token.transfer(accounts[0], amount, {'from': accounts[0]})

#     assert token.balanceOf(accounts[0]) == sender_balance


# def test_insufficient_balance(accounts, token):
#     balance = token.balanceOf(accounts[0])

#     with brownie.reverts():
#         token.transfer(accounts[1], balance + 1, {'from': accounts[0]})


# def test_transfer_event_fires(accounts, token):
#     amount = token.balanceOf(accounts[0])
#     tx = token.transfer(accounts[1], amount, {'from': accounts[0]})

#     assert len(tx.events) == 1
#     assert tx.events["Transfer"].values() == [accounts[0], accounts[1], amount]
