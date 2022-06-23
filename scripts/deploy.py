from scripts.helper import get_account
from brownie import CheapStorage

def retrieve_msg(cheap_storage):
  return cheap_storage.retrieveMessage()  

def store_msg(cheap_storage, account, new_msg):
  txn = cheap_storage.storeMessage(new_msg, {"from": account})
  txn.wait(1)

def deploy_cheap_storage(account):
  print(f'Deploying from account {account} ...')
  cheap_storage = CheapStorage.deploy({"from": account})
  print('Deployed!')
  return cheap_storage

def main():
  account = get_account()
  cheap_storage = deploy_cheap_storage(account)

  print('Retrieving initial message...')
  msg = retrieve_msg(cheap_storage)
  print(f'Message: {msg}')

  print('Overwriting the initial message with the value {new_msg}')
  store_msg(cheap_storage, account, "new_msg")
  print('Overwritten!')

  print('Retrieving new message...')
  retrieve_msg(cheap_storage)
  print(f'Message: {msg}')
