## Introduction

The code points to an IP address that you must change to match the IP and port for the video feed on your local area network.

This feed used the free Android app: IP Webcam

The app will broadcast a video feed over the network (via a router, or phone's hotspot). The stream will be in MJPEG format, which is what the code is built to expect.

## Concepts

Countour detection is done on a frame by frame basis. The frames are just image files, extracted from a video feed. The feed could be any video format (or image repository),
as long as you arrive at an image file representing one frame, to be processed.

The contour detection works on a grayscaled version of an RGB image.