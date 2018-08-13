#pragma once


#include "stdafx.h"
#include <QtWidgets/QMainWindow>
#include "ui_Kinect_App.h"
#include <QPaintEvent>
#include <QTimer>
#include <QPainter>
#include <QPixmap>
#include <QLabel>
#include <QImage>
#include <QDebug>
#include<iostream>
#include<opencv2/opencv.hpp>
#include<opencv2/imgproc.hpp>
#include<opencv2/calib3d.hpp>
#include<opencv2/highgui.hpp>
#include<math.h>
#include<Kinect.h>



using namespace std;
using namespace cv;

class Kinect_App : public QMainWindow
{
	Q_OBJECT

public:
	Kinect_App(QWidget *parent = Q_NULLPTR);
	~Kinect_App();
	//���ƹ�������
	void draw(Mat & img, Joint & joint_1, Joint & joint_2, ICoordinateMapper * myMapper);
	//����������ݵļ�demo
	bool handle_Joint(Joint & joint);
	//���������ؽڵĳ���
	double cal_length(Joint & joint_1, Joint & joint_2);

private slots:
	//��kinect�л�ȡ֡�ĺ�������timer����һ��timerÿ50ms��ʱһ�Σ������������������matתΪQimage�ŵ�label_2��
	void getFrame();

private:
	Ui::Kinect_AppClass ui;
	QImage *imag;
	CvCapture *capture;//highgui���ṩ��һ��ר�Ŵ�������ͷͼ��Ľṹ��
	IplImage *frame;//����ͷÿ��ץȡ��ͼ��Ϊһ֡��ʹ�ø�ָ��ָ��һ֡ͼ����ڴ�ռ�
	QTimer *timer;//��ʱ�����ڶ�ʱȡ֡������˵�ĸ�һ��ʱ���ȥȡ���������ʵ��
	
	//init kinect param
	//����Color��Body��Source,Reader,Frame
	IKinectSensor * myKinectSensor;
	IColorFrameSource * myColorSource;
	IColorFrameReader * myColorReader;
	IColorFrame * myColorFrame;
	int colorHeight, colorWidth;

	IBodyFrameSource * myBodySource;
	IBodyFrameReader * myBodyReader;
	IBodyFrame * myBodyFrame;

	
	IFrameDescription * myDescription;
	Mat original;
	int myBodyCount;
	ICoordinateMapper * myMapper;

};
