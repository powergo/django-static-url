import os
import datetime
import hashlib


def get_static_url_now(static_url_base, hash_url=True, secret_key=None):
    """Computes a static url based on the current time. This is usually a good
    way to compute a URL in DEBUG mode. In production, the time will change
    every time the process is restarted which will invalidate any client-side
    caching.

    :param static_url_base: The first part of the static url.
    :param hash_url: If True, hash the suffix with md5. Use secret_key as salt
                     if set.
    :param secret_key: If given, used as a salt in the hash.
    """
    suffix = "{0:.0f}".format(datetime.datetime.now().timestamp())
    if hash_url:
        suffix = _hash_suffix(suffix, secret_key)

    return static_url_base + suffix + "/"


def get_static_url_file(static_url_base, file_path, hash_url=True,
                        secret_key=None):
    """Computes a static url based on the access time of a file. This is
    usually a good strategy for production use because you just need to touch a
    file (and reload the process) to change the STATIC URL. If the file is not
    touched, the URL stays the same even if the process is uploaded

    :param static_url_base: The first part of the static url.
    :param file_path: The file path to get the access time.
    :param hash_url: If True, hash the suffix with md5. Use secret_key as salt
                     if set.
    :param secret_key: If given, used as a salt in the hash.
    """
    suffix = "{0:.0f}".format(os.stat(file_path).st_atime)

    if hash_url:
        suffix = _hash_suffix(suffix, secret_key)
    return static_url_base + suffix + "/"


def _hash_suffix(suffix, salt):
    hash = hashlib.md5()
    if salt:
        hash.update(salt.encode("utf-8"))
    hash.update(suffix.encode("utf-8"))
    suffix = hash.hexdigest()

    return suffix
