# Welcome to the Ascon Encryption Application

Welcome to the **Ascon Encryption Application**, a tool designed to provide a simple interface for experimenting with the **Ascon** cryptographic algorithm. This app allows you to encrypt and decrypt data using one of the most modern lightweight cryptography algorithms, ideal for resource-constrained environments.

## About Ascon

**Ascon** is a family of cryptographic algorithms designed for lightweight encryption and authenticated encryption with associated data (AEAD). It is based on a sponge construction and is highly efficient while providing strong security guarantees. It was designed to meet the security needs of constrained devices like embedded systems or IoT.

### Key Features of Ascon:
- **Lightweight**: Optimized for small devices with limited computational power.
- **Efficient**: Ascon provides strong security without requiring excessive processing power or memory.
- **Flexible**: Can be used for both encryption and authenticated encryption with associated data (AEAD).

## Ascon Encryption Variants

Ascon provides three encryption variants, each with a different security level and performance characteristics. You can choose between these variants based on your requirements.

1. **Ascon-128**:
   - **Key Size**: 128 bits
   - **Tag Size**: 128 bits
   - **Use Case**: General-purpose encryption with moderate security requirements.
   
2. **Ascon-128a**:
   - **Key Size**: 128 bits
   - **Tag Size**: 128 bits
   - **Use Case**: Provides a higher level of security than Ascon-128 while maintaining efficiency. Ideal for more sensitive applications.

3. **Ascon-80pq**:
   - **Key Size**: 80 bits
   - **Tag Size**: 80 bits
   - **Use Case**: A lightweight variant designed for environments where both memory and computational resources are extremely limited.

### Associated Data
In addition to encrypting the plaintext, **Ascon** allows the inclusion of associated data (AD). This is data that is authenticated but not encrypted. This feature is especially useful for ensuring the integrity of metadata in addition to the encrypted payload.

### Example Use Cases for Associated Data:
- Encrypting a file and adding a checksum as associated data.
- Authenticated transmission of messages with metadata (e.g., sender information, timestamps).

## Ascon Encryption Steps

Here’s how the encryption process works in **Ascon**:

1. **Step 1: Prepare Inputs**
   - Choose the encryption variant (Ascon-128, Ascon-128a, or Ascon-80pq).
   - Provide the **key** (the secret key used for encryption).
   - Provide the **nonce** (a unique value for each encryption, used to prevent replay attacks).
   - Provide the **plaintext** (the data you wish to encrypt).
   - Optionally, provide any **associated data**.

2. **Step 2: Encrypt the Data**
   - The algorithm uses the provided key, nonce, and plaintext, and applies the encryption function.
   - If associated data is provided, it is authenticated but not encrypted.

3. **Step 3: Output the Ciphertext**
   - The result is a **ciphertext** (the encrypted data) and a **tag** (the authentication tag to ensure data integrity).
   - The ciphertext and tag can be transmitted or stored securely.

## Ascon Decryption Steps

To decrypt data encrypted with **Ascon**, follow these steps:

1. **Step 1: Prepare Inputs**
   - Choose the encryption variant (same as the one used during encryption).
   - Provide the **key** (must match the key used during encryption).
   - Provide the **nonce** (must match the nonce used during encryption).
   - Provide the **ciphertext** (the data you want to decrypt).
   - Provide the **authentication tag** (the tag that was generated during encryption).
   - Optionally, provide the **associated data**.

2. **Step 2: Decrypt the Data**
   - The algorithm will first verify the authenticity of the associated data and the ciphertext using the provided tag.
   - If the authentication is successful, it will proceed to decrypt the ciphertext into the original plaintext.

3. **Step 3: Output the Decrypted Data**
   - If the decryption is successful, the original **plaintext** is restored.
   - If the authentication fails (e.g., if the ciphertext or tag was tampered with), the algorithm will indicate an error and refuse to decrypt the data.

---

## Notes on Security

- Always ensure that your **key** and **nonce** are kept secret and unique. Reusing the same nonce with the same key can lead to security vulnerabilities.
- Ascon provides strong security guarantees, but it's important to use it properly—especially when handling sensitive data.
