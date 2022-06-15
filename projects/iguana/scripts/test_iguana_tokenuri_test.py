#!/usr/bin/python3
import brownie
from brownie import Iguana, accounts, config
from utils_test import split_args

def main(*args):    
    params = split_args(args)
    
    contract_address = params['contract']
    tokenId = int(params['tokenId'])
    if 'accountId' in params.keys():      
        account_id = params['accountId']  
        acct = accounts.load(account_id)
    else:
        acct = accounts.add(config["wallets"]["from_key"])
    iguana = Iguana.at(contract_address)        
    tokenUri = iguana.tokenURI(tokenId)
    print(tokenUri)