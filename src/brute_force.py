import hashlib


def brute_force(hash):
    for i in range(999999):
        pwd = str(i)
        if hash == hashlib.md5(pwd.encode()).hexdigest():
            print(pwd)


brute_force("c8d278dd28e1c4ac23774d004bce1d74")
