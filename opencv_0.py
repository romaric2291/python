import cv2

def display_picture(name):
    picture = cv2.imread(name)
    picture = cv2.resize(picture, (picture.shape[1]/4,picture.shape[0]/4))
    cv2.imshow("My picture", picture)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def display_picture_bw(name):
    picture = cv2.imread(name,0)
    picture = cv2.resize(picture, (picture.shape[1]/4,picture.shape[0]/4))
    cv2.imshow("My picture", picture)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
    
if __name__ == "__main__":
    #display_picture("malta.jpg")
    display_picture_bw("malta.jpg")