import sys
import json

data = json.load(sys.stdin)

print(data["name"])
