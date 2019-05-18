import comphead as head

NO1, NE1 = head.headkeypoints("1")
maxX, maxY = head.Framescale('/home/ms/frame/frame_10.jpg')
x, y = head.NoseKeypoint(NO1, maxX, maxY)
x2, y2 = head.NeckKeypoint(NE1, maxX, maxY)

NO2, NE2 = head.headkeypoints("2")
maxX2, maxY2 = head.Framescale('/home/ms/frame/frame_20.jpg')
x3, y3 = head.NoseKeypoint(NO2, maxX2, maxY2)
x4, y4 = head.NeckKeypoint(NE2, maxX2, maxY2)

a = head.getDegree(x, y, x2, y2)
b = head.getDegree(x3, y3, x4, y4)
c, d, e = head.sHead(a, b)

print(head.head_point_out(c,d,e))

