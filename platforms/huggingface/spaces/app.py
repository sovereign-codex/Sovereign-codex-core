import os, glob
from flask import Flask, request, jsonify
ROOT=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
def load():
  data=[]
  for p in ["scrolls","ko/samples"]:
    for fp in glob.glob(os.path.join(ROOT,p,"**","*.*"), recursive=True):
      if fp.endswith((".md",".txt",".json")):
        data.append((os.path.relpath(fp, ROOT), open(fp,"r",encoding="utf-8").read()))
  return data
CONTENT=load()
app=Flask(__name__)
@app.route("/") 
def home(): return "Sovereign Net Kodex Space — /search?q=term"
@app.route("/search")
def search():
  q=(request.args.get("q") or "").lower()
  hits=[{"path":p,"snippet":t[:240]} for p,t in CONTENT if q and q in t.lower()]
  return jsonify({"q":q,"hits":hits[:12]})
