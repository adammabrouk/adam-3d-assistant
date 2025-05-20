## Project Overview

This project is a homelab setup with k3s deployed, and various components including a 3D assistant in three.js, openvoice os, and more.

<img src="static/photos/IMG_0966.HEIC" alt="IMG_0966" style="display: inline-block; width: 45%; margin-right: 5%;" />
<img src="static/photos/IMG_0976.heic" alt="IMG_0976" style="display: inline-block; width: 45%;" />

## Project Structure

The project is structured to isolate different components for better organization and maintainability. Below is an overview of the project structure:

```
.
├── examples
│   ├── transcription
│   │   ├── whisper.py
│   │   └── youtube_wav_fetcher.py
├── manifests
│   ├── minio
│   ├── monitoring
│   ├── ollama
│   └── whisper
├── src
│   ├── backend
│   │   └── watchservice
│   │       └── main.py
│   ├── frontend
│   │   ├── components
│   │   │   ├── Avatar.jsx
│   │   │   └── Experience.jsx
│   │   ├── App.jsx
│   │   └── main.jsx
├── text-to-speech-webgpu
│   ├── src
│   │   ├── App.jsx
│   │   └── main.jsx
│   └── index.html
├── package.json
└── README.md
```

## Ollama Query example

curl http://localhost:11434/api/pull -d '{
  "name": "smollm:135m"
}'

curl http://localhost:11434/api/generate -d '{
  "model": "smollm:135m",
  "prompt": "What is your name"
}'

## Installation / Management of Solr On Kubernetes

https://dan-niles.medium.com/setting-up-apache-solr-on-kubernetes-with-rancher-desktop-931433d8f56b

## 3D Assistant in three.js

The 3D assistant is built using three.js and react-three-fiber. It includes an animated avatar that can perform various actions and respond to user inputs.

### Key Components

- `Avatar.jsx`: This component handles the 3D model of the avatar, including animations and lip-syncing.
- `Experience.jsx`: This component sets up the 3D scene, including lighting and environment.

### Usage

To run the 3D assistant, navigate to the `src/frontend` directory and run the following commands:

```bash
npm install
npm run dev
```

## Openvoice OS

Openvoice OS is integrated into the project to provide voice assistant capabilities. It leverages various open-source tools and libraries to enable voice recognition and response generation.

### Setup

To set up Openvoice OS, follow the instructions in the `openvoice-os` directory.

### Usage

Once set up, you can interact with the voice assistant through the provided interface in the frontend.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
