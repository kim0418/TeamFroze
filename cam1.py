import os
import v4l2

# 비디오 장치를 차례로 테스트
for i in range(31):  # 31은 테스트할 비디오 장치의 수를 의미합니다.
    try:
        vd = open('/dev/video{}'.format(i), 'rw')
        cp = v4l2.v4l2_capability()
        fcntl.ioctl(vd, v4l2.VIDIOC_QUERYCAP, cp)

        if cp.capabilities & v4l2.V4L2_CAP_VIDEO_CAPTURE:
            print('/dev/video{} supports V4L2.'.format(i))
        else:
            print('/dev/video{} does not support V4L2.'.format(i))
    except IOError:
        print('/dev/video{} does not exist.'.format(i))
