#!/usr/bin/python3

from brownie import Iguana, accounts


def main():            
    print("Deploying Iguana contract! .....")    
    acct = accounts.load('kadushi_deployer')    
    iguana  = Iguana.deploy("IGUANA_NFT", "IGUANA",{'from': acct})
    print(iguana.name())   
    return iguana
