import time
import matplotlib.pyplot as plt
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import random
# =========================================================
# PLAYFAIR CIPHER
# =========================================================
def make_matrix(key):
    key = key.upper()
    # Replace J with I
    key = key.replace("J", "I")
    letters = ""
    # Add key letters first
    for ch in key:
        if ch.isalpha() and ch not in letters:
            letters += ch
    # Add remaining alphabet letters
    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in letters:
            letters += ch
    # Create 5 x 5 matrix
    matrix = []
    for i in range(0, 25, 5):
        matrix.append(letters[i:i + 5])
    return matrix
def find_position(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j
    return None
def prepare_text(text):
    # Keep only letters, and replace J with I
    clean = ""
    for ch in text.upper():
        if ch.isalpha():
            clean += ch
    clean = clean.replace("J", "I")

    result = ""
    i = 0
    while i < len(clean):
        a = clean[i]

        # Last character: pad with X
        if i + 1 == len(clean):
            result += a + "X"
            i += 1
        # Same letters in a pair: insert X
        elif clean[i] == clean[i + 1]:
            result += a + "X"
            i += 1
        # Normal pair
        else:
            result += a + clean[i + 1]
            i += 2

    return result
def playfair_encrypt(text, key):
    matrix = make_matrix(key)
    text = prepare_text(text)
    result = ""
    for i in range(0, len(text), 2):
        a = text[i]
        b = text[i + 1]
        pos1 = find_position(matrix, a)
        pos2 = find_position(matrix, b)
        r1, c1 = pos1
        r2, c2 = pos2
        # Same row
        if r1 == r2:
            result += matrix[r1][(c1 + 1) % 5]
            result += matrix[r2][(c2 + 1) % 5]
        # Same column
        elif c1 == c2:
            result += matrix[(r1 + 1) % 5][c1]
            result += matrix[(r2 + 1) % 5][c2]
        # Rectangle rule
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]
    return result
def playfair_decrypt(text, key):
    matrix = make_matrix(key)
    result = ""
    for i in range(0, len(text), 2):
        a = text[i]
        b = text[i + 1]
        pos1 = find_position(matrix, a)
        pos2 = find_position(matrix, b)
        r1, c1 = pos1
        r2, c2 = pos2
        # Same row
        if r1 == r2:
            result += matrix[r1][(c1 - 1) % 5]
            result += matrix[r2][(c2 - 1) % 5]
        # Same column
        elif c1 == c2:
            result += matrix[(r1 - 1) % 5][c1]
            result += matrix[(r2 - 1) % 5][c2]
        # Rectangle rule
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]
    return result
# =========================================================
# DES
# =========================================================
def des_encrypt(text, key):
    cipher = DES.new(
        key.encode(),
        DES.MODE_ECB
    )
    data = text.encode()
    data = pad(
        data,
        DES.block_size
    )
    encrypted = cipher.encrypt(data)
    return encrypted
def des_decrypt(data, key):
    cipher = DES.new(
        key.encode(),
        DES.MODE_ECB
    )
    decrypted = cipher.decrypt(data)
    decrypted = unpad(
        decrypted,
        DES.block_size
    )
    return decrypted.decode()
# =========================================================
# INPUT
# =========================================================
message = "CRYPTOGRAPHY"
playfair_key = "AMRITA"
des_key = "8BYTEKEY"
# =========================================================
# BASIC ENCRYPTION TEST
# =========================================================
playfair_cipher = playfair_encrypt(
    message,
    playfair_key
)
playfair_plain = playfair_decrypt(
    playfair_cipher,
    playfair_key
)
des_cipher = des_encrypt(
    message,
    des_key
)
des_plain = des_decrypt(
    des_cipher,
    des_key
)
# =========================================================
# DISPLAY RESULTS
# =========================================================
print()
print("==========================================")
print("           ENCRYPTION RESULTS")
print("==========================================")
print()
print("Original Message :", message)
print()
print("---------- PLAYFAIR ----------")
print("Encrypted :", playfair_cipher)
print("Decrypted :", playfair_plain)
print()
print("---------- DES ----------")
print("Encrypted :", des_cipher.hex())
print("Decrypted :", des_plain)
# =========================================================
# PERFORMANCE TEST
# =========================================================
print()
print("==========================================")
print("           PERFORMANCE TEST")
print("==========================================")
# Large message
test_message = (
    "CRYPTOGRAPHY IS USED TO PROTECT DATA "
    "AND INFORMATION FROM UNAUTHORIZED ACCESS "
) * 100
# Number of repetitions
iterations = 10
# ---------------------------------------------------------
# PLAYFAIR TIME
# ---------------------------------------------------------
start = time.perf_counter()
for i in range(iterations):
    playfair_encrypt(
        test_message,
        playfair_key
    )
playfair_time = time.perf_counter() - start
# ---------------------------------------------------------
# DES TIME
# ---------------------------------------------------------
start = time.perf_counter()
for i in range(iterations):
    des_encrypt(
        test_message,
        des_key
    )
des_time = time.perf_counter() - start
# =========================================================
# THROUGHPUT
# =========================================================
message_size = len(test_message.encode())
playfair_throughput = (
    message_size * iterations
) / playfair_time
des_throughput = (
    message_size * iterations
) / des_time
print()
print("Playfair Time :",
      round(playfair_time, 6),
      "seconds")
print("DES Time      :",
      round(des_time, 6),
      "seconds")
print()
print("Playfair Throughput :",
      round(playfair_throughput, 2),
      "bytes/second")
print("DES Throughput      :",
      round(des_throughput, 2),
      "bytes/second")
# =========================================================
# COMPARISON VALUES
# =========================================================
algorithms = [
    "Playfair",
    "DES"
]
# Playfair = 5 x 5 matrix
# DES = 56 effective key bits
#
# This is NOT saying Playfair has a 25-bit key.
matrix_key_values = [
    25,
    56
]
# Playfair works on 2 characters
# DES works on 64-bit blocks
block_values = [
    2,
    64
]
# Relative security score
# Higher = stronger
#
# These are educational scores.

# =========================================================
# GRAPH 1 - ENCRYPTION TIME
# =========================================================
plt.figure(figsize=(7, 5))
plt.bar(
    algorithms,
    [
        playfair_time,
        des_time
    ]
)
plt.title(
    "Playfair vs DES - Encryption Time"
)
plt.xlabel("Algorithm")
plt.ylabel("Time (seconds)")
plt.show()
# =========================================================
# GRAPH 2 - THROUGHPUT
# =========================================================
plt.figure(figsize=(7, 5))
plt.bar(
    algorithms,
    [
        playfair_throughput,
        des_throughput
    ]
)
plt.title(
    "Playfair vs DES - Throughput"
)
plt.xlabel("Algorithm")
plt.ylabel("Bytes per Second")
plt.show()
# =========================================================
# GRAPH 3 - KEY / MATRIX
# =========================================================
plt.figure(figsize=(7, 5))
plt.bar(
    algorithms,
    matrix_key_values
)
plt.title(
    "Playfair vs DES - Key / Matrix Comparison"
)
plt.xlabel("Algorithm")
plt.ylabel("Size / Value")
plt.show()
# =========================================================
# GRAPH 4 - BLOCK SIZE
# =========================================================
plt.figure(figsize=(7, 5))
plt.bar(
    algorithms,
    block_values
)
plt.title(
    "Playfair vs DES - Block Size"
)
plt.xlabel("Algorithm")
plt.ylabel("Block Size")
plt.show()
# =========================================================
# GRAPH - RELATIVE SECURITY
# =========================================================
security_values = [
    1,
    2
]
plt.figure(figsize=(7, 5))
plt.bar(
    algorithms,
    security_values
)
plt.title(
    "Playfair vs DES - Relative Security"
)
plt.xlabel("Algorithm")
plt.yticks([1, 2], ["Very Weak", "Weak"])
plt.show()
# ---------------- ERROR RESISTANCE ----------------

def playfair_error_test(message, key, trials=20):
    cipher = playfair_encrypt(message, key)
    original = playfair_decrypt(cipher, key)

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    total_changed = 0
    total_chars = 0

    # Repeat several times because the damage is random
    for _ in range(trials):
        for i in range(len(cipher)):
            damaged = list(cipher)
            damaged[i] = random.choice(alphabet.replace(damaged[i], ""))

            decrypted = playfair_decrypt("".join(damaged), key)

            total_changed += sum(a != b for a, b in zip(original, decrypted))
            total_chars += len(original)

    return 100 * total_changed / total_chars if total_chars else 0


def des_error_test(message, key):
    cipher = des_encrypt(message, key)
    original = pad(message.encode(), DES.block_size)

    total_changed = 0
    total_bytes = 0

    for i in range(len(cipher)):
        for bit in range(8):
            damaged = bytearray(cipher)
            damaged[i] ^= (1 << bit)

            decryptor = DES.new(key.encode(), DES.MODE_ECB)
            decrypted = decryptor.decrypt(bytes(damaged))

            total_changed += sum(a != b for a, b in zip(original, decrypted))
            total_bytes += len(original)

    return 100 * total_changed / total_bytes if total_bytes else 0


error_test_message = "CRYPTOGRAPHYINFORMATIONSECURITY"
error_playfair = playfair_error_test(error_test_message, playfair_key)
error_des = des_error_test(error_test_message, des_key)


# ---------------- INFORMATION LEAKAGE ----------------

def repeated_unit_rate(units):
    if not units:
        return 0
    counts = {}
    for unit in units:
        counts[unit] = counts.get(unit, 0) + 1
    repeated = sum(c for c in counts.values() if c > 1)
    return 100 * repeated / len(units)


def playfair_leak_test(message, key):
    cipher = playfair_encrypt(message, key)
    pairs = [cipher[i:i + 2] for i in range(0, len(cipher), 2)]
    return repeated_unit_rate(pairs)


def des_leak_test(message, key):
    cipher = des_encrypt(message, key)
    blocks = [cipher[i:i + DES.block_size]
              for i in range(0, len(cipher), DES.block_size)]
    return repeated_unit_rate(blocks)


leak_test_message = "ATTACKATDAWN" * 20
leak_playfair = playfair_leak_test(leak_test_message, playfair_key)
leak_des = des_leak_test(leak_test_message, des_key)


# ---------------- PRINT RESULTS ----------------

print("\nERROR RESISTANCE (lower = error stays local)")
print(f"Playfair: {error_playfair:.2f}% plaintext positions changed")
print(f"DES:      {error_des:.2f}% plaintext positions changed")

print("\nINFORMATION LEAKAGE (lower = better)")
print(f"Playfair: {leak_playfair:.2f}% repeated ciphertext pairs")
print(f"DES:     {leak_des:.2f}% repeated ciphertext blocks")


# ---------------- PRINT RESULTS ----------------

print("\nERROR RESISTANCE")
print(f"Playfair: {error_playfair:.2f}% plaintext positions changed")
print(f"DES:      {error_des:.2f}% plaintext positions changed")

print("\nINFORMATION LEAKAGE")
print(f"Playfair: {leak_playfair:.2f}% repeated ciphertext pairs")
print(f"DES:      {leak_des:.2f}% repeated ciphertext blocks")


# =========================================================
# GRAPH - ERROR RESISTANCE
# =========================================================
plt.figure(figsize=(7, 5))
plt.bar(
    algorithms,
    [
        error_playfair,
        error_des
    ]
)
plt.title(
    "Playfair vs DES - Error Resistance"
)
plt.xlabel("Algorithm")
plt.ylabel("Changed Plaintext Positions (%)")
plt.show()

# =========================================================
# GRAPH - INFORMATION LEAKAGE
# =========================================================
plt.figure(figsize=(7, 5))
plt.bar(
    algorithms,
    [
        leak_playfair,
        leak_des
    ]
)
plt.title(
    "Playfair vs DES - Information Leakage"
)
plt.xlabel("Algorithm")
plt.ylabel("Repeated Ciphertext Units (%)")
plt.show()
# =========================================================
# FINAL COMPARISON TABLE
# =========================================================
print()
print("======================================================")
print("              PLAYFAIR VS DES")
print("======================================================")
print()
print("Parameter              Playfair          DES")
print("------------------------------------------------------")
print("Type                   Classical         Block Cipher")
print("Key                    Keyword           56 effective bits")
print("Matrix                 5 x 5             Not used")
print("Block                  2 characters      64 bits")
print("Security               Very Weak         Weak")
print("Time Complexity        O(n)              O(n)")
print("Leakage Resistance     Low               Higher")
print("Error Resistance       Low               Higher")
print("Modern Use             Educational       Legacy")
print("------------------------------------------------------")
# =========================================================
# FINAL ANALYSIS
# =========================================================
print()
print("==========================================")
print("             FINAL ANALYSIS")
print("==========================================")
print("""
Playfair is a classical symmetric cipher.

It uses a 5 x 5 matrix and encrypts
two letters at a time.

DES is a symmetric block cipher.

DES uses 64-bit blocks and has an
effective key size of 56 bits.

Both algorithms have approximately
O(n) time complexity with respect
to the input size.

The actual encryption time depends
on the computer and the input size.

Playfair provides very weak security.

DES is stronger than Playfair
""")