# How to run the Dockerfile

docker run \
-v /home/blackhawk/whisper.cpp/models:/whisper/mountedmodels -p 8080:8080 stt-whisper \
-l fr -m /whisper/mountedmodels/ggml-base.bin --host 0.0.0.0 

