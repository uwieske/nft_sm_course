//SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.7;
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import '@openzeppelin/contracts/utils/Counters.sol';
import "@openzeppelin/contracts/access/Ownable.sol";


contract Iguana is ERC721, Ownable {
    // only for dev purposes! do not do this. poor coding. test net OpenSea address on Mumbai
    address constant openSeaProxyAddress = 0x58807baD0B376efc12F5AD86aAc70E78ed67deaE;
    uint256 public tokenCounter;
    mapping (uint256 => string) private _tokenURIs;

    event IGUANA_MINTED(uint256 indexed tokenId, address indexed owner);
    
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {
        tokenCounter = 0;
    }

    function mint(string memory _tokenURI) public {
        require(
            keccak256(abi.encodePacked(_tokenURI)) != keccak256(abi.encodePacked("")),
            "ERC721Metadata: URI not defined"
        );  // Checks if the tokenId exists        
        _safeMint(msg.sender, tokenCounter);
        _setTokenURI(tokenCounter, _tokenURI);
        emit IGUANA_MINTED(tokenCounter, msg.sender);
        tokenCounter++;        
    }

    function tokenURI(uint256 _tokenId) public view virtual override returns(string memory) {
        require(
            _exists(_tokenId),
            "ERC721Metadata: URI set of nonexistent token"
        );
        return _tokenURIs[_tokenId];
    }


    // Open Sea spefific Override isApprovedForAll to auto-approve OS's proxy contract
    function isApprovedForAll(
        address _owner,
        address _operator
    ) public override view returns (bool isOperator) {
        // if OpenSea's ERC721 Proxy Address is detected, auto-return true
        if (_operator == address(openSeaProxyAddress)) {
            return true;
        }

        // otherwise, use the default ERC721.isApprovedForAll()
        return  ERC721.isApprovedForAll(_owner, _operator);
    }

    function _setTokenURI(uint256 _tokenId, string memory _tokenURI) internal virtual {        
    require(
        _exists(_tokenId),
        "ERC721Metadata: URI set of nonexistent token"
    );  // Checks if the tokenId exists
    _tokenURIs[_tokenId] = _tokenURI;
    }
}
