import cv2

# Read the image
img = cv2.imread("image1.png")

# Convert image into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
cv2.imshow("Grayscale Image", gray)

# Save the grayscale image
cv2.imwrite("gray_image1.png", gray)

# Wait and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()