#import neck as cp
#import keypoint_all as key
from . import neck as cp
from . import keypoint_all as key
#import bodyrange as br
from . import body as br

def speech():
	x, y = key.keypoint("1", 0)
	x2, y2 = key.keypoint("1", 1)
	x3, y3 = key.keypoint("2", 0)
	x4, y4 = key.keypoint("2", 1)

	a = cp.getDegree(x, y, x2, y2)
	b = cp.getDegree(x3, y3, x4, y4)
	c, d, e = cp.sHead(a, b)

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



	return cp.head_point_out(c,d,e), bodyarray, armarray

'''
BS_x, BS_y, BW_x, BW_y = br.arm_right_left("1")
PS_x, PS_y, PW_x, PW_y = br.arm_right_left("2")


bmaxY, bminY = br.Max(BW_y)
pmaxY, pminY = br.Max(PW_y)
# neck range
Ok, Low, bodyarray = br.isbodyrange(y2, y4, bminY, pminY)

arm_bAngle = cp.getDegree(BS_x, BS_y, BW_x, BW_y)
arm_pAngle = cp.getDegree(PS_x, PS_y, PW_x, PW_y)

armOb = cp.armframe(y4)

Ok, Fal, armarray = br.armheight(arm_bAngle, arm_pAngle, armOb)
'''
'''
x2, y2 = key.keypoint("1", 1)
x4, y4 = key.keypoint("2", 1)

BS_x, BS_y, BW_x, BW_y = br.arm_right_left("1")
PS_x, PS_y, PW_x, PW_y = br.arm_right_left("2")


bmaxY, bminY = br.Max(BW_y)
pmaxY, pminY = br.Max(PW_y)
# neck range
Ok, Low, bodyarray = br.isbodyrange(y2, y4, bminY, pminY)

arm_bAngle = cp.getDegree(BS_x, BS_y, BW_x, BW_y)
arm_pAngle = cp.getDegree(PS_x, PS_y, PW_x, PW_y)

for i in range(len(arm_pAngle)):

    print(arm_pAngle[i])
    print(arm_bAngle[i])
    print('\n')

Ok, Fal, armarray = br.armheight(arm_bAngle, arm_pAngle)
'''