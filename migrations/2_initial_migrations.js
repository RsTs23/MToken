//const builtin = artifacts.require("./contracts/builtin.sol");
const MToken = artifacts.require("MToken");

module.exports = function (deployer) {
    //deployer.deploy(builtin).then(() => {
    deployer.deploy(MToken, "0x17ACC76e4685AEA9d574705163E871b83e36697f");
};
