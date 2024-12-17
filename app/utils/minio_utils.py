from minio import Minio

def minio_client():
    return Minio(
        "minio:9000",
        access_key="root_minio",
        secret_key="password_minio",
        secure=False  # Set to True if Minio is set up with TLS
    )
