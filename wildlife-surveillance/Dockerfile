FROM nvcr.io/nvidia/l4t-base:r32.6.1

ENV DEBIAN_FRONTEND=noninteractive

# Install Python and OpenCV
RUN apt-get update && apt-get install -y \
    python3-pip python3-dev python3-opencv \
    libopencv-dev libgstreamer1.0-dev \
    libgstreamer-plugins-base1.0-dev \
    gstreamer1.0-tools \
    && apt-get clean

# Set Python 3 as default
RUN ln -sf /usr/bin/python3 /usr/bin/python

# Copy the script into the container
COPY capture.py /app/capture.py
WORKDIR /app

CMD ["python", "capture.py"]
