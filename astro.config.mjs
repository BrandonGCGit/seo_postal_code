// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  site: 'https://seo-postal-code.vercel.app',
  integrations: [
    sitemap({
      changefreq: 'weekly',
      priority: 0.7,
    })
  ],
  vite: {
    plugins: [tailwindcss()]
  }
});