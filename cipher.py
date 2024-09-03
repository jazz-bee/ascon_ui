from algoritmos import ascon
from utils.timing import measure_execution_time


class AsconCipher:
    def encrypt(self, key, nonce, associateddata, plaintext, variant):
        return measure_execution_time(ascon.ascon_encrypt, key, nonce, associateddata, plaintext, variant)

    def decrypt(self, key, nonce, associateddata, ciphertext, variant):
        return measure_execution_time(ascon.ascon_decrypt, key, nonce, associateddata, ciphertext, variant)
