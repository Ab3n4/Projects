import re
def mabn26(x):
    k = 0
    for i in range(len(x)):
        k = k + (ord(x[i]) - 64) * 26 ** (len(x) - i - 1)
    return k - 1
def dd(x):
    return chr(int(x) + 65)
def de_26(n):
    k = ""
    while n != -1:
        y = (n) % 26
        n = n // 26 - 1
        k = dd(y) + k
    return (k)
def evalator(kl):
    kl = re.sub(("\s*[+]\s*"), "+", kl)
    kl = re.sub(("\s*[-]\s*"), "-", kl)
    kl = re.sub(("\s*[/]\s*"), "/", kl)
    kl = re.sub(("\s*[*]\s*"), "*", kl)
    while (re.search("[0-9]+[*][0-9]+|[0-9]+[/][0-9]+", kl) != None):
        t = re.search("[0-9]+[*][0-9]+", kl)
        l = re.search("[0-9]+[/][0-9]+", kl)
        if (l == None and t != None):
            p = t.group()
            o = re.search("[*]", t.group())
            i, j = o.span()
            kl = re.sub("[0-9]+[*][0-9]+", str(int(int(p[:i]) * int(p[j:]))), kl, 1)
        elif (t == None and l != None):
            p = l.group()
            o = re.search("[/]", l.group())
            i, j = o.span()
            kl = re.sub("[0-9]+[/][0-9]+", str(int(int(p[:i]) / int(p[j:]))), kl, 1)
        elif (l.start() > t.start()):
            p = t.group()
            o = re.search("[*]", t.group())
            i, j = o.span()
            kl = re.sub("[0-9]+[*][0-9]+", str(int(int(p[:i]) * int(p[j:]))), kl, 1)
        else:
            p = l.group()
            o = re.search("[/]", l.group())
            i, j = o.span()
            kl = re.sub("[0-9]+[/][0-9]+", str(int(int(p[:i]) / int(p[j:]))), kl, 1)
    x = re.split("[+]|[-]", kl)
    c = re.findall("[+]|[-]", kl)
    flag = 1
    # print(x,c)
    while (len(x) > 1 and flag == 1):
        if c[0] == "+":
            if (x[0].isdecimal() and x[1].isdecimal()):
                x[1] = str(int(x[0]) + int(x[1]))
                del x[0]
                del c[0]
            elif (x[0].isdecimal() and not x[1].isdecimal()):
                if x[1][1:-1].isupper() and x[1][1:-1].isalpha():
                    x[1] = str(int(x[0]) + int(mabn26(x[1][1:-1])))
                    del x[0]
                    del c[0]
                else:
                    x[0] = "unsupported operand"
                    flag = 0
            elif (not x[0].isdecimal() and x[1].isdecimal()):
                if x[0][1:-1].isupper() and x[0][1:-1].isalpha():
                    x[1] = "\"" + de_26(int(mabn26((x[0][1:-1]))) + int(x[1])) + "\""
                    del x[0]
                    del c[0]
                else:
                    x[0] = "unsupported operand"
                    flag = 0
            else:
                o1 = re.sub("\"", "", x[0])
                o2 = re.sub("\"", "", x[1])
                x[1] = "\"" + o1 + o2 + "\""
                del x[0]
                del c[0]
        else:
            if (x[0].isdecimal() and x[1].isdecimal()):
                x[1] = str(int(x[0]) - int(x[1]))
                del x[0]
                del c[0]
            elif (x[0].isdecimal() and not x[1].isdecimal()):
                if x[1][1:-1].isupper() and x[1][1:-1].isalpha():
                    x[1] = str(int(x[0]) - int(mabn26(x[1][1:-1])))
                    del x[0]
                    del c[0]
                else:
                    x[0] = "unsupported operand"
                    flag = 0
            elif (not x[0].isdecimal() and x[1].isdecimal()):
                if x[0][1:-1].isupper() and x[0][1:-1].isalpha():
                    x[1] = "\"" + de_26(int(mabn26((x[0][1:-1]))) - int(x[1])) + "\""
                    del x[0]
                    del c[0]
                else:
                    x[0] = "unsupported operand"
                    flag = 0
            else:
                x[0] = "unsupported operand"
                flag = 0
    return x[0]
def jayguh_khan(t, k):
    for i in range(len(t)):
        if not t[i].isalpha():
            DD = i
            break
    return k[int(t[DD:]) - 1][int(mabn26(evalator(t[:DD])))]
def eval_pish(equa,dic = {}, k=[]):
    equa = re.sub(("\s*[+]\s*"), "+", equa)
    equa = re.sub(("\s*[-]\s*"), "-", equa)
    equa = re.sub(("\s*[/]\s*"), "/", equa)
    equa = re.sub(("\s*[*]\s*"), "*", equa)
    ls = re.split("[+]|[-]|[*]|[/]|[\[]|[\]]", equa)
    ks = re.findall("[+]|[-]|[*]|[/]|[\[]|[\]]", equa)
    for i, j in enumerate(ls):
        if j in dic.keys():
            ls[i] = dic[j]
    for i, j in enumerate(ls):
        if re.search("[A-Z]+[0-9]+", j) and "\"" not in j:
            ls[i] = jayguh_khan(j, k)
    olo = ls[:]
    while (len(ls) > 1):
        ls[0] = ls[0] + ks[0] + ls[1]
        del ls[1]
        del ks[0]
    hala = ls[0]
    nss = re.findall(r"\[([^\]]+)\]\[([^\]]+)\]", hala)
    while (re.search(r"\[([^\]]+)\]\[([^\]]+)\]", hala) != None):
        j = evalator(nss[0][0])[1:-1]
        i = evalator(nss[0][1])
        hala = re.sub(r"\[([^\]]+)\]\[([^\]]+)\]", jayguh_khan(j + i, k), hala, 1)
        del nss[0]
    return hala
def bool_khan(equa,dic={},k=[]):
    u = "flag"
    shell = re.split("or|and", equa)
    shell_bool = re.findall("or|and", equa)
    # print(shell_bool)
    # print(shell)
    for i, j in enumerate(shell):
        if j.strip() == "true":
            shell[i] = True
            continue
        if j.strip() == "false":
            shell[i] = False
            continue
        zoro = re.split("==|>|<", j)
        t = zoro[0].strip()
        z = zoro[1].strip()
        fr = re.findall("==|>|<", j)
        do1 = evalator(eval_pish(t,dic,k))
        do2 = evalator(eval_pish(z,dic,k))
        if "\"" in do1:
            kdo1 = 1
        else:
            kdo1 = 0
        if "\"" in do2:
            kdo2 = 1
        else:
            kdo2 = 0
        if kdo1 == 0:
            do1 = int(do1)
        if kdo2 == 0:
            do2 = int(do2)
        if kdo1 == kdo2:
            if fr[0] == "==":
                if do2 == do1:
                    shell[i] = True
                else:
                    shell[i] = False
            elif fr[0] == ">":
                if do2 < do1:
                    shell[i] = True
                else:
                    shell[i] = False
            else:
                if do2 > do1:
                    shell[i] = True
                else:
                    shell[i] = False
        else:
            u = 'Error'
            break
    # shell_bool
    while (len(shell) > 1):
        if shell_bool[0] == "or":
            shell[0] = shell[0] or shell[1]
            del shell[1]
            del shell_bool[0]
        else:
            shell[0] = shell[0] and shell[1]
            del shell[1]
            del shell_bool[0]
    if u == "Error":
        return (u)
    else:
        if shell[0]:
            return ('true')
        else:
            return ('false')

def ja(t):
    for i in range(len(t)):
        if not t[i].isalpha():
            DD = i
            break
    return int(t[DD:]) - 1,int(mabn26(evalator(t[:DD])))

def hmmm(k):
    t = re.split("\[|\]", k)
    return t[1],t[3]
def nesfeval(equa,dic):
    equa = re.sub(("\s*[+]\s*"), "+", equa)
    equa = re.sub(("\s*[-]\s*"), "-", equa)
    equa = re.sub(("\s*[/]\s*"), "/", equa)
    equa = re.sub(("\s*[*]\s*"), "*", equa)
    ls = re.split("[+]|[-]|[*]|[/]|[\[]|[\]]", equa)
    ks = re.findall("[+]|[-]|[*]|[/]|[\[]|[\]]", equa)
    for i, j in enumerate(ls):
        if j in dic.keys():
            ls[i] = dic[j]
    while(len(ls)>1):
        ls[0] = ls[0]+ks[0]+ls[1]
        del ls[1]
        del ks[0]
    return ls[0]
class pyxcel:
    dic_ = {}
    lis_table= []
    curtable = []
    vars_ = {}
    def __init__(self,i,j):
        self.table = [["None"]*int(i) for _ in range(int(j))]
    def printt(mat):
        arthas = [de_26(i) for i in range(len(mat[0]))]
        mat = [arthas]+ mat
        for i in range(len(mat)):
            mat[i]= [str(i)]+mat[i]
        lens = [max(map(len, col)) for col in zip(*(mat))]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in mat]
        print('\n'.join(table))
    def kok(k):
        while (re.search(r"\[([^\]]+)\]\[([^\]]+)\]", k))!=None or re.search("[A-Z]+[0-9]+",k) != None:
            k = eval_pish(k, pyxcel.vars_, pyxcel.curtable)
        return k
    def dastorkhan(k):
        if re.match("create(.*)",k):
            t = re.split("\,",k[7:-1])
            j = pyxcel(t[1],t[2])
            pyxcel.dic_[t[0]] = j
            pyxcel.lis_table.append(t[0])

        elif re.match("print(.*)",k):
            try:
                if (re.search(r"\[([^\]]+)\]\[([^\]]+)\]", k))!=None or re.search("[A-Z]+[0-9]+",k) != None:
                    #if pyxcel.curtable == []:
                        #print("Error")
                        #return "Error"
                    #else:
                        y = pyxcel.kok(k[6:-1])
                        print("out:"+evalator(eval_pish(y,pyxcel.vars_,pyxcel.curtable)))
                else:
                    print("out:"+evalator(eval_pish(k[6:-1],pyxcel.vars_,[])))
            except:
                print("Error")
                return "Error"
            #print(pyxcel.curtable)

            #print(k[6:-1])
        elif re.match("setFunc(.*)",k):
            if pyxcel.curtable == []:
                print("Error")
                return "Error"
            else:
                t = re.split("\,",k[8:-1])
                if re.match(r"\[([^\]]+)\]\[([^\]]+)\]", t[0]):
                    i,j = hmmm(t[0])
                    i = mabn26(evalator(eval_pish(i.strip()[1:-1], pyxcel.vars_, pyxcel.curtable)))
                    j = int(evalator(eval_pish(j.strip(), pyxcel.vars_, pyxcel.curtable)))-1
                else:
                    j,i = ja(t[0].strip())
            if i > len(pyxcel.curtable[0]) or j > len(pyxcel.curtable):
                print("Error")
                return "Error"
            else:
                pyxcel.curtable[j][i] = nesfeval(t[1].strip(),pyxcel.vars_)
        elif re.match("display(.*)",k):
            too = k[8:-1].strip()
            if too not in pyxcel.lis_table:
                print("Error")
                return "Error"
            else:
                ho = pyxcel.dic_[too].table
                tem = [["None" for _ in ho[0]] for _ in ho]
                for i,i1 in enumerate(ho):
                    for j,j1 in enumerate(i1):
                        uu = pyxcel.kok(j1)
                        fo = evalator(eval_pish(uu,pyxcel.dic_,ho))
                        if "None" not in fo and "unsupported operand" not in fo:
                            tem[i][j] = evalator(eval_pish(uu,pyxcel.dic_,ho))
                pyxcel.printt(tem)

        elif re.match(".*[=].+",k):
                y = re.split("[=]",k)
                if re.match(r"\[([^\]]+)\]\[([^\]]+)\]", y[0]):
                    i,j = hmmm(y[0])
                    i = mabn26(evalator(eval_pish(i.strip(),pyxcel.vars_,pyxcel.curtable))[1:-1])
                    j = int(evalator(eval_pish(j.strip(),pyxcel.vars_,pyxcel.curtable)))
                    if i > len(pyxcel.curtable[0]) or j-1 > len(pyxcel.curtable):
                        print("Error")
                        return "Error"
                    else:
                        pyxcel.curtable[j-1][i]= evalator(eval_pish(y[1].strip(),pyxcel.vars_,pyxcel.curtable))
                elif re.match("[A-Z]+[0-9]+",y[0]):
                    i,j = ja(y[0].strip())
                    if i > len(pyxcel.curtable[0]) or j > len(pyxcel.curtable):
                        print("Error")
                        return "Error"
                    else:
                        pyxcel.curtable[i][j] = evalator(eval_pish(y[1].strip(),pyxcel.vars_,pyxcel.curtable))
                else:
                    pyxcel.vars_[y[0].strip()] = evalator(eval_pish(y[1].strip(),pyxcel.vars_,pyxcel.curtable))
        elif re.match("context(.*)",k):
            if k[8:-1] not in pyxcel.lis_table:
                print("Error")
                return "Error"
            else:
                pyxcel.curtable = pyxcel.dic_[k[8:-1]].table
    def comment(t):
        for i,j in enumerate(t):
            if j == "$":
                t = t[:i]
                break
        return t
    def iiff(t):
        t = t.strip()
        if bool_khan(t,pyxcel.vars_,pyxcel.curtable) == "true":
            return True
        elif bool_khan(t,pyxcel.vars_,pyxcel.curtable) == "false":
            return False
        else:
            print("Error")
            return ("Error")

    def darar(dast):
        n = 0
        m = 0
        for i,j in enumerate(dast):
            if "}" in j:
                n += 1
            if "{" in j:
                m += 1
            if m==n:
                break
        return dast[1:i],i

    def run(t1):
        i = 0
        while(i<len(t1)):
            if "if" in t1[i]:
                ke,f = pyxcel.darar(t1[i:])
                if pyxcel.iiff(t1[i][3:-2]):
                    pyxcel.run(ke)

                i += f
            if "while" in t1[i]:
                ke, f = pyxcel.darar(t1[i:])

                while pyxcel.iiff(t1[i][6:-2]):
                    pyxcel.run(ke)
                i += f
            else:
                if pyxcel.dastorkhan(t1[i]) == "Error":
                    return
                i = i+1
line_ = []
for i in range(int(input())):
    t = input().strip()
    line_ += [pyxcel.comment(t)]
pyxcel.run(line_)
'''for i in line_:
    if i_love.dust_2(i,line_) == "Error":
        break'''
"""14
$This code has written by Pyxcel language!
create(prices,3,10)
context(prices)
A1 = "Cost" $ set title
B1 = "Discount"
C1 = "Final Cost"
va = 2
while(va<11){
    ["A"][va] = va*1000
    ["B"][va] = 20
    setFunc(["C"][va],["A"][va]-["A"][va]*["B"][va]/100)
    va = va + 1
}
display(prices)"""
