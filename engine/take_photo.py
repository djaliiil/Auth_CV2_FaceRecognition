import cv2, os


def take_photo(name):
    """
    Take photo from Camera and save it
    """
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Camera")

    while True:
        ret, frame = cam.read()
        cv2.imshow("Camera", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = str(name) + ".png"
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            break

    cam.release()
    cv2.destroyAllWindows()

    return img_name


if __name__ == '__main__':
    img = take_photo()
