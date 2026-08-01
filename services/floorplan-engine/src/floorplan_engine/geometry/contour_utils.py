import cv2


class ContourUtils:

    @staticmethod
    def find(binary_image):

        contours, _ = cv2.findContours(
            binary_image,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE,
        )

        return contours