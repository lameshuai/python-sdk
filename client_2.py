import configparser
import json

import numpy as np

from client.bcosclient import (
    BcosClient,
)
from client.datatype_parser import (
    DatatypeParser,
)
from client_config2 import (
    client2,
)

# 从文件加载abi定义
abi_file = "contracts/FL.abi"
data_parser = DatatypeParser()
data_parser.load_abi_file(abi_file)
contract_abi = data_parser.contract_abi

# 加载合约地址
config = configparser.ConfigParser() # 类实例化
contract_ini_path  = "bin/contract.ini"
config.read(contract_ini_path)
to_address = config['address.bcos2-1']['FL']

# 实例化客户端
client2 = BcosClient(client_config_instance=client2)

# 要发送给合约的数据
array = np.arange(9,18).reshape((3, 3))
encoded = json.dumps(array.tolist())

# 发送交易
args = [encoded, 80]
receipt = client2.sendRawTransactionGetReceipt(
    to_address, contract_abi, "setModelParameters", args
)
print("receipt:", receipt)

# 断开连接
client2.finish()