#include"Kinect_App.h"
#include<QtWidgets/QApplication>
#include<Python.h>
#include<iostream>
#include<stdafx.h>

using namespace std;

int main(int argc, char *argv[])
{
	QApplication a(argc, argv);
	Kinect_App w;
	
	w.show();
	return a.exec();

	//domo of python
	//cout << "hello Python!" << endl;
	//cout << "123" << endl;
	//Py_Initialize();
	////添加python工作目录
	//PyRun_SimpleString("import sys");
	//PyRun_SimpleString("sys.path.append('C:/Users/Richado/Desktop/smart-trainer/Kinect_App/')");
	//PyRun_SimpleString("sys.path.append('C:/Users/Richado/Desktop/smart-trainer/')");

	//PyObject * pMoudle = NULL;
	//PyObject * pFunc = NULL;
	//pMoudle = PyImport_ImportModule("hello");
	//pFunc = PyObject_GetAttrString(pMoudle, "hello");
	//PyRun_SimpleString("import matplotlib.pyplot as plt");
	//PyRun_SimpleString("plt.plot(range(5))");
	//PyRun_SimpleString("plt.show()");
	//PyEval_CallObject(pFunc, NULL);
	//Py_Finalize();
	//system("pause");
	//return 0;
}
