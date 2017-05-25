import datetime
import cv2

show_video = True
video = "video.avi"
porcent = 10

def format_time (seconds):
    return str(datetime.timedelta(seconds=int(seconds)))

def diffImg (t0, t1, t2):
    d1 = cv2.absdiff(t2, t1)
    d2 = cv2.absdiff(t1, t0)
    return cv2.bitwise_and(d1, d2)

def moved (frame, size, porcent):
    if cv2.countNonZero(frame) > (size * porcent / 100):
        return True
    return False

if __name__ == "__main__":
    cap    = cv2.VideoCapture(video)
    fps    = cap.get(cv2.cv.CV_CAP_PROP_FPS)
    size   = cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH) * cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
    count_frame = 0
    last_time = ''

    t_minus = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)
    t       = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)
    t_plus  = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)

    while True:
        count_frame += 1
        frame = diffImg(t_minus, t, t_plus)
        current_time = format_time(count_frame/fps)

        if moved(frame, size, porcent) and last_time != current_time:
            last_time = current_time
            print current_time

        if show_video:
            text = "%s" % (current_time)#, width, height)
            cv2.putText(frame, text, (10, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 255)
            cv2.imshow("movimento", frame)

        t_minus = t
        t       = t_plus
        t_plus  = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)

        if cv2.waitKey(10) == 27: break

    cap.release()
    cv2.destroyAllWindows()
