"""
algorithms concerning the SHA algorithm and its uses
"""

import hashlib as hl
from struct import *

# let's encode a number into binary
payload1 = pack("H", 65028)
payload2 = pack("H", 65029)

# now let's hash it to see what we obtain:
hash1 = hl.sha1(payload1).hexdigest()
hash2 = hl.sha1(payload2).hexdigest()

# and now let's compare both results:
text1 = bytes("hola em dic gregory, tu com et dius?",'utf-8')
text2 = bytes("hola em dic gregory, tu com et djus?",'utf-8')
hash3 = hl.sha1(text1).hexdigest()
hash4 = hl.sha1(text2).hexdigest()
hash5 = hl.sha1(text2).hexdigest()