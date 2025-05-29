# Códigos Postales Costa Rica

Un directorio completo de códigos postales de Costa Rica construido con Astro.js y Tailwind CSS. El sitio web sirve como una herramienta de búsqueda y consulta para todos los códigos postales organizados por provincia, cantón y distrito.

## 🚀 Características

- **Estructura completa**: Páginas para cada provincia, cantón y distrito
- **Búsqueda inteligente**: Barra de búsqueda con autocompletado
- **SEO optimizado**: Meta tags, JSON-LD, sitemap.xml y robots.txt
- **Responsive**: Diseño adaptable para móviles y escritorio
- **Compartir**: Botones para compartir por WhatsApp
- **Navegación**: Breadcrumbs en español para fácil navegación
- **Rendimiento**: Sitio estático generado para máxima velocidad

## 🛠️ Tecnologías

- **Astro.js**: Framework para sitios estáticos
- **Tailwind CSS**: Framework de CSS utilitario
- **TypeScript**: Tipado estático
- **JSON**: Base de datos de códigos postales

## 📁 Estructura del Proyecto

```
src/
├── components/          # Componentes reutilizables
│   ├── Breadcrumb.astro
│   └── SearchBar.astro
├── data/               # Datos de códigos postales
│   └── postal-codes.json
├── layouts/            # Layouts base
│   └── Layout.astro
├── pages/              # Páginas del sitio
│   ├── index.astro
│   ├── sitemap.xml.ts
│   └── codigo-postal/
│       └── [province]/
│           ├── index.astro
│           └── [canton]/
│               ├── index.astro
│               └── [district]/
│                   └── index.astro
├── styles/             # Estilos globales
│   └── global.css
└── utils/              # Funciones utilitarias
    ├── data.ts
    └── url.ts
```

## 🌐 Estructura de URLs

- **Inicio**: `/`
- **Provincia**: `/codigo-postal/san-jose/`
- **Cantón**: `/codigo-postal/san-jose/curridabat/`
- **Distrito**: `/codigo-postal/san-jose/curridabat/granadilla/`

## 📊 Datos

El archivo `src/data/postal-codes.json` contiene todos los códigos postales de Costa Rica con la siguiente estructura:

```json
{
  "province": "San José",
  "canton": "Curridabat", 
  "district": "Granadilla",
  "postal_code": "11802"
}
```

## 🔧 Instalación y Desarrollo

### Prerrequisitos

- Node.js 18+ 
- npm

### Instalación

```bash
# Clonar el repositorio
git clone <repository-url>
cd seo_postal_code

# Instalar dependencias
npm install

# Iniciar servidor de desarrollo
npm run dev

# Construir para producción
npm run build

# Previsualizar build de producción
npm run preview
```

## 🚀 Despliegue

El proyecto está optimizado para desplegarse en Vercel:

1. Conecta tu repositorio a Vercel
2. Vercel detectará automáticamente que es un proyecto Astro
3. El sitio se construirá y desplegará automáticamente

### Variables de Entorno

No se requieren variables de entorno para el funcionamiento básico.

## 📈 SEO y Rendimiento

### Características SEO

- **Meta tags**: Títulos y descripciones optimizadas en español
- **JSON-LD**: Datos estructurados para cada página
- **Sitemap**: Generado automáticamente con todas las URLs
- **Robots.txt**: Configurado para permitir indexación
- **URLs amigables**: Slugs sanitizados sin acentos
- **Open Graph**: Meta tags para redes sociales

### Rendimiento

- **Sitio estático**: Generación en tiempo de build
- **Lazy loading**: Imágenes y componentes optimizados
- **CSS optimizado**: Tailwind CSS con purging automático
- **Compresión**: Assets minificados y comprimidos

## 🔍 Funcionalidades

### Búsqueda

- Autocompletado en tiempo real
- Búsqueda por provincia, cantón, distrito o código postal
- Navegación con teclado (flechas, Enter, Escape)
- Resultados limitados a 10 para mejor rendimiento

### Compartir

- Botón de WhatsApp en cada página de distrito
- Botón para copiar código postal al portapapeles
- URLs amigables para compartir

### Navegación

- Breadcrumbs en todas las páginas internas
- Enlaces contextuales entre provincias, cantones y distritos
- Sidebar con información relacionada

## 📱 Responsive Design

El sitio está optimizado para:

- **Móviles**: 320px+
- **Tablets**: 768px+
- **Desktop**: 1024px+

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📞 Contacto

Para preguntas o sugerencias sobre el proyecto, puedes abrir un issue en GitHub.

---

**Códigos Postales Costa Rica** - Directorio completo y actualizado de códigos postales de Costa Rica 🇨🇷

```sh
npm create astro@latest -- --template minimal
```

[![Open in StackBlitz](https://developer.stackblitz.com/img/open_in_stackblitz.svg)](https://stackblitz.com/github/withastro/astro/tree/latest/examples/minimal)
[![Open with CodeSandbox](https://assets.codesandbox.io/github/button-edit-lime.svg)](https://codesandbox.io/p/sandbox/github/withastro/astro/tree/latest/examples/minimal)
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/withastro/astro?devcontainer_path=.devcontainer/minimal/devcontainer.json)

> 🧑‍🚀 **Seasoned astronaut?** Delete this file. Have fun!

## 🚀 Project Structure

Inside of your Astro project, you'll see the following folders and files:

```text
/
├── public/
├── src/
│   └── pages/
│       └── index.astro
└── package.json
```

Astro looks for `.astro` or `.md` files in the `src/pages/` directory. Each page is exposed as a route based on its file name.

There's nothing special about `src/components/`, but that's where we like to put any Astro/React/Vue/Svelte/Preact components.

Any static assets, like images, can be placed in the `public/` directory.

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `npm install`             | Installs dependencies                            |
| `npm run dev`             | Starts local dev server at `localhost:4321`      |
| `npm run build`           | Build your production site to `./dist/`          |
| `npm run preview`         | Preview your build locally, before deploying     |
| `npm run astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `npm run astro -- --help` | Get help using the Astro CLI                     |

## 👀 Want to learn more?

Feel free to check [our documentation](https://docs.astro.build) or jump into our [Discord server](https://astro.build/chat).
