from distutils.command.build import build
from thor_requests.connect import Connect
from thor_requests.wallet import Wallet
from thor_requests.contract import Contract


# Import wallets from mnemonic (this should be only one, but for know we need 2 for testing)
def wallet_import_mnemonic():
    #--EDIT--
    mnemonic_1 = "word1, word2,...word12"
    _wallet = Wallet.fromMnemonic(mnemonic_1.split(', '))
    _wallet_address = _wallet.getAddress()
    return _wallet, _wallet_address

#
# Connect to Veblocks and import the DHN contract
#
def connect(network_choice):

    if network_choice == 1:
        #Testnet node
        print("Connected to Veblocks Testnet Node\n")
        connector = Connect("http://3.71.71.72:8669")

    elif network_choice == 2:
        #Mainnet node
        print("Connected to Veblocks Mainnet Node")
        connector = Connect("http://3.124.193.149:8669")

    else:
        print("You must choose between 1 (Testnet) or 2 (Mainnet).")
    
    return connector

#
#Transfer tokens
#
def transfer_token(_wallet, _receiver_address, amount):

        #Connect to testnet node
        connector = connect(1)

        #Import wallet
        (_wallet, main_wallet_address) = wallet_import_mnemonic()

        #Get contract build and address --EDIT--
        _contract_Token = Contract.fromFile("/build/contracts/MToken.json")
        Token_contract_address="0xa98Ce4051A0d1cb1c0025b13DaB371239fD0C257"

        #transfers tokens to the _wallet_address
        transf_Token = connector.transact(
            _wallet,
            contract=_contract_Token,
            func_name="transfer",
            func_params=[_receiver_address, amount],
            to=Token_contract_address,
        )
        