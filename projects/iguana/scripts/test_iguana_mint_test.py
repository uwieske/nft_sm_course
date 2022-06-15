#!/usr/bin/python3
import brownie
from brownie import  Contract, Iguana, accounts, config
from brownie.project import build, IguanaProject
from .utils_test import split_args


def main(*args):    
    params = split_args(args)    
    contract_address = params['contract']
    tokenURI = params['tokenURI']        
    if 'accountId' in params.keys():      
        account_id = params['accountId']  
        acct = accounts.load(account_id)
    else:
        acct = accounts.add(config["wallets"]["from_key"])
    iguana = Iguana.at(contract_address)        
    print(iguana.name())
    tx = iguana.mint(tokenURI,{'from': acct})
    tx.wait(1)
    receipt =brownie.web3.eth.getTransactionReceipt(tx.txid)
    print(tx.info())
    print(type(tx))
    
    # read emitted events from operation
    logs_IGUANA_MINTED = iguana.events.IGUANA_MINTED().processReceipt(receipt)
    logs_Transfer = iguana.events.Transfer().processReceipt(receipt)

    ## get first event occurrence
    print(logs_IGUANA_MINTED[0]['args']['tokenId'])
    print(logs_Transfer[0]['args']['to'])
    
