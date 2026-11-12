package com.iglesia.gestion.conexion;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

/**
 * Administra la conexión nativa JDBC con la base de datos MySQL.
 */
public class ConexionBD {
    private static final String URL = "jdbc:mysql://localhost:3306/db_iglesia_gestion?useSSL=false&serverTimezone=UTC";
    private static final String USUARIO = "root";
    private static final String CONTRASENA = "tu_contraseña_mysql"; // Cambia por tu clave de MySQL

    public static Connection obtenerConexion() {
        Connection conexion = null;
        try {
            conexion = DriverManager.getConnection(URL, USUARIO, CONTRASENA);
            System.out.println("¡Conexión exitosa a la base de datos por JDBC!");
        } catch (SQLException e) {
            System.err.println("Error al conectar con la base de datos: " + e.getMessage());
        }
        return conexion;
    }
}