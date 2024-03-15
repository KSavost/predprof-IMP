with open("vacancy.txt", encoding="utf8") as f:
    # проходимся по исходному файлу
    arr = list(map(lambda x: x.strip().split(";"), f.readlines()))[1:]
    print(arr)
    # кешируем данные
    d = {}
    for i in arr:
        d[i[3]] = i
    print(d)

    while True:
        # ввод
        a = input()

        if a == "устал":
            break
        if a in d.keys():
            # выводим требуемые данные (было в условии)
            print(f"В {d[a][4]} найдена искомая вакансия: {d[a][3]} . З/п составит: {d[a][0]} ")
        else:
            print('К сожалению, ничего не удалось найти')
