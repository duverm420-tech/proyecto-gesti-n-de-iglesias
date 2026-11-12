package com.iglesia.gestion.dao;

import com.iglesia.gestion.conexion.ConexionBD;
import com.iglesia.gestion.model.Aporte;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

/**
 * Objeto de Acceso a Datos (DAO) para la gestión de aportes mediante JDBC.
 */
public class AporteDAO {

    // 1. INSERCIÓN (Create)
    public boolean insertarAporte(Aporte aporte) {
        String sql = "INSERT INTO aportes (tipo_aporte, monto, fecha_transaccion, fk_miembro) VALUES (?, ?, ?, ?)";
        try (Connection conn = ConexionBD.obtenerConexion();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            
            pstmt.setString(1, aporte.getTipoAporte());
            pstmt.setBigDecimal(2, aporte.getMonto());
            pstmt.setTimestamp(3, Timestamp.valueOf(aporte.getFechaTransaccion()));
            pstmt.setLong(4, aporte.getIdMiembro());
            
            int filasAfectadas = pstmt.executeUpdate();
            return filasAfectadas > 0;
        } catch (SQLException e) {
            System.err.println("Error al insertar aporte: " + e.getMessage());
            return false;
        }
    }

    // 2. CONSULTA (Read)
    public List<Aporte> consultarAportes() {
        List<Aporte> listaAportes = new ArrayList<>();
        String sql = "SELECT id_aporte, tipo_aporte, monto, fecha_transaccion, fk_miembro FROM aportes";
        
        try (Connection conn = ConexionBD.obtenerConexion();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
            
            while (rs.next()) {
                Aporte aporte = new Aporte();
                aporte.setIdAporte(rs.getLong("id_aporte"));
                aporte.setTipoAporte(rs.getString("tipo_aporte"));
                aporte.setMonto(rs.getBigDecimal("monto"));
                aporte.setFechaTransaccion(rs.getTimestamp("fecha_transaccion").toLocalDateTime());
                aporte.setIdMiembro(rs.getLong("fk_miembro"));
                listaAportes.add(aporte);
            }
        } catch (SQLException e) {
            System.err.println("Error al consultar aportes: " + e.getMessage());
        }
        return listaAportes;
    }

    // 3. ACTUALIZACIÓN (Update)
    public boolean actualizarAporte(Aporte aporte) {
        String sql = "UPDATE aportes SET tipo_aporte = ?, monto = ? WHERE id_aporte = ?";
        try (Connection conn = ConexionBD.obtenerConexion();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            
            pstmt.setString(1, aporte.getTipoAporte());
            pstmt.setBigDecimal(2, aporte.getMonto());
            pstmt.setLong(3, aporte.getIdAporte());
            
            int filasAfectadas = pstmt.executeUpdate();
            return filasAfectadas > 0;
        } catch (SQLException e) {
            System.err.println("Error al actualizar aporte: " + e.getMessage());
            return false;
        }
    }

    // 4. ELIMINACIÓN (Delete)
    public boolean eliminarAporte(Long idAporte) {
        String sql = "DELETE FROM aportes WHERE id_aporte = ?";
        try (Connection conn = ConexionBD.obtenerConexion();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            
            pstmt.setLong(1, idAporte);
            int filasAfectadas = pstmt.executeUpdate();
            return filasAfectadas > 0;
        } catch (SQLException e) {
            System.err.println("Error al eliminar aporte: " + e.getMessage());
            return false;
        }
    }
}