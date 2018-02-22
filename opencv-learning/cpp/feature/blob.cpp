#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;
int main()
{

    // Read image
    Mat im = imread( "D:/Develop/DL/deeplearning-notes/temp/images/blox.jpg", IMREAD_GRAYSCALE );
    // Set up the detector with default parameters.
//    SimpleBlobDetector detector;
//    // Detect blobs.
    std::vector<KeyPoint> keypoints;
//    detector.detect( im, keypoints);
    cv::Ptr<cv::SimpleBlobDetector> detector = cv::SimpleBlobDetector::create();
    detector->detect( im, keypoints );
    // Draw detected blobs as red circles.
    // DrawMatchesFlags::DRAW_RICH_KEYPOINTS flag ensures the size of the circle corresponds to the size of blob
    Mat im_with_keypoints;
    drawKeypoints( im, keypoints, im_with_keypoints, Scalar(0,0,255), DrawMatchesFlags::DRAW_RICH_KEYPOINTS );
    // Show blobs
    imshow("keypoints", im_with_keypoints );
    waitKey(0);
}
