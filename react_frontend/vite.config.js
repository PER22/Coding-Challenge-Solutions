import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      // Forward requests to /api to the Django backend
      '/api': 'http://localhost:8000'
    }
  }
})
