import comphead as cp
import keypoint as key
import bodyrange as br
import climber as cb
import lunge as lu


x, y = key.keypoint("bpush", 0)
x2, y2 = key.keypoint("bpush", 1)
x3, y3 = key.keypoint("ppush", 0)
x4, y4 = key.keypoint("ppush", 1)

print(cp.same(y2, y4))

# a = cp.getDegree(x, y, x2, y2)
# b = cp.getDegree(x3, y3, x4, y4)
# c, d, e = cp.sHead(a, b)

# print(cp.head_point_out(c,d,e))

# BS_x, BS_y, BW_x, BW_y = br.arm_right_left("1")
# PS_x, PS_y, PW_x, PW_y = br.arm_right_left("2")


# bmaxY, bminY = br.Max(BW_y)
# pmaxY, pminY = br.Max(PW_y)
# # neck range
# Ok, Low, bodyarray = br.isbodyrange(y2, y4, bminY, pminY)

# arm_bAngle = cp.getDegree(BS_x, BS_y, BW_x, BW_y)
# arm_pAngle = cp.getDegree(PS_x, PS_y, PW_x, PW_y)

# armOb = br.armframe(y4)

# P_arOk, P_arFal, P_ararmarray = br.armheight(arm_bAngle, arm_pAngle, armOb)

# print(armarray)

def climber():
	'''
	#마운팅 클라이밍 목 비교
	C_x, C_y = key.keypoint("bclimber", 0)
	C_x2, C_y2 = key.keypoint("bclimber", 1)
	C_x3, C_y3 = key.keypoint("pclimber", 0)
	C_x4, C_y4 = key.keypoint("pclimber", 1)

	C_a = cp.getDegree(C_x, C_y, C_x2, C_y2)
	C_b = cp.getDegree(C_x3, C_y3, C_x4,C_y4)
	C_c, C_d, C_e = cp.sHead(C_a, C_b)

	C_head = cp.head_point_out(C_c,C_d,C_e)
	'''
	
	#마운팅 클라이밍 팔 수직 비교
	# C_BS_x, C_BS_y, C_BW_x, C_BW_y = br.arm_right_left("bclimber")
	# C_PS_x, C_PS_y, C_PW_x, C_PW_y = br.arm_right_left("pclimber")

	# C_arm_bAngle = cp.getDegree(C_BS_x, C_BS_y, C_BW_x, C_BW_y)
	# C_arm_pAngle = cp.getDegree(C_PS_x, C_PS_y, C_PW_x, C_PW_y)

	# C_aOK, C_aFal, C_aarray = cb.C_armheight(C_arm_bAngle, C_arm_pAngle)
	'''
	#마운팅 클라이밍의 무릅 가동 범위 확인
	# C_isOK, C_isFal, C_isarray = cb.ispullknee()
	'''
	#마운팅 클라이밍의 엉덩이 높이 확인
	# C_HIOK, C_HIFal, C_HIarray = cb.Hipheight()

	# C_all = C_aarray + C_isarray + C_HIarray

	# print(C_HIarray)

	# print("long head")
	# print(C_c, C_d)

	# print("long suzic")
	# print(C_aFal)
	# print("long range")
	# print(C_isFal)
	# print("long hip")
	# print(C_HIFal)

	# print(len(C_isFal)/len(C_isarray))
	# print(len(C_isarray))
	# return C_isarray

# climber()

# L_isOK, L_isFal, L_isarray = lu.lunge_waist()
# print(L_isOK,L_isFal,L_isarray)

# L_fOK, L_fFal, L_farray = lu.isfloor()
# print(L_fOK,L_fFal,L_farray)

# a,b,c,d,e,f = lu.overknee()
# print(a,b,c,d,e,f)

# br.iswaist()