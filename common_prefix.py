def common_prefix(words):
    prefix = []
    t=[]
    j=0
    while j>=0:
        try:
            for i in words:
                t.append(i[j])
            if len(set(t))==1:
                prefix.append(i[j])
                j+=1
                t.clear()
            else:
                break
        except IndexError:
            break
    # print("".join(prefix))
    print(prefix)



common_prefix(([1,2,3], [1,2,4], [1,2,9]))



common_prefix(('приветxай', 'приветxв', 'привет'))