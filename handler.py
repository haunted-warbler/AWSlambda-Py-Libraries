import boto3
import os
import ctypes
import uuid
import sklearn
import pickle
import pandas as pd
import numpy as np

for d, _, files in os.walk('lib'):
    for f in files:
        if f.endswith('.a'):
            continue
        ctypes.cdll.LoadLibrary(os.path.join(d, f))

s3_client = boto3.client('s3')

def main(event, context):
    a = np.arange(15).reshape(3, 5)
    
    print("Your numpy array:")
    print(a)

if __name__ == "__main__":
    main('', '')
