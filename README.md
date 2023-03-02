# DNA ENCODING

This project allows to convert a string into a DNA sequence and vice versa. This is to showcase the possibility of storing digital information inside a string of DNA. 

⚠ Disclaimer: This project is just a POC and is not intended for research or production work. This project only as educational purposes.

## I. Conversion String to DNA
### 1. Find a secret message
The first step is to find the secret message you want to encode in a DNA strand. There are some guidelines to follow:
1. The message should only contains alphanumeric characters and spaces (e.i 0-9, a-z and A-Z), no special characters or punctuation allowed.
2. Although upper-cased letters are accepted, the final message will be retrieved in lower-case meaning that acronyms might be less obvious.

### 2. Secret message => Formatted secret message
Once you have your secret message there is a first step of message formatting. It is not possible to directly convert the sentence into binary because the DNA won't be synthesizable. Indeed, when encoding txt into DNA by directly transforming bits to ATCG, we end up with high GC content and repeated patterns. This makes sense because a sentence contains a lot of repeated characters (e.g spaces ' ' or frequent letters like 'e'). It is therefore necessary to add some randomness into the sentence. To bypass this issue, we alternate between lowercase and uppercase of the same letter and sequencially assign a special character to spaces (that is the reason why special characters are not allowed).

The formatted sentence of `"This is a secret message"` becomes `"This IS#a&secrEt§meSsAgE"`.

Also to make sure we know where the message starts and stops, I encapsulated the message between "START" and "STOP". Therefore the previous sentence `"This is a secret message"` actually becomes `"STARTThis IS#a&secrEt§meSsAgESTOP"`.

### 3. Formatted secret message => Binary sequence 
Once the message is formatted, we simply convert in into Binary so `"STARTThis IS#a&secrEt§meSsAgESTOP"` becomes `"010100110101010001000001010100100101010001010100011010000110100101110011001000000100100101010011001000110110000100100110011100110110010101100011011100100100010101110100101001110110110101100101010100110111001101000001011001110100010101010011010101000100111101010000"`.

### 4. Binary sequence => DNA Sequence
For now, the conversion relies on naive bit encoding meaning :

| DNA | Binary |
| :---: | :---: |
| A | 00 |
| C | 01 |
| G | 10 |
| T | 11 |

Other data compression algorithms exist like the Huffman Code but for this Proof of concept (POC) we will keep it as simple as possible. Therefore the previous binary sequence becomes `"CCATCCCACAACCCAGCCCACCCACGGACGGCCTATAGAACAGCCCATAGATCGACAGCGCTATCGCCCGATCTAGCACCCTCAGGCTCGTCCGCCCCATCTATCAACCGCTCACCCCATCCCACATTCCAA"`

There it is, you have your DNA sequence ready to be synthetized.

## II. Conversion DNA to String
If you have a DNA strand containing a secret message and you want to read it, you'll first have to find a sequencing machine. 
For this POC, we partnered with the Pasteur institute to use a [MinION](https://nanoporetech.com/products/minion). 
The MinION reads the DNA and generates a file in the [FASTA format](minion_sequence.fasta) where it is possible to read the DNA sequence. From the DNA sequence it is possible to work backward from the conversion steps we saw above. 

Have fun encoding your own secret messages into DNA strands :smiley:
