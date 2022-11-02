import time
import VL53L0X
import sys

#create objet sensor
tof1 = VL53L0X.VL53L0X(TCA9548A_Num=0, TCA9548A_Addr=0x70)
tof2 = VL53L0X.VL53L0X(TCA9548A_Num=1, TCA9548A_Addr=0x70)
tof3 = VL53L0X.VL53L0X(TCA9548A_Num=2, TCA9548A_Addr=0x70)
tof4 = VL53L0X.VL53L0X(TCA9548A_Num=3, TCA9548A_Addr=0x70)

#startin sensor bus 1
tof1.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)
tof2.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)
tof3.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)
tof4.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)

#timing = tof1.get_timing()
#if (timing < 20000):
#	timing=20000

#for count
dist=tof1.get_distance()
dist1=tof2.get_distance()
dist2=tof3.get_distance()
dist3=tof4.get_distance()

cm1=dist/10
cm2=dist1/10
cm3=dist2/10
cm4=dist3/10

sys.stdout.write(",%d,%d,%d,%d" % (cm1,cm2,cm3,cm4))

#if(dist > 0):
#	sys.stdout.write("%d" % (dist/10))




