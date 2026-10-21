def average_value1_by_type(rows):
    A = []
    B = []
    C = []
    D = []

    for point in rows:
        if point[0] == "A":
            A.append(float(point[1]))
            A.append(float(point[2]))
        elif point[0] == "B":
            B.append(float(point[1]))
            B.append(float(point[2]))
        elif point[0] == "C":
            C.append(float(point[1]))
            C.append(float(point[2]))
        else:
            D.append(float(point[1]))
            D.append(float(point[2]))

    A_avg = sum(A)/len(A)
    B_avg = sum(B)/len(B)
    C_avg = sum(C)/len(C)
    D_avg = sum(D)/len(D)

    return [("A",A_avg),("B",B_avg),("C",C_avg),("D",D_avg)]
