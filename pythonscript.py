import json
from boto3 import s3
from Crypto.PublicKey import RSA
import sys

def lambda_handler():
    # TODO implement
    try:
        if event['RequestType'] == 'Create':
            # Generate keys
            new_key = RSA.generate(4096)
            pub_key = new_key.publickey().exportKey(format='OpenSSH')
            priv_key = new_key.exportKey()

            f = open('/tmp/private_key','wb')
            f.write(private_key)
            f.close()

            # Upload priivate key to S3
            s3 = boto.client('s3')
            bucket_name = 'my-bucket'
            s3.upload_file('/tmp/private_key',bucket_name,'private_key')
        else:
            print('invalid')

    except:
        traceback.print_exc()
        cfnresponse.send(event, context, cfnresponse.FAILED, {}, '') 


if __name__== "__main__":
  lambda_handler()