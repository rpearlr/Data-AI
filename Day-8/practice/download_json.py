from urllib.request import Request,urlopen
import ssl
import json
import threading
def download () :
    url = "https://fakestoreapi.com/products"
    headers = {
        "User-Agent" : "Mozilla/5.0"
    }
    req=Request(url,headers=headers)
    
    context = ssl._create_unverified_context()
    
    with urlopen(req,context=context) as res:
        data = res.read()
    print("data is downloaded")
    
    posts = json.loads(data)
    
    with open("posts.json","w") as f :
        json.dump(posts,f,indent=4)

t= threading.Thread(target=download)
t.start()