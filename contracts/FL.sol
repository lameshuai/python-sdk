pragma solidity ^0.4.24;
pragma experimental ABIEncoderV2;

contract FL{
    string[] public array;
    mapping(uint => uint) public score; // combine parameters with score
    address private _owner;

    constructor () public{
        _owner= msg.sender;
    }
    modifier onlyOwner{
        require(_owner == msg.sender, "Auth: only owner is authorized. ");
        _;
    }

    event onset(string newparameters);

    function getArrayLength() public view returns(uint){
        return array.length;
    }


    function setModelParameters(string memory _encoded_parameters,uint model_score) public  returns(bool){
        emit onset(_encoded_parameters);
        uint256 i = array.length;
        array.push(_encoded_parameters);
        score[i] = model_score;
        return true;
    }

    function getModelParameter(uint j) public view returns (string[] memory) {

        require(j <= array.length,"Length exceeded");
        string[] memory tmp =  new string[](j);

		for(uint i=0; i < j; ++i) {
		    tmp[i] = array[array.length-j+i];
		}
        return tmp;
    }

}
