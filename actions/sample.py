import json
import hashlib
from pathlib import Path

def execute(inputs, action_version, destination):
    data=json.dumps({"inputs":inputs,"version":action_version},sort_keys=True).encode("utf-8")
    path=Path(destination)
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_bytes(data)
    return {"sha256":hashlib.sha256(data).hexdigest(),"path":str(path)}
