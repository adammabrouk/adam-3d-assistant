## Query example

curl http://localhost:11434/api/pull -d '{
  "name": "smollm:135m"
}'

curl http://localhost:11434/api/generate -d '{
  "model": "smollm:135m",
  "prompt": "What is your name"
}'