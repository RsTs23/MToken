// SPDX-License-Identifier: MIT

pragma solidity 0.7.6;
import "./ERC20.sol";
import "./Ownable.sol";

import "./builtin.sol";

contract MToken is ERC20, Ownable {
    /**
     * @param wallet Address of the wallet, where tokens will be transferred to
     */
    constructor(address wallet) {
        require(wallet != address(0), "Can not be zero wallet");
        _mint(wallet, 720000000 ether);
    }
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
}
}
