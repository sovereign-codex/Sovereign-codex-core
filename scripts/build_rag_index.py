#!/usr/bin/env python3
import os, json, glob, hashlib
ROOT = os.path.dirname(os.path.dirname(__file__))
docs = []
for p in ["scrolls","ko/samples"]:
    for fp in glob.glob(os.path.join(ROOT,p,"**","*.*"), recursive=True):
        if fp.endswith((".md",".txt",".json")):
            text = open(fp,"r",encoding="utf-8").read()
            h = hashlib.sha256(text.encode()).hexdigest()[:16]
            docs.append({"path": os.path.relpath(fp, ROOT), "sha16": h, "len": len(text)})
os.makedirs(os.path.join(ROOT,"indices"), exist_ok=True)
with open(os.path.join(ROOT,"indices","kodex.index.json"),"w",encoding="utf-8") as f:
    json.dump({"docs": docs}, f, indent=2)
print(f"Indexed {len(docs)} docs → indices/kodex.index.json")
