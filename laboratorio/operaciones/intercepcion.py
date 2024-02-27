def intercepcion2(conjunto1, conjunto2):
    inter = []
    if len(conjunto1)>len(conjunto2):
        for i in range(len(conjunto1)):
            if conjunto1[i]==conjunto2[i]:
                inter[i] = conjunto1[i]

    print()