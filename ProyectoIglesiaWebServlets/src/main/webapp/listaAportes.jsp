<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@page import="java.util.List"%>
<%@page import="com.iglesia.gestion.model.Aporte"%>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Historial de Aportes - Sistema Iglesia</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #F8F9FA; padding: 20px; }
        .container { max-width: 800px; margin: 20px auto; background: #fff; padding: 25px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
        h2 { color: #1B4965; }
        .alerta { background-color: #d4edda; color: #155724; padding: 10px; border-radius: 4px; margin-bottom: 15px; }
        table { width: 100%; border-collapse: collapse; margin-top: 15px; }
        th, td { border: 1px solid #ddd; padding: 10px; text-align: left; }
        th { background-color: #1B4965; color: #fff; }
        .btn-volver { display: inline-block; margin-top: 15px; padding: 8px 14px; background: #52B788; color: #fff; text-decoration: none; border-radius: 4px; }
        .btn-eliminar { color: #c0392b; text-decoration: none; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Listado de Diezmos y Ofrendas Registrados</h2>

        <%
            String mensaje = (String) request.getAttribute("mensaje");
            if (mensaje != null) {
        %>
            <div class="alerta"><%= mensaje %></div>
        <%
            }
        %>

        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Tipo</th>
                    <th>Feligrés</th>
                    <th>Monto ($)</th>
                    <th>Fecha</th>
                    <th>Acción (GET)</th>
                </tr>
            </thead>
            <tbody>
                <%
                    List<Aporte> aportes = (List<Aporte>) request.getAttribute("aportes");
                    if (aportes != null && !aportes.isEmpty()) {
                        for (Aporte ap : aportes) {
                %>
                <tr>
                    <td><%= ap.getId() %></td>
                    <td><%= ap.getTipoAporte() %></td>
                    <td><%= ap.getNombreFeligres() %></td>
                    <td>$ <%= ap.getMonto() %></td>
                    <td><%= ap.getFecha() %></td>
                    <td>
                        <a href="AporteServlet?accion=eliminar&id=<%= ap.getId() %>" class="btn-eliminar">Eliminar</a>
                    </td>
                </tr>
                <%
                        }
                    } else {
                %>
                <tr>
                    <td colspan="6">No hay registros disponibles.</td>
                </tr>
                <%
                    }
                %>
            </tbody>
        </table>

        <a href="index.html" class="btn-volver">&larr; Registrar nuevo aporte</a>
    </div>
</body>
</html>
