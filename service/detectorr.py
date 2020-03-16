import cv2
import matplotlib


def detection():
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    # params.minThreshold = 150;
    # params.maxThreshold = 255;

    # Filter by Area.
    params.filterByArea = True
    params.minArea = 2500

    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = .6

    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = .6

    # Filter by Inertia
    params.filterByInertia = True
    params.minInertiaRatio = .5

    # Create a detector with the parameters
    ver = (cv2.__version__).split('.')
    if int(ver[0]) < 3:
        detector = cv2.SimpleBlobDetector(params)
    else:
        detector = cv2.SimpleBlobDetector_create(params)

    return detector
