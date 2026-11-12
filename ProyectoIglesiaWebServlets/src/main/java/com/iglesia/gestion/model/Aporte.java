package com.iglesia.gestion.model;

import java.math.BigDecimal;
import java.time.LocalDate;

public class Aporte {
    private int id;
    private String tipoAporte;
    private String nombreFeligres;
    private BigDecimal monto;
    private LocalDate fecha;

    public Aporte() {}

    public Aporte(int id, String tipoAporte, String nombreFeligres, BigDecimal monto, LocalDate fecha) {
        this.id = id;
        this.tipoAporte = tipoAporte;
        this.nombreFeligres = nombreFeligres;
        this.monto = monto;
        this.fecha = fecha;
    }

    public int getId() { return id; }
    public void setId(int id) { this.id = id; }

    public String getTipoAporte() { return tipoAporte; }
    public void setTipoAporte(String tipoAporte) { this.tipoAporte = tipoAporte; }

    public String getNombreFeligres() { return nombreFeligres; }
    public void setNombreFeligres(String nombreFeligres) { this.nombreFeligres = nombreFeligres; }

    public BigDecimal getMonto() { return monto; }
    public void setMonto(BigDecimal monto) { this.monto = monto; }

    public LocalDate getFecha() { return fecha; }
    public void setFecha(LocalDate fecha) { this.fecha = fecha; }
}
