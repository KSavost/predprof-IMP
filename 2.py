import operator


def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)


def merge(l, r, sr):
    #функция сортировки
    res = []
    i, j = 0, 0
    while i < len(l) and j < len(r):
        if sr(l[i], r[j]):
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1
    while i < len(l):
        res.append(l[i])
        i += 1
    while j < len(r):
        res.append(r[j])
        j += 1
    return res


with open("vacancy.txt", encoding="utf8") as f:
    # парсим исходный файл
    arr = list(map(lambda x: x.strip().split(";"), f.readlines()))[1:]
    sort = sorted(arr, key=lambda x: x[0],reverse=True)
    #сортируем
    print(sort[0])
    # принтим

