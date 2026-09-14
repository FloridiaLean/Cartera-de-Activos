console.log("JavaScript está funcionando");

const botonInicio = document.getElementById("ordenar-inicio");
const botonInicioCerradas = document.getElementById("ordenar-inicio-cerradas");
const botonCapital = document.getElementById("ordenar-capital");
const botonGanancia = document.getElementById("ordenar-ganancia");
const botonDuracion = document.getElementById("ordenar-duracion");
const botonDuracionCerradas = document.getElementById("ordenar-duracion-cerradas");
const tablaAbiertas = document.getElementById("tabla-posiciones-abiertas");
const tablaCerradas = document.getElementById("tabla-posiciones-cerradas");
const filas = tablaAbiertas.querySelectorAll("tr");
const filasCerradas = tablaCerradas.querySelectorAll("tr");
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

botonInicio.addEventListener("click",ordenarPorInicio);
botonInicioCerradas.addEventListener("click",ordenarPorInicioCerradas);
botonCapital.addEventListener("click",ordenarPorCapital);
botonGanancia.addEventListener("click",ordenarPorGanancia);
botonDuracion.addEventListener("click",ordenarPorDuracion);
botonDuracionCerradas.addEventListener("click",ordenarPorDuracionCerradas);
