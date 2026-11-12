# Sistema de Gestión para Iglesias - Módulo Web (Servlets y JSP)

**Aprendiz:** Duver Stiven Martínez Caicedo  
**Ficha:** 3336220  
**Evidencia:** GA7-220501096-AA2-EV02  

## Descripción del Módulo
Implementación web del módulo de **Tesorería (Registro y Consulta de Diezmos y Ofrendas)** desarrollado en Java utilizando **Servlets** y **JavaServer Pages (JSP)** bajo el patrón MVC.

## Funcionalidades Implementadas
- **Formulario HTML (`index.html`):** Captura de datos de diezmos y ofrendas mediante petición HTTP `POST`.
- **Controlador (`AporteServlet.java`):** Procesamiento de peticiones `doPost` (registro de aportes) y `doGet` (listado y eliminación de registros).
- **Vista Dinámica (`listaAportes.jsp`):** Renderizado dinámico en servidor mediante directivas (`<%@page %>`), scriptlets (`<% %>`) y expresiones JSP (`<%= %>`).
