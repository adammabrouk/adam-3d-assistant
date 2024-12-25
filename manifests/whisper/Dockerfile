# Use an official Ubuntu as a parent image
FROM ubuntu:20.04

# Set environment variables to non-interactive
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && \
    apt-get install -y \
    git \
    build-essential \
    cmake \
    ffmpeg \
    libfftw3-dev \
    libsndfile1-dev \
    && rm -rf /var/lib/apt/lists/*

# Clone the whisper.cpp repository
RUN git clone https://github.com/ggerganov/whisper.cpp.git /whisper

# Build whisper.cpp
WORKDIR /whisper
RUN mkdir build && cd build && cmake .. && make

VOLUME [ "/whisper/mountedmodels" ]

# Set the entrypoint
ENTRYPOINT ["/whisper/build/bin/whisper-server"]