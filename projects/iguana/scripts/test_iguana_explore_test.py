#!/usr/bin/python3
import brownie
from brownie import Iguana, accounts, config
from .utils_test import split_args
import functools

def retrieve_logs(c_address, account, contract):
    lgs = brownie.web3.eth.filter({'fromBlock': 0, 'toBlock': 'latest', 'address': c_address})
    # print(list(map(lambda x: x['topics'], lgs.get_all_entries())) )
    # brownie.web3.eth.
    print(lgs.get_all_entries())

    
    

def main(*args):    
    params = split_args(args)    
    contract_address = params['contract']
    if 'accountId' in params.keys():      
        account_id = params['accountId']  
        acct = accounts.load(account_id)
    else:
        acct = accounts.add(config["wallets"]["from_key"])
    iguana = Iguana.at(contract_address)            
    print('Analyzing transaction logs..')
    logs = retrieve_logs(contract_address, acct, iguana)
    
    