from algorithms import ascon
from utils.timing import measure_execution_time


class AsconController:

    def encrypt(self, params):
        self._validate_encryption_parameters(params)
        ciphertext_tag = ascon.ascon_encrypt(
            params['key'], params['nonce'], params['associated_data'], params['plaintext'], params['variant'])
        return ciphertext_tag

    def encrypt_and_measure_time(self, params):
        self._validate_encryption_parameters(params)
        ciphertext_tag, execution_time = measure_execution_time(ascon.ascon_encrypt,
                                                                params['key'], params['nonce'], params['associated_data'], params['plaintext'], params['variant'])
        return ciphertext_tag, execution_time

    def decrypt(self, params):
        self._validate_decryption_parameters(params)
        received_plaintext = ascon.ascon_decrypt(
            params['key'], params['nonce'], params['associated_data'], params['ciphertext'], params['variant'])
        return received_plaintext

    def decrypt_and_measure_time(self, params):
        self._validate_decryption_parameters(params)
        received_plaintext, execution_time = measure_execution_time(ascon.ascon_decrypt,
                                                                    params['key'], params['nonce'], params['associated_data'], params['ciphertext'], params['variant'])
        return received_plaintext, execution_time

    def _validate_encryption_parameters(self, params):
        required_params = {
            'key': bytes,
            'nonce': bytes,
            'plaintext': bytes,
            'associated_data': bytes,
            'variant': str
        }
        self._check_required_params(params, required_params)

    def _validate_decryption_parameters(self, params):
        required_params = {
            'key': bytes,
            'nonce': bytes,
            'ciphertext': bytes,
            'associated_data': bytes,
            'variant': str
        }
        self._check_required_params(params, required_params)

    def _check_required_params(self, params, required_params):
        for rp, expected_type in required_params.items():
            if rp not in params or params[rp] is None:
                raise ValueError(
                    f"{rp.replace('_', ' ').capitalize()} is required.")
            if not isinstance(params[rp], expected_type):
                raise TypeError(f"{rp.replace('_', ' ').capitalize()} must be of type {
                    expected_type.__name__}.")

    def get_random_key(self, keysize):
        return ascon.get_random_bytes(keysize)

    def get_random_nonce(self, num):
        return ascon.get_random_bytes(num)

    def bytes_to_hex(self, byte_data):
        return ascon.bytes_to_hex(byte_data)

        # to do: probably convert method to @staticmethod to remove the need for an instance
