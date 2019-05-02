import none as no

NO1, NE1 = no.headkeypoints("1")
maxX, maxY = no.Framescale('/home/ms/frame/frame_10.jpg')
x, y = no.NoseKeypoint(NO1, maxX, maxY)
x2, y2 = no.NeckKeypoint(NE1, maxX, maxY)

NO2, NE2 = no.headkeypoints("2")
maxX2, maxY2 = no.Framescale('/home/ms/frame/frame_20.jpg')
x3, y3 = no.NoseKeypoint(NO2, maxX2, maxY2)
x4, y4 = no.NeckKeypoint(NE2, maxX2, maxY2)

NO3, NE3 = no.headkeypoints("3")
maxX3, maxY3 = no.Framescale('/home/ms/frame/frame_30.jpg')
x5, y5 = no.NoseKeypoint(NO3, maxX3, maxY3)
x6, y6 = no.NeckKeypoint(NE3, maxX3, maxY3)

a = no.getDegree(x, y, x2, y2)
b = no.getDegree(x5, y5, x6, y6)
c, d, e = no.sHead(a, b)

no.head_point_out(c,d,e)

