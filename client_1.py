import configparser
import json

import numpy as np

from client.bcosclient import (
    BcosClient,
)
from client.datatype_parser import (
    DatatypeParser,
)
from client_config1 import (
    client1,
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
client1 = BcosClient(client_config_instance=client1)

# 要发送给合约的数据
array = np.arange(9).reshape((3, 3))
encoded = json.dumps(array.tolist())

# 发送交易
args = [encoded, 80]
receipt = client1.sendRawTransactionGetReceipt(
    to_address, contract_abi, "setModelParameters", args
)
print("receipt:", receipt)

# 断开连接
client1.finish()