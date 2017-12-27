import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.2

ApplicationWindow {
    visible: true
    width: 640
    height: 240
    title: qsTr("PyQt5 love QML")
    color: "whitesmoke"

    GridLayout {
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.margins: 9

        columns: 4
        rows: 4
        rowSpacing: 10
        columnSpacing: 10

        Text {
            text: qsTr("First number")
        }

        // Input field of the first number
        TextField {
            id: firstNumber
        }

        Text {
            text: qsTr("Second number")
        }

        // Input field of the second number
        TextField {
            id: secondNumber
        }

        Button {
            height: 40
            Layout.fillWidth: true
            text: qsTr("Sum numbers")

            Layout.columnSpan: 2

            onClicked: {
                // Invoke the calculator slot to sum the numbers
                calculator.sum(firstNumber.text, secondNumber.text)
            }
        }

        Text {
            text: qsTr("Result")
        }

        // Here we see the result of sum
        Text {
            id: sumResult
        }

        Button {
            height: 40
            Layout.fillWidth: true
            text: qsTr("Subtraction numbers")

            Layout.columnSpan: 2

            onClicked: {
                // Invoke the calculator slot to subtract the numbers
                calculator.sub(firstNumber.text, secondNumber.text)
            }
        }

        Text {
            text: qsTr("Result")
        }

        // Here we see the result of subtraction
        Text {
            id: subResult
        }
    }

    // Here we take the result of sum or subtracting numbers
    Connections {
        target: calculator

        // Sum signal handler
        onSumResult: {
            // sum was set through arguments=['sum']
            sumResult.text = sum
        }

        // Subtraction signal handler
        onSubResult: {
            // sub was set through arguments=['sub']
            subResult.text = sub
        }
    }
}