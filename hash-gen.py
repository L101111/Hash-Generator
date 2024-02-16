import hashlib
import argparse
import sys


if len(sys.argv)>1:
    if sys.argv[1]=="-h" or sys.argv[1]=="--help" or sys.argv[1]=="help":
        print(""" 
        
            __  __           __       ______                           __            
           / / / /___ ______/ /_     / ____/__  ____  ___  _________ _/ /_____  _____
          / /_/ / __ `/ ___/ __ \   / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/
         / __  / /_/ (__  ) / / /  / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /    
        /_/ /_/\__,_/____/_/ /_/   \____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/     
                                                             Made by hei$enberg 

    Hash Generator is a tool that turns plaintext into hash. To use simply type:
                
              $>  python3 hash-gen.py
           
    Supported algorithms:  
    MD5
    SHA1
    SHA224
    SHA256
    SHA384
    SHA512
    BLAKE2b (512-bit)
    BLAKE2s (256-bit)
    SHA3_224
    SHA3_256
    SHA3_384
    SHA3_512
    SHAKE128
    SHAKE256 

        """)
        sys.exit()

print("""

            __  __           __       ______                           __            
           / / / /___ ______/ /_     / ____/__  ____  ___  _________ _/ /_____  _____
          / /_/ / __ `/ ___/ __ \   / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/
         / __  / /_/ (__  ) / / /  / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /    
        /_/ /_/\__,_/____/_/ /_/   \____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/     
                                                             Made by hei$enberg 

                            Welcome to Hash Generator!               

"""
)


algorithms = ['blake2b', 'blake2s', 'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512', 'sha512', 'shake_128', 'shake_256']

plain=input('Enter the plaintext you want to hash: ')
print(' ')
while True:
    chosen_alg = input("""Choose one of the available algorithms: 
            blake2b, blake2s, md5, sha1, 
            sha224, sha256, sha384, sha3_224, 
            sha3_256, sha3_384, sha3_512, sha512, 
            shake_128 
            $> """)
    if chosen_alg in algorithms:
        break
    else:
        print('Invalid input: choose one from the provided list.')
h=hashlib.new(chosen_alg, plain.encode()).hexdigest()
print(' ')
print('     SUCCESS!')
print(f'$$   {h}    $$')
