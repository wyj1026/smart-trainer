#include "Kinect_App.h"

//���캯��
Kinect_App::Kinect_App(QWidget *parent)
	: QMainWindow(parent)
{
	ui.setupUi(this);
	timer = new QTimer(this);
	imag = new QImage();

	//init kinectsensor
	myKinectSensor = nullptr;
	GetDefaultKinectSensor(&myKinectSensor);
	myKinectSensor->Open();

	//init ColorFrame :Source Reader
	myColorSource = nullptr;
	myKinectSensor->get_ColorFrameSource(&myColorSource);
	
	myColorReader = nullptr;
	myColorSource->OpenReader(&myColorReader);

	colorHeight = 0, colorWidth = 0;

	//init BodyFrame :Source  Reader
	myBodySource = nullptr;
	myKinectSensor->get_BodyFrameSource(&myBodySource);
	myBodyReader = nullptr;
	myBodySource->OpenReader(&myBodyReader);

	myBodyFrame = nullptr;

	myBodyCount = 0;
	myBodySource->get_BodyCount(&myBodyCount);


	//��kinect�еõ������һ���������߿�
	myDescription = nullptr;
	myColorSource->get_FrameDescription(&myDescription);
	myDescription->get_Height(&colorHeight);
	myDescription->get_Width(&colorWidth);

	myColorFrame = nullptr;
	original = Mat(colorHeight, colorWidth, CV_8UC4);

	
	//�����׼��ͼ
	myMapper = nullptr;
	myKinectSensor->get_CoordinateMapper(&myMapper);
	
	//�����źźͲۺ���
	connect(timer, SIGNAL(timeout()), this, SLOT(getFrame()));//��ʱ�Ͷ�ȡ��ǰ����ͷ��Ϣ
	
	//��Ϊ��û�����ÿ�ʼ��ť֮����źţ������ڹ��캯���п�ʼtimer�ļ�ʱ����������
	timer->start(50);
}

//��������
Kinect_App::~Kinect_App() {
	delete &ui;

	myDescription->Release();
	myColorReader->Release();
	myColorSource->Release();

	myBodyReader->Release();
	myBodySource->Release();
	myKinectSensor->Close();
	myKinectSensor->Release();
}

void Kinect_App::getFrame()
{
	while (true)
	{
		//ֱ����ȡ�����һ����ܣ�����ܸ����ˣ�������һ������
		while (myColorReader->AcquireLatestFrame(&myColorFrame) != S_OK);
		//��kinect����ɫ������ݼ��ؽ�һ��
		myColorFrame->CopyConvertedFrameDataToArray(colorHeight * colorWidth * 4, original.data, ColorImageFormat_Bgra);

		Mat copy = original.clone();

		while (myBodyReader->AcquireLatestFrame(&myBodyFrame) != S_OK);
		//������body���飬��ʾ��⵽����ÿ��body
		IBody ** myBodyArr = new IBody *[myBodyCount];
		for (int i = 0; i < myBodyCount; i++)
			myBodyArr[i] = nullptr;

		//���body������ˢ��
		if (myBodyFrame->GetAndRefreshBodyData(myBodyCount, myBodyArr) == S_OK)
			//	std::cout << "��׽��body���£�\n"<<myBodyCount;

			for (int i = 0; i < myBodyCount; i++)
			{

				BOOLEAN tracked = false;//��׽���
				myBodyArr[i]->get_IsTracked(&tracked);
				if (tracked) {
					//	std::cout << "��׽����\n";
					//�ؽڵ���Ϣ����
					Joint myJointArr[JointType_Count];

					if (myBodyArr[i]->GetJoints(JointType_Count, myJointArr) == S_OK)
					{
						std::cout << "��׽�����£�\n";
						for (int i = 0; i<JointType_Count; i++)

						//�ڱ���ͼ�л��ƹ�����͹Ǽ�ͼ
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
		
		//��mat��ʽ��ͼƬתΪqimage �ŵ�label_2��
		Mat Rgb;
		QImage Img;
		if (copy.channels() == 3)//RGB Img
		{
			cout << "color";
			cv::cvtColor(copy, Rgb, CV_BGR2RGB);//��ɫ�ռ�ת��
			Img = QImage((const uchar*)(Rgb.data), Rgb.cols, Rgb.rows, Rgb.cols * Rgb.channels(), QImage::Format_RGB888);
		}
		else//Gray Img
		{
			cout << "grey";
			Img = QImage((const uchar*)(copy.data), copy.cols, copy.rows, copy.cols*copy.channels(), QImage::Format_ARGB32);
		}
		Img = Img.scaled(ui.label_2->width(), ui.label_2->height());
		ui.label_2->setPixmap((QPixmap::fromImage(Img)));
		break;
	}
	
}


void Kinect_App::draw(Mat & img, Joint & joint_1, Joint & joint_2, ICoordinateMapper * myMapper) {
	//���jonit_1 �� joint_2����׽��
	if (joint_1.TrackingState == TrackingState_Tracked && joint_2.TrackingState == TrackingState_Tracked) {
		ColorSpacePoint joint_color;
		Point point_1, point_2;
		//��joint_1����joint_color
		myMapper->MapCameraPointToColorSpace(joint_1.Position, &joint_color);
		point_1.x = joint_color.X;
		point_1.y = joint_color.Y;
		//��joint_2����joint_color
		myMapper->MapCameraPointToColorSpace(joint_2.Position, &joint_color);
		point_2.x = joint_color.X;
		point_2.y = joint_color.Y;
		//����
		line(img, point_1, point_2, Vec3b(0, 255, 0), 5);
		//��Ȧ
		circle(img, point_1, 10, Vec3b(255, 0, 0), -1);
		circle(img, point_2, 10, Vec3b(255, 0, 0), -1);
	}
}

//��ȡ�����ؽڵ���Ϣ��demo
bool Kinect_App::handle_Joint(Joint & joint) {
	//���joint���ؽڵ㣩����׽	
	if (joint.TrackingState == TrackingState_Tracked) {
		std::cout << "�ؽڵ�����Ϊ:" << joint.JointType << std::endl;
		std::cout << "�ؽڵ���ά����Ϊ(x,y,z):" << joint.Position.X << " " << joint.Position.Y << " " << joint.Position.Z << std::endl << std::endl << std::endl;
		return true;
	}
	return false;
}

//���������ؽڵ�֮��ľ���
double Kinect_App::cal_length(Joint & joint_1, Joint & joint_2) {
	if (joint_1.TrackingState == TrackingState_Tracked && joint_2.TrackingState == TrackingState_Tracked)
		return sqrt(pow(abs(joint_1.Position.X - joint_2.Position.X), 2) + pow(abs(joint_1.Position.Y - joint_2.Position.Y), 2) + pow(abs(joint_1.Position.Z - joint_2.Position.Z), 2));
	else
		return 0;
}