from brownie import CheapStorage, accounts

def test_deploy():
  account = accounts[0]
  cheap_storage = CheapStorage.deploy({"from": account})
  assert cheap_storage.retrieveMessage() == "init_msg"

def test_update_storage():
  account = accounts[0]
  cheap_storage = CheapStorage.deploy({"from": account})
  new_msg = "new_msg"
  txn = cheap_storage.storeMessage(new_msg, {"from": account})
  txn.wait(1)
  assert cheap_storage.retrieveMessage() == new_msg
