// SPDX-License-Identifier: MIT
pragma solidity ^0.8.12;

contract Kadushi {
    
    int8 public numMolecules = 0;

    address public nonPayableAddress;
    address payable public payableAddress;

    string scientificName = "Cereus repandus";

    struct KadushiPilar {
        uint32 height;
        uint8 diameter;
    }

    KadushiPilar[] public hedge;

    event ETHER_RECEIVED(address from, uint amount);

    constructor() {
    }

    /**

     */
    function clash(int8 a, int8 b) external {
        numMolecules = a + b;
    }

    function setNonPayablePerson(address person)  external {
        nonPayableAddress = person;
    }

    function setPayablePerson(address payable person) external{
        payableAddress = person;
    }
    /**
    Attempt to send 10 wei to a non-payable person.
    Will fail.
     */
    function payOutNonPayablePerson10() external payable {
        // if you comment out the line below, put revert(..) in comment and compile again, then you would get a compile error.
        // nonPayableAddress is declared as an address and not as a payable address.
        // So, nonPayableAddres won't be provided with the transfer funtion by the compiler.        
        //nonPayableAddress.transfer(10);
        revert('Not possible to pay out a non payable person.');        
    }
    
    /**
    Attempt to send 10 wei to a payable person.
    Will succeed (assuming contract has enough funds).
     */
    function payOutPayablePerson10() external payable {
        payableAddress.transfer(10);
    }

    /**
    Must be implemented if this contract wants to receive ether, otherwise transfers to this contract will fail.
     */
    receive() external payable {
        emit ETHER_RECEIVED(msg.sender, msg.value);
    }

    function createHedge() external {
        // hedge = new KadushiPilar[]();
    }

    function addPilar(KadushiPilar calldata pilar) external {        
        // KadushiPilar memory newPilar = pilar;
        hedge.push(pilar);
    }

}