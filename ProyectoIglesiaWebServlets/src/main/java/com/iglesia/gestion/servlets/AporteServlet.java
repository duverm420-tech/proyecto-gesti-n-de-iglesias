package com.iglesia.gestion.servlets;

import com.iglesia.gestion.model.Aporte;
import java.io.IOException;
import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet(name = "AporteServlet", urlPatterns = {"/AporteServlet"})
public class AporteServlet extends HttpServlet {

    // Lista en memoria para simular persistencia en la prueba del módulo web
    private static final List<Aporte> listaAportes = new ArrayList<>();
    private static int secuenciaId = 1;

    static {
        listaAportes.add(new Aporte(secuenciaId++, "Diezmo", "Carlos Andrés Gómez", new BigDecimal("150000"), LocalDate.now()));
        listaAportes.add(new Aporte(secuenciaId++, "Ofrenda", "Anónimo / Congregación", new BigDecimal("45000"), LocalDate.now()));
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String accion = request.getParameter("accion");

        if ("eliminar".equals(accion)) {
            String idParam = request.getParameter("id");
            if (idParam != null) {
                int idEliminar = Integer.parseInt(idParam);
                listaAportes.removeIf(a -> a.getId() == idEliminar);
            }
        }

        request.setAttribute("aportes", listaAportes);
        request.getRequestDispatcher("listaAportes.jsp").forward(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        request.setCharacterEncoding("UTF-8");

        String tipoAporte = request.getParameter("tipoAporte");
        String nombreFeligres = request.getParameter("nombreFeligres");
        String montoParam = request.getParameter("monto");

        if (nombreFeligres == null || nombreFeligres.trim().isEmpty()) {
            nombreFeligres = "Anónimo / General";
        }

        BigDecimal monto = new BigDecimal(montoParam);
        Aporte nuevoAporte = new Aporte(secuenciaId++, tipoAporte, nombreFeligres, monto, LocalDate.now());
        listaAportes.add(nuevoAporte);

        request.setAttribute("mensaje", "Aporte registrado correctamente en el sistema.");
        request.setAttribute("aportes", listaAportes);
        request.getRequestDispatcher("listaAportes.jsp").forward(request, response);
    }
}
