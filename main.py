import boto3
import dotenv
import codecs

dotenv.load_dotenv()

class EncryptionWithKMS:
    def __init__(self, key_id: str):
        self.client = boto3.client('kms',
            region_name='ap-northeast-1')
        self.key_id = key_id
    
    def encrypt(self, plaintext: str) -> bytes:
        response = self.client.encrypt(
            KeyId=self.key_id,
            Plaintext=plaintext,
        )
        return response['CiphertextBlob']

    def decrypt(self, ciphertext: bytes) -> str:
        response = self.client.decrypt(
            CiphertextBlob=ciphertext,
        )
        return response['Plaintext'].decode('utf-8')

if __name__ == '__main__':
    # サンプル
    sampleText = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    print('Sample Text: ', sampleText)

    # KMSを使って暗号化
    kms = EncryptionWithKMS(key_id='alias/kms-test')
    ciphertext = kms.encrypt(plaintext=sampleText)
    print('Ciphertext: ', codecs.encode(ciphertext, 'hex'))

    # KMSを使って復号
    plaintext = kms.decrypt(ciphertext=ciphertext)
    print('Plaintext: ', plaintext)
