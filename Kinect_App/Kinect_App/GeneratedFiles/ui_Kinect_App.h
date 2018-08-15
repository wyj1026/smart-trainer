/********************************************************************************
** Form generated from reading UI file 'Kinect_App.ui'
**
** Created by: Qt User Interface Compiler version 5.9.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_KINECT_APP_H
#define UI_KINECT_APP_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QTextBrowser>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Kinect_AppClass
{
public:
    QWidget *centralwidget;
    QHBoxLayout *horizontalLayout;
    QFrame *line_6;
    QVBoxLayout *verticalLayout;
    QFrame *line_4;
    QLabel *label_2;
    QFrame *line_5;
    QFrame *line;
    QVBoxLayout *verticalLayout_3;
    QFrame *line_7;
    QLabel *label;
    QFrame *line_3;
    QFormLayout *formLayout;
    QLabel *label_3;
    QLabel *label_6;
    QLabel *label_4;
    QLabel *label_7;
    QLabel *label_5;
    QTextBrowser *textBrowser;
    QFrame *line_9;
    QFrame *line_10;
    QFrame *line_2;
    QLabel *label_8;
    QFrame *line_8;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(1258, 1000);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QStringLiteral("centralwidget"));
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(centralwidget->sizePolicy().hasHeightForWidth());
        centralwidget->setSizePolicy(sizePolicy);
        centralwidget->setMinimumSize(QSize(1000, 1000));
        horizontalLayout = new QHBoxLayout(centralwidget);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        line_6 = new QFrame(centralwidget);
        line_6->setObjectName(QStringLiteral("line_6"));
        line_6->setFrameShape(QFrame::VLine);
        line_6->setFrameShadow(QFrame::Sunken);

        horizontalLayout->addWidget(line_6);

        verticalLayout = new QVBoxLayout();
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        line_4 = new QFrame(centralwidget);
        line_4->setObjectName(QStringLiteral("line_4"));
        line_4->setFrameShape(QFrame::HLine);
        line_4->setFrameShadow(QFrame::Sunken);

        verticalLayout->addWidget(line_4);

        label_2 = new QLabel(centralwidget);
        label_2->setObjectName(QStringLiteral("label_2"));
        sizePolicy.setHeightForWidth(label_2->sizePolicy().hasHeightForWidth());
        label_2->setSizePolicy(sizePolicy);

        verticalLayout->addWidget(label_2);

        line_5 = new QFrame(centralwidget);
        line_5->setObjectName(QStringLiteral("line_5"));
        line_5->setFrameShape(QFrame::HLine);
        line_5->setFrameShadow(QFrame::Sunken);

        verticalLayout->addWidget(line_5);


        horizontalLayout->addLayout(verticalLayout);

        line = new QFrame(centralwidget);
        line->setObjectName(QStringLiteral("line"));
        line->setFrameShape(QFrame::VLine);
        line->setFrameShadow(QFrame::Sunken);

        horizontalLayout->addWidget(line);

        verticalLayout_3 = new QVBoxLayout();
        verticalLayout_3->setObjectName(QStringLiteral("verticalLayout_3"));
        verticalLayout_3->setSizeConstraint(QLayout::SetMinAndMaxSize);
        line_7 = new QFrame(centralwidget);
        line_7->setObjectName(QStringLiteral("line_7"));
        line_7->setFrameShape(QFrame::HLine);
        line_7->setFrameShadow(QFrame::Sunken);

        verticalLayout_3->addWidget(line_7);

        label = new QLabel(centralwidget);
        label->setObjectName(QStringLiteral("label"));
        label->setMinimumSize(QSize(0, 100));
        label->setMaximumSize(QSize(16777215, 100));
        QFont font;
        font.setPointSize(12);
        font.setBold(true);
        font.setWeight(75);
        label->setFont(font);
        label->setAlignment(Qt::AlignCenter);

        verticalLayout_3->addWidget(label);

        line_3 = new QFrame(centralwidget);
        line_3->setObjectName(QStringLiteral("line_3"));
        line_3->setFrameShape(QFrame::HLine);
        line_3->setFrameShadow(QFrame::Sunken);

        verticalLayout_3->addWidget(line_3);

        formLayout = new QFormLayout();
        formLayout->setObjectName(QStringLiteral("formLayout"));
        label_3 = new QLabel(centralwidget);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setMinimumSize(QSize(0, 100));
        QFont font1;
        font1.setPointSize(13);
        font1.setItalic(false);
        font1.setStrikeOut(false);
        label_3->setFont(font1);
        label_3->setAlignment(Qt::AlignCenter);
        label_3->setMargin(10);

        formLayout->setWidget(0, QFormLayout::LabelRole, label_3);

        label_6 = new QLabel(centralwidget);
        label_6->setObjectName(QStringLiteral("label_6"));
        QFont font2;
        font2.setPointSize(14);
        font2.setBold(true);
        font2.setWeight(75);
        label_6->setFont(font2);
        label_6->setAlignment(Qt::AlignCenter);

        formLayout->setWidget(0, QFormLayout::FieldRole, label_6);

        label_4 = new QLabel(centralwidget);
        label_4->setObjectName(QStringLiteral("label_4"));
        label_4->setMinimumSize(QSize(0, 100));
        QFont font3;
        font3.setPointSize(13);
        label_4->setFont(font3);
        label_4->setMargin(10);

        formLayout->setWidget(2, QFormLayout::LabelRole, label_4);

        label_7 = new QLabel(centralwidget);
        label_7->setObjectName(QStringLiteral("label_7"));
        label_7->setFont(font2);
        label_7->setAlignment(Qt::AlignCenter);

        formLayout->setWidget(2, QFormLayout::FieldRole, label_7);

        label_5 = new QLabel(centralwidget);
        label_5->setObjectName(QStringLiteral("label_5"));
        label_5->setMinimumSize(QSize(0, 100));
        label_5->setFont(font3);
        label_5->setMargin(10);

        formLayout->setWidget(4, QFormLayout::LabelRole, label_5);

        textBrowser = new QTextBrowser(centralwidget);
        textBrowser->setObjectName(QStringLiteral("textBrowser"));

        formLayout->setWidget(5, QFormLayout::SpanningRole, textBrowser);

        line_9 = new QFrame(centralwidget);
        line_9->setObjectName(QStringLiteral("line_9"));
        line_9->setFrameShape(QFrame::HLine);
        line_9->setFrameShadow(QFrame::Sunken);

        formLayout->setWidget(3, QFormLayout::LabelRole, line_9);

        line_10 = new QFrame(centralwidget);
        line_10->setObjectName(QStringLiteral("line_10"));
        line_10->setFrameShape(QFrame::HLine);
        line_10->setFrameShadow(QFrame::Sunken);

        formLayout->setWidget(1, QFormLayout::LabelRole, line_10);


        verticalLayout_3->addLayout(formLayout);

        line_2 = new QFrame(centralwidget);
        line_2->setObjectName(QStringLiteral("line_2"));
        line_2->setFrameShape(QFrame::HLine);
        line_2->setFrameShadow(QFrame::Sunken);

        verticalLayout_3->addWidget(line_2);

        label_8 = new QLabel(centralwidget);
        label_8->setObjectName(QStringLiteral("label_8"));
        label_8->setMinimumSize(QSize(0, 60));
        label_8->setAlignment(Qt::AlignCenter);

        verticalLayout_3->addWidget(label_8);

        line_8 = new QFrame(centralwidget);
        line_8->setObjectName(QStringLiteral("line_8"));
        line_8->setFrameShape(QFrame::HLine);
        line_8->setFrameShadow(QFrame::Sunken);

        verticalLayout_3->addWidget(line_8);


        horizontalLayout->addLayout(verticalLayout_3);

        horizontalLayout->setStretch(1, 3);
        horizontalLayout->setStretch(3, 1);
        MainWindow->setCentralWidget(centralwidget);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("Kinect_AppClass", "Raindar", Q_NULLPTR));
        label_2->setText(QApplication::translate("Kinect_AppClass", "Viedo                                                                             ", Q_NULLPTR));
        label->setText(QApplication::translate("Kinect_AppClass", "Smart Trainer V1.0", Q_NULLPTR));
        label_3->setText(QApplication::translate("Kinect_AppClass", "\345\275\223\345\211\215\345\212\250\344\275\234\357\274\232", Q_NULLPTR));
        label_6->setText(QApplication::translate("Kinect_AppClass", "None", Q_NULLPTR));
        label_4->setText(QApplication::translate("Kinect_AppClass", "\350\257\204\344\274\260\345\210\206\345\200\274\357\274\232", Q_NULLPTR));
        label_7->setText(QApplication::translate("Kinect_AppClass", "99", Q_NULLPTR));
        label_5->setText(QApplication::translate("Kinect_AppClass", "\345\212\250\344\275\234\345\273\272\350\256\256\357\274\232", Q_NULLPTR));
        textBrowser->setHtml(QApplication::translate("Kinect_AppClass", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Test Text</p></body></html>", Q_NULLPTR));
        label_8->setText(QApplication::translate("Kinect_AppClass", "2018.8.6 SmartTrainer V1.0", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class Kinect_AppClass: public Ui_Kinect_AppClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_KINECT_APP_H
