console.log("JavaScript está funcionando");

const botonInicio = document.getElementById("ordenar-inicio");
const botonInicioCerradas = document.getElementById("ordenar-inicio-cerradas");
const botonCapital = document.getElementById("ordenar-capital");
const botonGanancia = document.getElementById("ordenar-ganancia");
const botonDuracion = document.getElementById("ordenar-duracion");
const botonDuracionCerradas = document.getElementById("ordenar-duracion-cerradas");
const tablaAbiertas = document.getElementById("tabla-posiciones-abiertas");
const tablaCerradas = document.getElementById("tabla-posiciones-cerradas");
const filas = tablaAbiertas ? tablaAbiertas.querySelectorAll("tr") : [];
const filasCerradas = tablaCerradas ? tablaCerradas.querySelectorAll("tr") : [];
const filasPosiciones = Array.from(filas).slice(1);
const filasPosicionesCerradas = Array.from(filasCerradas).slice(1);

let ordenAscendente = true;
let ordenAscendenteCerradas = true;
let ordenCapitalAscendente = true;
let ordenGananciaAscendente = true;
let ordenDuracionAscendente = true;
let ordenDuracionAscendenteCerradas = true;

function ordenarFilas(filas,tabla,columna,tipoDato,ordenAscendente) {
    
    filas.sort(function(a,b) {
        
        const celdaA = a.querySelector(
            `[data-campo="${columna}"]`
        );
        
        const celdaB = b.querySelector(
            `[data-campo="${columna}"]`
        );
        
        const textoA = celdaA.dataset.valor || celdaA.textContent.trim();
        const textoB = celdaB.dataset.valor || celdaB.textContent.trim();
        
        let valorA;
        let valorB;
        
        if (tipoDato === "fecha") {
            
            valorA = new Date(textoA);
            valorB = new Date(textoB);
            
        } else if (tipoDato === "numero") {
            
            valorA = Number(textoA);
            valorB = Number(textoB);
        }
        
        return ordenAscendente
        ? valorA - valorB
        : valorB - valorA;
    
    });
    
    tabla.append(...filas);
    
    return !ordenAscendente;
}

function ordenarPorInicio () {
    
    ordenAscendente = ordenarFilas(
        filasPosiciones,
        tablaAbiertas,
        "fecha-apertura",
        "fecha",
        ordenAscendente
    );
}

function ordenarPorInicioCerradas () {
    
    ordenAscendenteCerradas = ordenarFilas(
        filasPosicionesCerradas,
        tablaCerradas,
        "fecha-apertura",
        "fecha",
        ordenAscendenteCerradas
    );
}

function ordenarPorCapital() {
    
    ordenCapitalAscendente = ordenarFilas(
        filasPosiciones,
        tablaAbiertas,
        "capital-invertido",
        "numero",
        ordenCapitalAscendente
    );
}

function ordenarPorGanancia() {
    
    ordenGananciaAscendente = ordenarFilas( 
        filasPosicionesCerradas,
        tablaCerradas,
        "ganancia-realizada",
        "numero",
        ordenGananciaAscendente
    );
}

function ordenarPorDuracion() {
    
    ordenDuracionAscendente = ordenarFilas(
        filasPosiciones,
        tablaAbiertas,
        "duracion",
        "numero",
        ordenDuracionAscendente
    );
}

function ordenarPorDuracionCerradas() {
    
    ordenDuracionAscendenteCerradas = ordenarFilas(
        filasPosicionesCerradas,
        tablaCerradas,
        "duracion",
        "numero",
        ordenDuracionAscendenteCerradas
    );
}

if (botonInicio) {
    botonInicio.addEventListener("click",ordenarPorInicio);
}

if (botonInicioCerradas) {
    botonInicioCerradas.addEventListener("click",ordenarPorInicioCerradas);
}

if (botonCapital){
    botonCapital.addEventListener("click",ordenarPorCapital);
}

if(botonGanancia) {
    botonGanancia.addEventListener("click",ordenarPorGanancia);
}

if (botonDuracion) {
    botonDuracion.addEventListener("click",ordenarPorDuracion);
}

if (botonDuracionCerradas) {
    botonDuracionCerradas.addEventListener("click",ordenarPorDuracionCerradas);
}

function venderTodo(cantidad, inputId) {
    
    const inputCantidad = document.getElementById(inputId);
    
    if (inputCantidad) {
        inputCantidad.value = cantidad;
    }
}

const botonesMax = document.querySelectorAll(".boton-max");

botonesMax.forEach(function(boton) {

    boton.addEventListener("click", function() {
        venderTodo(
            boton.dataset.cantidad,
            boton.dataset.inputId
        );
    });
});

function mostrarFormulario(formularioId) {
    
    const formulario = document.getElementById(formularioId);
    
    if (formulario) {
        formulario.classList.toggle("formulario-oculto");
    }
}

const botonesMostrarFormulario = document.querySelectorAll(".boton-mostrar-formulario");

botonesMostrarFormulario.forEach(function(boton) {
    
    boton.addEventListener("click", function() {
        mostrarFormulario(boton.dataset.formularioId);
    });
});