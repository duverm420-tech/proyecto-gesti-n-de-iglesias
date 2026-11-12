package com.iglesia.gestion.model;

import java.math.BigDecimal;
import java.time.LocalDateTime;

/**
 * Representa la entidad de aportes financieros (Diezmos y Ofrendas).
 * @author Duver Stiven Martínez Caicedo
 */
public class Aporte {
    private Long idAporte;
    private String tipoAporte;
    private BigDecimal monto;
    private LocalDateTime fechaTransaccion;
    private Long idMiembro;

    public Aporte() {}

    public Aporte(String tipoAporte, BigDecimal monto, LocalDateTime fechaTransaccion, Long idMiembro) {
        this.tipoAporte = tipoAporte;
        this.monto = monto;
        this.fechaTransaccion = fechaTransaccion;
        this.idMiembro = idMiembro;
    }

    public Long getIdAporte() { return idAporte; }
    public void setIdAporte(Long idAporte) { this.idAporte = idAporte; }

    public String getTipoAporte() { return tipoAporte; }
    public void setTipoAporte(String tipoAporte) { this.tipoAporte = tipoAporte; }

    public BigDecimal getMonto() { return monto; }
    public void setMonto(BigDecimal monto) { this.monto = monto; }

    public LocalDateTime getFechaTransaccion() { return fechaTransaccion; }
    public void setFechaTransaccion(LocalDateTime fechaTransaccion) { this.fechaTransaccion = fechaTransaccion; }

    public Long getIdMiembro() { return idMiembro; }
    public void setIdMiembro(Long idMiembro) { this.idMiembro = idMiembro; }
}