from client.contractnote import ContractNote
from client.bcosclient import BcosClient
from client.datatype_parser import DatatypeParser
from client_config import client_config
from client.datatype_parser import DatatypeParser
from client.common.compiler import Compiler
import os

demo_config = client_config
if os.path.isfile(demo_config.solc_path) or os.path.isfile(demo_config.solcjs_path):
    Compiler.compile_file("contracts/FL.sol")
# 从文件加载abi定义
abi_file = "contracts/FL.abi"
data_parser = DatatypeParser()
data_parser.load_abi_file(abi_file)
contract_abi = data_parser.contract_abi

# 部署合约
# print("\n>>Deploy:----------------------------------------------------------")
with open("contracts/FL.bin", 'r') as load_f:
    contract_bin = load_f.read()
    load_f.close()

# 实例化客户端
client = BcosClient()
result = client.deploy(contract_bin)

print("deploy", result)
print("new address : ", result["contractAddress"])

# 把部署结果存入文件备查
to_address = result["contractAddress"]
contract_name = os.path.splitext(os.path.basename(abi_file))[0]  #basename return FL.abi ----- splitext returns ['FL','abi']
ContractNote.save_address_to_contract_note("bcos2-1",contract_name,to_address)

# 断开连接
client.finish()