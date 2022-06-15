#!/usr/bin/python3

from brownie import Kadushi, accounts
import brownie


def main():        
    print("Deploying Kadushi contract! .....")
    return Kadushi.deploy({'from': accounts[0]})
