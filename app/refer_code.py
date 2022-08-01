import uuid


def refer_codes():
    code = str(uuid.uuid4()).replace("-", "")[:19]
    return code
def refer_codes2():
    codex = str(uuid.uuid4()).replace("-", "")[:29]
    return codex
