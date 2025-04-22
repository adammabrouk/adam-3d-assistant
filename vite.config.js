import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@backend': '/src/backend',
      '@frontend': '/src/frontend',
      '@examples': '/examples',
      '@manifests': '/manifests',
      '@text-to-speech-webgpu': '/text-to-speech-webgpu',
    },
  },
})
