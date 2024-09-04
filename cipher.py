from algoritmos import ascon
from utils.timing import measure_execution_time


class AsconCipher:

    def encrypt(self, key, nonce, associateddata, plaintext, variant):
        return ascon.ascon_encrypt, key, nonce, associateddata, plaintext, variant

    def decrypt(self, key, nonce, associateddata, ciphertext, variant):
        return ascon.ascon_decrypt, key, nonce, associateddata, ciphertext, variant

    def encrypt_and_measure_time(self, key, nonce, associateddata, plaintext, variant):
        return measure_execution_time(ascon.ascon_encrypt, key, nonce, associateddata, plaintext, variant)

    def decrypt_and_measure_time(self, key, nonce, associateddata, ciphertext, variant):
        return measure_execution_time(ascon.ascon_decrypt, key, nonce, associateddata, ciphertext, variant)

    def get_random_key(self, keysize):
        return ascon.get_random_bytes(keysize)

    def get_random_nonce(self, num):
        return ascon.get_random_bytes(num)

    def bytes_to_hex(self, byte_data):
        return ascon.bytes_to_hex(byte_data)

# to do: probably convert method to @staticmethod to remove the need for an instance
