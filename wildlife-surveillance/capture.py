import cv2

def capture_image(output_file="output.jpg"):
    # GStreamer pipeline for CSI camera
    gst_pipeline = (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), width=1280, height=720, format=NV12, framerate=30/1 ! "
        "nvjpegenc ! "
        "appsink"
    )

    cap = cv2.VideoCapture(gst_pipeline, cv2.CAP_GSTREAMER)

    if not cap.isOpened():
        print("Failed to open camera.")
        return

    ret, frame = cap.read()
    if ret:
        cv2.imwrite(output_file, frame)
        print(f"Image saved to {output_file}")
    else:
        print("Failed to capture image.")

    cap.release()

if __name__ == "__main__":
    capture_image("photo.jpg")
