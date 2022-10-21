# -- coding: utf-8 --
import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        m = cv2.medianBlur(gray, 5)
        canny = cv2.Canny(gray, 50, 100)
        cv2.imshow('03', canny)
        cv2.imshow('04', m)
        # # Преобразование Хафа - классический алгоритм обнаружения прямых линий.
        # lines = cv2.HoughLinesP(canny, 1, np.pi / 180, 30, minLineLength=30, maxLineGap=10)
        # lines = lines[:, 0, :]
        # for x1, y1, x2, y2 in lines:
        #      cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        rows = canny.shape[0]
        circles = cv2.HoughCircles(m, cv2.HOUGH_GRADIENT, 1, rows / 8,
                                  param1=100, param2=30,
                                  minRadius=1, maxRadius=30)



        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                center = (i[0], i[1])
                # circle center
                cv2.circle(img, center, 1, (0, 100, 100), 3)
                # circle outline
                radius = i[2]
                cv2.circle(img, center, radius, (255, 0, 255), 3)

        cv2.imshow('img0', img)
        cv2.imshow('img1', gray)
        key = cv2.waitKey(1)

        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()