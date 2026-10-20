# Playfair Cipher vs DES: Cryptography Comparison

## Project Overview

This project implements and compares two symmetric encryption algorithms: the **Playfair Cipher** and the **Data Encryption Standard (DES)**. It evaluates encryption performance, throughput, ciphertext corruption effects, and repeated ciphertext patterns using Python.

The project demonstrates the differences between a classical encryption technique and a block cipher through practical implementation, performance testing, graphs, and a comparison table.

## Objectives

- Implement encryption and decryption using the Playfair Cipher and DES.
- Measure and compare encryption execution time.
- Calculate throughput in bytes per second.
- Analyze the effects of ciphertext corruption on decrypted data.
- Examine repeated ciphertext patterns as a simplified illustration of potential information leakage.
- Visualize the comparison using graphs and summarize the results.

## Technologies Used

- **Programming Language:** Python 3
- **Libraries:** Matplotlib, PyCryptodome
- **Standard Libraries:** `time`, `random`

## Features

- Playfair Cipher encryption and decryption.
- DES encryption and decryption using ECB mode.
- Automatic text preparation and padding.
- Encryption time and throughput calculation.
- Ciphertext corruption experiments.
- Repeated ciphertext pair and block analysis.
- Graphical comparison of performance and selected characteristics.
- Final comparison table and analysis.

## Algorithms Used

### 1. Playfair Cipher

The Playfair Cipher is a classical encryption technique that encrypts two letters at a time.

- Uses a 5 × 5 matrix generated from a keyword.
- Combines the letters I and J in the matrix.
- Prepares plaintext into pairs of letters.
- Applies the same-row, same-column, and rectangle rules for encryption and decryption.

### 2. Data Encryption Standard (DES)

DES is a symmetric block cipher that encrypts data in fixed-size blocks.

- Uses 64-bit data blocks.
- Has an effective key length of 56 bits.
- This implementation uses an 8-byte key.
- Pads plaintext to fit the required block size.
- Uses ECB (Electronic Codebook) mode for encryption and decryption.

> **Security warning:** DES is obsolete and ECB mode can reveal repeated-block patterns. This project is for educational purposes only; do not use it to protect real or sensitive data.

## Performance Metrics

| Metric | Description |
|---|---|
| Encryption Time | Time taken to encrypt the test message repeatedly |
| Throughput | Input bytes processed per second during the measured repetitions |
| Key/Matrix Comparison | Illustrative comparison of Playfair's matrix and DES key characteristics |
| Block Size | Comparison of the algorithms' processing units |
| Relative Security | Educational comparison using predefined scores |
| Error Effects | Percentage of plaintext positions or bytes changed after ciphertext corruption |
| Repeated Ciphertext Units | Percentage of repeated ciphertext pairs or blocks |

## Graphs and Visualizations

The program generates graphs for:

1. Encryption Time Comparison
2. Throughput Comparison
3. Key/Matrix Comparison
4. Block Size Comparison
5. Relative Security Comparison
6. Error Effects Comparison
7. Information Leakage Comparison

These graphs visualize the observed differences between the two algorithms.

## Installation and Setup

### Step 1: Install Python

Install Python 3 if it is not already installed.

### Step 2: Install Required Libraries

Run this command in your terminal:

```bash
pip install matplotlib pycryptodome
```

### Step 3: Clone the Repository

```bash
git clone <your-repository-url>
cd <your-repository-folder>
```

Replace the placeholders with your actual GitHub repository URL and folder name.

### Step 4: Run the Program

```bash
python cryptoproject.py
```

The program uses predefined sample messages and keys, so interactive input is not required. It prints encryption/decryption results, performance measurements, error-test results, and the final comparison. Graphs are displayed using Matplotlib.

## Project Structure

```text
Playfair-DES-Comparison/
├── cryptoproject.py
└── README.md
```

## Results and Analysis

The program compares the algorithms using execution time, throughput, ciphertext corruption experiments, and repeated ciphertext units.

- Playfair uses a matrix-based approach and processes pairs of letters.
- DES processes fixed-size 64-bit blocks and uses a 56-bit effective key.
- Execution time and throughput depend on the computer, input size, Python environment, and implementation.
- Error-effect and repeated-pattern measurements provide simplified educational observations, not formal security guarantees.

The relative security scores in the program are predefined illustrative values, not results from a formal security test.

## Limitations

- Playfair is vulnerable to classical cryptanalysis.
- DES has an insufficient effective key length for modern security requirements.
- ECB mode can expose repeated-block patterns.
- The experiments use predefined sample messages and keys.
- The error-effect tests use different corruption procedures, so their results are not a perfectly controlled comparison.
- The repeated-ciphertext metric is simplified and does not measure total information leakage.

## Future Enhancements

- Add AES-GCM to compare with a modern authenticated encryption algorithm.
- Test messages of different sizes and content.
- Repeat timing tests and calculate average execution time.
- Improve consistency in the error-corruption experiments.
- Export experimental results to CSV.
- Add automated tests for encryption and decryption.
- Develop an interactive dashboard for visualizing comparisons.

## Conclusion

This project demonstrates the implementation and comparison of the Playfair Cipher and DES using Python. It evaluates their basic encryption behavior, performance, and selected characteristics through numerical measurements and graphs.

The project provides a practical introduction to cryptographic algorithms and highlights why classical ciphers and outdated encryption standards should not be used to protect sensitive information.

## Author

**Name:** Add your name here.

## License

Add a license if you intend to publish or redistribute this project.
