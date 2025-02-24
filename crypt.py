import math
import random
import base64

def generate_key():
    numberkey = random.randint(1, 180)
    print(f"The number generated: {numberkey}")
    sin_value = math.sin(math.radians(numberkey))
    print(f"Sin value: {sin_value}")
    encoded_key = base64.b64encode(str(sin_value).encode('utf-8')).decode('utf-8')
    return encoded_key

def decodekey(key):
    decoded = base64.b64decode(key.encode('utf-8')).decode('utf-8')
    return float(decoded)

def encodestring(stringtext, key):
    modified = [ord(c) + 69 for c in stringtext]
    key_val = decodekey(key)
    keytransform = math.asin(key_val)
    if keytransform < 360:
        keytransform += 1
    else:
        keytransform -= 1
    encoded_nums = [round(num * keytransform) for num in modified]
    num_string = ','.join(str(num) for num in encoded_nums)
    encoded_string = base64.b64encode(num_string.encode('utf-8')).decode('utf-8')
    return encoded_string

def decode_string(encoded_string, key):
    decoded_b64 = base64.b64decode(encoded_string.encode('utf-8')).decode('utf-8')
    encoded_nums = [int(x) for x in decoded_b64.split(',') if x]
    key_val = decodekey(key)
    keytransform = math.asin(key_val)
    if keytransform < 360:
        keytransform += 1
    else:
        keytransform -= 1
    original_nums = [round(num / keytransform) - 69 for num in encoded_nums]
    original_string = ''.join(chr(num) for num in original_nums)
    return original_string
def writetofile(stringtext1, key, filepath):
    origin = f"""import crypt as crypt5
import math
import random
import base64

key = "{key}"
code = "{stringtext1}"
codexe = crypt5.decode_string(code, key)
exec(codexe)"""
    with open(filepath, "w") as output:
        output.write(origin)


