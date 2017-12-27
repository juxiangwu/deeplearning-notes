import QtQuick 2.6
import QtQuick.Window 2.2
import QtQuick.Controls 1.4
Rectangle {
    width: 640
    height: 480   //这里一定要加个大小 不然打开的窗口太小什么都看不到 很不方便
    Label {
        id: label
        x: 204
        y: 74
        width: 232
        height: 39
        text: qsTr("验证码识别")
        font.pointSize: 26
        textFormat: Text.AutoText
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
    }
    Image {
        id: image
        x: 220
        y: 143
        width: 200
        height: 100
        //source: "../../../../../datas/app/images/resources/images/clock.png"
    }
    Button {
        id: button
        x: 165
        y: 352
        text: qsTr("开始")
    }
    Button {
        id: button1
        x: 399
        y: 352
        text: qsTr("关闭")
    }
    TextField {
        id: textField
        x: 204
        y: 267
        width: 232
        height: 20
        placeholderText: qsTr("Text Field")
    }
    Label {
        id: label1
        x: 132
        y: 271
        width: 51
        height: 10
        text: qsTr("结果")
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
    }
    }