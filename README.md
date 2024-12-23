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