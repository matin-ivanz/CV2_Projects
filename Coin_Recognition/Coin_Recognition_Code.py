import cv2

# upload a photo and adjust the size and color
image = cv2.imread("CV2_Projects/Coin_Recognition/Photos/Photo_of_coins.png")
image_resized = cv2.resize(image, None, fx=0.4, fy=0.4)
raw_image = image_resized.copy()
image_gray = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)

# photo filtering
image_blur = cv2.medianBlur(image_gray, 7)

# apply binary threshold
ret, thresh = cv2.threshold(image_blur, 70, 255,
                            cv2.THRESH_BINARY)

# detect external contours (coins)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)
image_drawn = cv2.drawContours(image_resized, contours, -1,
                               (0, 255, 0), 2)

# calculating the area and writing it on the photo
for cnt in contours:
    m = cv2.moments(cnt)
    area = str(int(cv2.contourArea(cnt)))

    x, y, w, h = cv2.boundingRect(cnt)
    cy = int(m["m01"] / m["m00"]) + 30

    cv2.putText(image_drawn, area,
                (x - 50, cy),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0),
                1)

cv2.imshow("Original", raw_image)
cv2.imshow("Grayscale", image_gray)
cv2.imshow("Blurred", image_blur)
cv2.imshow("Binary Threshold", thresh)
cv2.imshow("Detected Coins", image_drawn)

cv2.waitKey(0)
cv2.destroyAllWindows()
