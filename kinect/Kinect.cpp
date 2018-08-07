// Kinect.cpp: 定义控制台应用程序的入口点。
#include "stdafx.h"
#include<iostream>
#include<opencv2/opencv.hpp>
#include<opencv2/imgproc.hpp>
#include<opencv2/calib3d.hpp>
#include<opencv2/highgui.hpp>
#include<math.h>

using namespace std;
using namespace cv;


void draw(Mat & img, Joint & joint_1, Joint & joint_2, ICoordinateMapper * myMapper) {
	//如果jonit_1 和 joint_2被捕捉到
	if (joint_1.TrackingState == TrackingState_Tracked && joint_2.TrackingState == TrackingState_Tracked) {
		ColorSpacePoint joint_color;
		Point point_1, point_2;
		//用joint_1构造joint_color
		myMapper->MapCameraPointToColorSpace(joint_1.Position, &joint_color);
		point_1.x = joint_color.X;
		point_1.y = joint_color.Y;
		//用joint_2构造joint_color
		myMapper->MapCameraPointToColorSpace(joint_2.Position, &joint_color);
		point_2.x = joint_color.X;
		point_2.y = joint_color.Y;
		//画线
		line(img, point_1, point_2, Vec3b(0, 255, 0), 5);
		//画圈
		circle(img, point_1, 10, Vec3b(255, 0, 0), -1);
		circle(img, point_2, 10, Vec3b(255, 0, 0), -1);
	}
}


//获取骨骼关节点信息的demo
bool handle_Joint(Joint & joint) {
	//如果joint（关节点）被捕捉	
	if (joint.TrackingState == TrackingState_Tracked) {
		std::cout << "关节点类型为:" << joint.JointType << std::endl;
		std::cout << "关节点三维坐标为(x,y,z):" << joint.Position.X <<" "<< joint.Position.Y << " " << joint.Position.Z <<std::endl<< std::endl<< std::endl;
		return true;
	}
	return false;
}
//计算两个关节点之间的距离
double cal_length(Joint & joint_1, Joint & joint_2) {
	if (joint_1.TrackingState == TrackingState_Tracked && joint_2.TrackingState == TrackingState_Tracked)
		return sqrt(pow(abs(joint_1.Position.X - joint_2.Position.X), 2) + pow(abs(joint_1.Position.Y - joint_2.Position.Y), 2) + pow(abs(joint_1.Position.Z - joint_2.Position.Z), 2));
	else
		return 0;
}
//计算两个骨头的夹角(三骨骼节点，以joint为交点)
double cal_degree(Joint & joint_1, Joint & joint_2, Joint & joint) {
	if (joint_1.TrackingState == TrackingState_Tracked && joint_2.TrackingState == TrackingState_Tracked && joint.TrackingState == TrackingState_Tracked)
	{
		//向量化
		double x1 = joint_1.Position.X - joint.Position.X;
		double y1 = joint_1.Position.Y - joint.Position.Y;
		double z1 = joint_1.Position.Z - joint.Position.Z;

		double x2 = joint_2.Position.X - joint.Position.X;
		double y2 = joint_2.Position.Y - joint.Position.Y;
		double z2 = joint_2.Position.Z - joint.Position.Z;

		double dz = z2 - z1;
		double dy = y2 - y1;
		double dx = x2 - x1;
		double angle = atan2(abs(dz), sqrt(dx * dx + dy * dy));
		angle = angle * 180 / 3.1415926;
		return angle;
	}
	return 0;
}
int main()
{	
	//init kinectsensor;
	IKinectSensor * myKinectSensor = nullptr;
	GetDefaultKinectSensor(&myKinectSensor);
	myKinectSensor->Open();


	//init ColorFrame :Source Reader
	IColorFrameSource *myColorSource = nullptr;
	myKinectSensor->get_ColorFrameSource(&myColorSource);

	IColorFrameReader * myColorReader = nullptr;
	myColorSource->OpenReader(&myColorReader);

	int colorHeight = 0, colorWidth = 0;

	//从kinect中得到界面的一个描述（高宽）
	IFrameDescription   * myDescription = nullptr;
	myColorSource->get_FrameDescription(&myDescription);
	myDescription->get_Height(&colorHeight);
	myDescription->get_Width(&colorWidth);

	IColorFrame * myColorFrame = nullptr;
	Mat original(colorHeight, colorWidth, CV_8UC4);

	//init BodyFrame :Source  Reader
	IBodyFrameSource * myBodySource = nullptr;
	myKinectSensor->get_BodyFrameSource(&myBodySource);

	IBodyFrameReader * myBodyReader = nullptr;
	myBodySource->OpenReader(&myBodyReader);

	IBodyFrame * myBodyFrame = nullptr;

	int myBodyCount = 0;
	myBodySource->get_BodyCount(&myBodyCount);

	//坐标基准绘图
	ICoordinateMapper * myMapper = nullptr;
	myKinectSensor->get_CoordinateMapper(&myMapper);

	//kinect工作
	while (1) {
		//直到获取到最后一个框架，即框架更新了，进行下一步操作
		while (myColorReader->AcquireLatestFrame(&myColorFrame) != S_OK);
		//将kinect的颜色框架数据加载进一个
		myColorFrame->CopyConvertedFrameDataToArray(colorHeight * colorWidth * 4, original.data, ColorImageFormat_Bgra);
		
		Mat copy = original.clone();

		while (myBodyReader->AcquireLatestFrame(&myBodyFrame) != S_OK);
		//建立个body数组，表示检测到到的每个body
		IBody ** myBodyArr = new IBody *[myBodyCount];
		for (int i = 0; i < myBodyCount; i++)
			myBodyArr[i] = nullptr;

		//如果body的数据刷新
		if(myBodyFrame->GetAndRefreshBodyData(myBodyCount,myBodyArr) == S_OK)
		//	std::cout << "捕捉到body更新！\n"<<myBodyCount;

			for (int i = 0; i < myBodyCount; i++)
			{
				
				BOOLEAN tracked = false;//捕捉标记
				myBodyArr[i]->get_IsTracked(&tracked);
				if ( tracked) {
				//	std::cout << "捕捉到！\n";
					//关节点信息数组
					Joint myJointArr[JointType_Count];
					
					if (myBodyArr[i]->GetJoints(JointType_Count, myJointArr) == S_OK)
					{
						std::cout << "捕捉到更新！\n";
						for(int i = 0;i<JointType_Count;i++)
							handle_Joint(myJointArr[i]);

						//在背景图中绘制骨骼点和骨架图
						draw(copy, myJointArr[JointType_Head], myJointArr[JointType_Neck], myMapper);
						draw(copy, myJointArr[JointType_Neck], myJointArr[JointType_SpineShoulder], myMapper);

						draw(copy, myJointArr[JointType_SpineShoulder], myJointArr[JointType_ShoulderLeft], myMapper);
						draw(copy, myJointArr[JointType_SpineShoulder], myJointArr[JointType_SpineMid], myMapper);
						draw(copy, myJointArr[JointType_SpineShoulder], myJointArr[JointType_ShoulderRight], myMapper);

						draw(copy, myJointArr[JointType_ShoulderLeft], myJointArr[JointType_ElbowLeft], myMapper);
						draw(copy, myJointArr[JointType_SpineMid], myJointArr[JointType_SpineBase], myMapper);
						draw(copy, myJointArr[JointType_ShoulderRight], myJointArr[JointType_ElbowRight], myMapper);

						draw(copy, myJointArr[JointType_ElbowLeft], myJointArr[JointType_WristLeft], myMapper);
						draw(copy, myJointArr[JointType_SpineBase], myJointArr[JointType_HipLeft], myMapper);
						draw(copy, myJointArr[JointType_SpineBase], myJointArr[JointType_HipRight], myMapper);
						draw(copy, myJointArr[JointType_ElbowRight], myJointArr[JointType_WristRight], myMapper);

						draw(copy, myJointArr[JointType_WristLeft], myJointArr[JointType_ThumbLeft], myMapper);
						draw(copy, myJointArr[JointType_WristLeft], myJointArr[JointType_HandLeft], myMapper);
						draw(copy, myJointArr[JointType_HipLeft], myJointArr[JointType_KneeLeft], myMapper);
						draw(copy, myJointArr[JointType_HipRight], myJointArr[JointType_KneeRight], myMapper);
						draw(copy, myJointArr[JointType_WristRight], myJointArr[JointType_ThumbRight], myMapper);
						draw(copy, myJointArr[JointType_WristRight], myJointArr[JointType_HandRight], myMapper);

						draw(copy, myJointArr[JointType_HandLeft], myJointArr[JointType_HandTipLeft], myMapper);
						draw(copy, myJointArr[JointType_KneeLeft], myJointArr[JointType_FootLeft], myMapper);
						draw(copy, myJointArr[JointType_KneeRight], myJointArr[JointType_FootRight], myMapper);
						draw(copy, myJointArr[JointType_HandRight], myJointArr[JointType_HandTipRight], myMapper);
					}
				}
			}
	
		delete[]myBodyArr;
		myBodyFrame->Release();
		myColorFrame->Release();
		imshow("Kinect_body", copy);
		if (waitKey(30) == VK_ESCAPE)
			break;
	}
	myDescription->Release();
	myColorReader->Release();
	myColorSource->Release();

	myBodyReader->Release();
	myBodySource->Release();
	myKinectSensor->Close();
	myKinectSensor->Release();


    return 0;
}

