# hashcash
intento resumir aquí tot el que estic entenent de com funciona la tecnologia blockchain. I si pogués, afegir algun exemple també.

# What is hashcash for the real world?
The Hashcash algorithm is a proof-of-work system. It was invented by Adam Back in 1997 and is still used today in various applications.

## Why do we use it for?
In order to prevent *email spam* and *denial-of-service attacks* by requiring computational work from the sender

# The *hashcash* algorithm

## General idea
This work is done by generating a cryptographic hash of the message or request, and then adding a string of random data to the hash until a certain condition is met.

## Details

### Leading number of zeroes
The condition that must be met is that the resulting hash must have a certain number of leading zeros. This number is determined by the system administrator and is designed to make the computational work required to find a valid hash difficult enough to deter spammers and attackers, but not so difficult that legitimate users are significantly impacted.


### The recepient verifies the hash

Once a valid hash is found, it is included in the header of the email or request, along with the random string of data that was added to the original message. The recipient of the email or request can then verify that the hash was generated correctly by repeating the same computational work and checking that the resulting hash matches the one included in the header.

### What is a *hash* function?

Hash functions are mathematical functions that transform or "map" a given set of data into a bit string of fixed size.