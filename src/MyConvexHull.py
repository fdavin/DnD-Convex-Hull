from cmath import inf

def titikExtreme(bucket):
    nilaimin = inf
    nilaimaks = -inf
    ttkmin = 0
    ttkmaks = 0
    for i in range(len(bucket)):
        if bucket[i][1] < nilaimin:
            nilaimin = bucket[i][1]
            ttkmin = i
        
        if bucket[i][1] > nilaimaks:
            nilaimaks = bucket[i][1]
            ttkmaks = i
    
    return (ttkmin,ttkmaks)

def inLeft(p1,p2,p0):
    result = ( (p2.item(1) - p1.item(1)) * (p0.item(0) - p2.item(0)) ) - ( (p2.item(0) - p1.item(0)) * (p0.item(1) - p2.item(1)) )
    return (result < 0)


def Jarak(p1,p2,p0):
    return (1/2) * abs((p1.item(0) - p0.item(0)) * (p2.item(1)-p1.item(1)) - (p1.item(0) - p2.item(0)) * (p0.item(1) - p1.item(1)))


def TitikTerjauh(awal,akhir,bucket):
    jarak = 0
    titik = -1
    notFound = True
    if len(bucket) == 1:
        if bucket == [[]]:
            return -1
        else:
            return 0
    for i in range(len(bucket)):
        if (inLeft(awal,akhir,bucket[i])):
            if jarak < Jarak(awal,akhir,bucket[i]):
                notFound = False
                jarak = Jarak(awal,akhir,bucket[i])
                titik = i
    if notFound:
        return -1
    else:
        return titik


def splitBucketLeft(awal,akhir,bucket):
    finbucket = [[]]
    for i in range(len(bucket)):
        if inLeft(awal,akhir,bucket[i]):
            if finbucket == [[]]:
                finbucket[0] = bucket[i]
            else:
                finbucket.append(bucket[i])
    return finbucket
            

def subConvexHull(awal,akhir,bucket,hull):
    titik = TitikTerjauh(awal,akhir,bucket)
    if titik == -1:
        return
    else:
        subConvexHull(awal,bucket[titik],splitBucketLeft(awal,bucket[titik],bucket),hull)
        hull.append(bucket[titik])
        subConvexHull(bucket[titik],akhir,splitBucketLeft(bucket[titik],akhir,bucket),hull)

def ConvexHull(bucket):
    (titikMin,titikMaks) = titikExtreme(bucket)
    hull = [bucket[titikMin]]
    subConvexHull(bucket[titikMin],bucket[titikMaks],splitBucketLeft(bucket[titikMin],bucket[titikMaks],bucket),hull)
    hull.append(bucket[titikMaks])
    subConvexHull(bucket[titikMaks],bucket[titikMin],splitBucketLeft(bucket[titikMaks],bucket[titikMin],bucket),hull)
    hull.append(bucket[titikMin])
    return hull

