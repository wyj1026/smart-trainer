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
	//绘制骨骼函数
	void draw(Mat & img, Joint & joint_1, Joint & joint_2, ICoordinateMapper * myMapper);
	//处理骨骼数据的简单demo
	bool handle_Joint(Joint & joint);
	//计算两个关节的长度
	double cal_length(Joint & joint_1, Joint & joint_2);

private slots:
	//从kinect中获取帧的函数，与timer连在一起，timer每50ms超时一次，调用这个函数，并将mat转为Qimage放到label_2中
	void getFrame();

private:
	Ui::Kinect_AppClass ui;
	QImage *imag;
	CvCapture *capture;//highgui里提供的一个专门处理摄像头图像的结构体
	IplImage *frame;//摄像头每次抓取的图像为一帧，使用该指针指向一帧图像的内存空间
	QTimer *timer;//定时器用于定时取帧，上面说的隔一段时间就去取就是用这个实现
	
	//init kinect param
	//包括Color和Body的Source,Reader,Frame
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
