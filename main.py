import comphead as cp
import keypoint as key
import bodyrange as br

x, y = key.keypoint("1", 0)
x2, y2 = key.keypoint("1", 1)
x3, y3 = key.keypoint("2", 0)
x4, y4 = key.keypoint("2", 1)

a = cp.getDegree(x, y, x2, y2)
b = cp.getDegree(x3, y3, x4, y4)
c, d, e = cp.sHead(a, b)


cp.head_point_out(c,d,e)

BS_x, BS_y, BW_x, BW_y = br.arm_right_left("1")
PS_x, PS_y, PW_x, PW_y = br.arm_right_left("2")


bmaxY, bminY = br.Max(BW_y)
pmaxY, pminY = br.Max(PW_y)
# neck range
Ok, Low, bodyarray = br.isbodyrange(y2, y4, bminY, pminY)

arm_bAngle = cp.getDegree(BS_x, BS_y, BW_x, BW_y)
arm_pAngle = cp.getDegree(PS_x, PS_y, PW_x, PW_y)

armOb = br.armframe(y4)

Ok, Fal, armarray = br.armheight(arm_bAngle, arm_pAngle, armOb)

print(armarray)