with open('vacancy.txt','r', encoding='utf8') as f, open('vacansy_new.csv','w', encoding='utf8') as fout:
    arr = list(map(lambda p: p.strip().split(";"), f.readlines()))[1:]
    classes = {}
    vac = list(set([i[1] for i in arr]))
    fout.write(f"Work_Type, Role, Salary" + "\n")
    for i in range(len(vac)):
        res = [r for r in arr if r[1] == vac[i]]

        m = max(res,key=lambda x:int(x[0]))
        m1 = [i for i in res if i[0] == m[0]]
        m_m = max(m1,key=lambda x: x[3])
        m2 = m1 = [i for i in res if i[3] == m[3]]
        m_res = max(m2,key=lambda x: x[2])
        s = ','.join([m_res[1], m_res[3], m_res[0]])
        fout.write(f"{s}" + "\n")
