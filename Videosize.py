import sys
import cv2

def Videosize(filepath, savename):
    cap = cv2.VideoCapture(filepath)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(savename, fourcc, 25.0, (int(cap.get(3)),int(cap.get(4))))

    while(cap.isOpened()):
        ret, frame = cap.read()
	
        if ret:
    	
            out.write(frame)
    	
            cv2.imshow('frame', frame)
    	
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

Videosize(sys.argv[1], sys.argv[2])
