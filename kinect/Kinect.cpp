// Kinect.cpp: 定义控制台应用程序的入口点。
//
#include "stdafx.h"
#include<iostream>



bool handle_Joint(Joint & joint) {
	//如果joint（关节点）被捕捉	
	if (joint.TrackingState == TrackingState_Tracked) {
		std::cout << "关节点类型为:" << joint.JointType << std::endl;
		std::cout << "关节点三维坐标为(x,y,z):" << joint.Position.X <<" "<< joint.Position.Y << " " << joint.Position.Z <<std::endl<< std::endl<< std::endl;
		return true;
	}
	return false;
}


int main()
{	
	//init kinectsensor;
	IKinectSensor * myKinectSensor = nullptr;
	GetDefaultKinectSensor(&myKinectSensor);
	myKinectSensor->Open();

	//init BodyFrame :Source  Reader
	IBodyFrameSource * myBodySource = nullptr;
	myKinectSensor->get_BodyFrameSource(&myBodySource);

	IBodyFrameReader * myBodyReader = nullptr;
	myBodySource->OpenReader(&myBodyReader);

	IBodyFrame * myBodyFrame = nullptr;

	int myBodyCount = 0;
	myBodySource->get_BodyCount(&myBodyCount);


	//kinect工作
	while (1) {
		//直到获取到最后一个框架，即框架更新了，进行下一步操作
		while (myBodyReader->AcquireLatestFrame(&myBodyFrame) != S_OK);
		//建立个body数组，表示检测到到的每个body
		IBody ** myBodyArr = new IBody *[myBodyCount];
		for (int i = 0; i < myBodyCount; i++)
			myBodyArr[i] = nullptr;

		//如果body的数据刷新
		if(myBodyFrame->GetAndRefreshBodyData(myBodyCount,myBodyArr) == S_OK)
			std::cout << "捕捉到body更新！\n"<<myBodyCount;

			for (int i = 0; i < myBodyCount; i++)
			{
				
				BOOLEAN tracked = false;//捕捉标记
				myBodyArr[i]->get_IsTracked(&tracked);
				if ( tracked) {
					std::cout << "捕捉到！\n";
					//关节点信息数组
					Joint myJointArr[JointType_Count];
					
					if (myBodyArr[i]->GetJoints(JointType_Count, myJointArr) == S_OK)
					{
						std::cout << "捕捉到更新！\n";
						for (int i = 0; i < JointType_Count; i++)
							handle_Joint(myJointArr[i]);
					}
				}
			}
	
		delete[]myBodyArr;
		myBodyFrame->Release();

		Sleep(1000);
	}

    return 0;
}

