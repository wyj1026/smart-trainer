# Kinect

[TOC]

##  配置

**Win32 Debug**

**Kinect V2 SDK**

**vs项目属性：Kinect.props **



## 关节点对应枚举变量

```c++
JointType_SpineBase = 0,
JointType_SpineMid = 1,
JointType_Neck = 2,
JointType_Head = 3,
JointType_ShoulderLeft = 4,
JointType_ElbowLeft = 5,
JointType_WristLeft = 6,
JointType_HandLeft = 7,
JointType_ShoulderRight = 8,
JointType_ElbowRight = 9,
JointType_WristRight = 10,
JointType_HandRight = 11,
JointType_HipLeft = 12,
JointType_KneeLeft = 13,
JointType_AnkleLeft = 14,
JointType_FootLeft = 15,
JointType_HipRight = 16,
JointType_KneeRight = 17,
JointType_AnkleRight = 18,
JointType_FootRight = 19,
JointType_SpineShoulder = 20,
JointType_HandTipLeft = 21,
JointType_ThumbLeft = 22,
JointType_HandTipRight = 23,
JointType_ThumbRight = 24,
JointType_Count = (JointType_ThumbRight + 1)
```



![Kinect关节点对应图](C:\Users\Richado\Desktop\Kinect\Kinect关节点对应图.jpg)



## 捕捉状态对应枚举变量

```c++
TrackingState_NotTracked = 0,
TrackingState_Inferred = 1,
TrackingState_Tracked = 2
```

