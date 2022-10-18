import configparser
import json

import numpy as np

from client.bcosclient import (
    BcosClient,
)
from client.datatype_parser import (
    DatatypeParser,
)
from client_config import (
    client_config,
)

# 从文件加载abi定义
abi_file = "contracts/FL.abi"
data_parser = DatatypeParser()
data_parser.load_abi_file(abi_file)
contract_abi = data_parser.contract_abi

# 加载合约地址
config = configparser.ConfigParser()  # 类实例化
contract_ini_path = "bin/contract.ini"
config.read(contract_ini_path)
to_address = config["address.bcos2-1"]["FL"]

# 实例化客户端
client = BcosClient(client_config_instance=client_config)

# 得到数据合约的数据
args =[2]
encoded_parameters  = client.call(to_address, contract_abi, "getModelParameter",args) #return is tuple

decoded_parameters = encoded_parameters[0][0]
decoded_parameters2 = encoded_parameters[0][1]

decoded_parameters = json.loads(decoded_parameters)
decoded_parameters2 = json.loads(decoded_parameters2)

res = np.array(decoded_parameters)
res2 = np.array(decoded_parameters2)

print("res:",res)
print("res2:",res2)

print(type(res))

# 断开连接
client.finish()