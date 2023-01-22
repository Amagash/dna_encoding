# DNA ENCODING

This project allows to convert a string into a DNA sequence and vice versa. This is to showcase the possibility of storing digital information inside a string of DNA.

## Conversion algorithm explainations
### 1. Naive encoding
For now, the conversion relies on naive bit encoding meaning :

| DNA | Binary |
| :---: | :---: |
| A | 00 |
| C | 01 |
| G | 10 |
| T | 11 |

Other data compression algorithms exist like the Huffman Code but for this Proof of concept (POC) we will keep it as simple as possible. 

### 2. Find a secret message
The first step is to find the secret message you want to encode in a DNA strand. There are some guidelines to follow:
1. The message should only contains alphanumeric characters and spaces (e.i 0-9 a-z and A-Z), no special characters or punctuation allowed.
2. Although upper-cased letters are accepted, the final message will be retrieved in lower-case meaning that acronyms might be less obvious.

### 3. Formatted message
Once you have your secret message there is a first step of message formatting. It is not possible to directly convert the sentence into binary because the DNA won't be synthesizable. Indeed, when encoding txt into DNA by directly transforming bits to ATCG, we end up with high GC content and repeated patterns. This makes sense because a sentence contains a lot of repeated characters (e.g spaces ' ' or frequent letters like 'e'). It is therefore necessary to add some randomness into the sentence. To bypass this issue, I alternate between lowercase and uppercase of the same letter and sequencially assign a special character to spaces (that is the reason why special characters are not allowed).

The formatted sentence of "This is a secret message" becomes "This IS#a&secrEt§meSsAgE".

Also to make sure we now where the message starts and stops, I encapsulated the message between "START" and "STOP". Therefore the previous sentence "This is a secret message" actually becomes "STARTThis IS#a&secrEt§meSsAgESTOP"

### 4. 
Once the message is formatted 