package com.iglesia.gestion;

import com.iglesia.gestion.dao.AporteDAO;
import com.iglesia.gestion.model.Aporte;

import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        AporteDAO aporteDao = new AporteDAO();

        // Prueba de Inserción
        Aporte nuevoAporte = new Aporte("Diezmo", new BigDecimal("150000.00"), LocalDateTime.now(), 1L);
        boolean insertado = aporteDao.insertarAporte(nuevoAporte);
        if (insertado) {
            System.out.println("Aporte registrado correctamente en la base de datos.");
        }

        // Prueba de Consulta
        List<Aporte> lista = aporteDao.consultarAportes();
        System.out.println("--- LISTADO DE APORTES ---");
        for (Aporte a : lista) {
            System.out.println("ID: " + a.getIdAporte() + " | Tipo: " + a.getTipoAporte() + " | Monto: $" + a.getMonto());
        }
    }
}
