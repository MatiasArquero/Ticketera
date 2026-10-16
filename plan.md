## TICKETERA (MVP Jira Simplified) PLAN

## 🎯 OBJETIVO GENERAL Y ARQUITECTURA
Migración y construcción de una SPA en Vue 3 que consuma una API REST C# .NET estructurada en capas, enfocada en la gestión de proyectos mediante una jerarquía de Tickets Padre y Subtickets.

## 📂 ENTORNO DE TRABAJO
- **Raíz:** `C:\Users\MatiasArquero\Documents\Proyectos\TICKETERA`
- **Backend Activo:** `\TICKETERA_WEB_API` (C# .NET)
- **Referencia Legacy:** `\TICKETERA_BFF` (Flask)
- **Recursos Globales:** `\RECURSOS` (Contiene `style.css` en `\Hoja de estilos brutalista`)
- **Nuevo Frontend:** `\TICKETERA_FRONTEND` (Se creará en la Fase 0)

---

## 🚀 FASE 0: Scaffolding e Infraestructura Base (Frontend)
*Objetivo: Levantar el esqueleto de Vue 3, limpiar dependencias y aplicar el estilo global.*
- [X] **0.1 CLI:** Ejecutar `npm create vue@latest` en la raíz para generar la carpeta `TICKETERA_FRONTEND`.
- [X] **0.2 Limpieza:** Eliminar componentes de ejemplo (HelloWorld, iconos), limpiar `App.vue` y borrar el CSS que trae Vite por defecto.
- [X] **0.3 Dependencias:** Instalar `vue-router`, `pinia` y `axios`.
- [ ] **0.4 Estilos Globales:** Copiar el archivo `style.css` desde `..\RECURSOS\Hoja de estilos brutalista\style.css` a `src/assets/style.css` e importarlo directamente en `src/main.js`.
- [ ] **0.5 Estructura de Carpetas:** Crear dentro de `src/` los directorios: `/views`, `/components`, `/layouts`, `/router`, `/stores`, `/services`.

## 🛠️ FASE 1: Enrutamiento y Sistema de Layouts
*Objetivo: Crear las cáscaras visuales publicas y privadas basándose en el diseño marco de Flask.*
- [ ] **1.1 Cáscara Pública:** Crear `src/layouts/PublicLayout.vue` (usando como molde el contenedor de la portada de Flask.)
- [ ] **1.2 Cáscara Privada:** Crear `src/layouts/PrivateLayout.vue` (Sidebar, Navbar superior, contenedor principal) Crea una maqetacion nueva manteniendo el estilo brutalista impuesto BFF en flask, pero manteniendo un diseño standar en la industria.
- [ ] **1.3 Ruteo Dinámico:** Configurar `App.vue` usando `<component :is="layout">` o anidación de `<RouterView>` para alternar visualmente según la ruta actual.

## 🔐 FASE 2: Módulo de Autenticación (Vertical Slice)
*Objetivo: Conectar Vue con el JWT de C# y proteger las rutas.*
- [ ] **2.1 API Service:** Crear `src/services/api.js`. Configurar Axios apuntando a la URL de C#. Implementar `interceptors.request` para inyectar `Authorization: Bearer Token`.
- [ ] **2.2 Estado Global:** Crear `src/stores/auth.js` en Pinia. Definir acciones para `login`, `logout` y persistencia en `localStorage`.
- [ ] **2.3 Vistas de Acceso:** Crear `LoginView.vue` y `RegisterView.vue`. Conectar los formularios al store de Pinia, basar las vistas copiando exactamente la estructura HTML de los respectivos auth registo y login de Flask.
- [ ] **2.4 Guardia de Seguridad:** Modificar `src/router/index.js`. Agregar `router.beforeEach` para leer Pinia; si la ruta tiene `requiresAuth: true` y no hay token, redirigir a `/login`.

## 👤 FASE 3: Módulo de Identidad y Perfil
*Objetivo: Visualizar y modificar los datos básicos del usuario autenticado.*
- [ ] **3.1 Análisis Backend:** Leer `UsuariosController` en C#. Identificar qué endpoints GET/PUT existen para el perfil.
- [ ] **3.2 Completar Backend:** Si falta, codificar en C# el endpoint `GET /api/perfil` (que descifre el ID desde el JWT) y `PUT /api/perfil` (solo Nombre, Apellido y Username).
- [ ] **3.3 Componentes UI:** Crear `src/components/perfil/TarjIdentidad.vue` usando clases del `style.css`.
- [ ] **3.4 Vista Principal:** Crear `ProfileView.vue` (con `PrivateLayout`). Hacer el `fetch` de datos en el ciclo `onMounted` y pasarlos al componente vía `props`.
- [ ] **3.5 Test de Integración:** Verificar visualmente que al editar el nombre, el cambio persista en la base de datos de .NET y se refleje en Vue sin recargar la página.

## 🎫 FASE 4: Motor de Tickets (Jira Simplified)
*Objetivo: Implementar la lógica de negocio central (relación Padre -> Hijo).*
- [ ] **4.1 Modelo de Datos (C#):** Diseñar o actualizar la entidad `Ticket` en Entity Framework. Debe incluir `ParentTicketId` (nullable, FK a la misma tabla `Ticket`), `AssignedUserId`, `Estado`, `Prioridad`.
- [ ] **4.2 Endpoints (C#):** 
      - `POST /api/tickets`: Creación genérica (si trae ParentTicketId, es un subticket).
      - `GET /api/tickets/proyectos`: Trae solo tickets donde `ParentTicketId` es NULL.
      - `GET /api/tickets/{id}/subtickets`: Trae la lista de hijos.
- [ ] **4.3 Componentes (Vue):** 
      - `TarjetaProyecto.vue` (para tickets padre).
      - `TarjetaSubticket.vue` (versión minimalista para tareas hijas).
- [ ] **4.4 Vistas (Vue):** 
      - Crear `DashboardView.vue` (Listado de proyectos asignados).
      - Crear `TicketDetailView.vue` (Vista profunda de un ticket Padre que renderice recursivamente o en lista sus subtickets).

---

## ⚠️ REGLA DE ORO DE EJECUCIÓN
El agente TIENE PROHIBIDO iniciar una nueva Fase o Sub-Fase si la anterior no ha sido probada y verificada mediante un resumen en el chat.