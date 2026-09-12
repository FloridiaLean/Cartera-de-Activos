console.log("JavaScript está funcionando");

const botonInicio = document.getElementById("ordenar-inicio");
const botonInicioCerradas = document.getElementById("ordenar-inicio-cerradas");
const tablaAbiertas = document.getElementById("tabla-posiciones-abiertas");
const tablaCerradas = document.getElementById("tabla-posiciones-cerradas");
const filas = tablaAbiertas.querySelectorAll("tr");
const filasCerradas = tablaCerradas.querySelectorAll("tr");
const filasPosiciones = Array.from(filas).slice(1);
const filasPosicionesCerradas = Array.from(filasCerradas).slice(1);

let ordenAscendente = true;
let ordenAscendenteCerradas = true;

function ordenarPorInicio () {
    
    filasPosiciones.sort(function(a,b) {
        
        const celdaFechaA = a.querySelector(
            '[data-campo="fecha-apertura"]'
        );
        
        const celdaFechaB = b.querySelector(
            '[data-campo="fecha-apertura"]'
        );
        
        const textoFechaA = celdaFechaA.textContent.trim();
        const textoFechaB = celdaFechaB.textContent.trim();
        
        const fechaA = new Date(textoFechaA);
        const fechaB = new Date(textoFechaB);
        
        return ordenAscendente
        ? fechaA - fechaB
        : fechaB - fechaA;
    });
    
    tablaAbiertas.append(...filasPosiciones);
    
    ordenAscendente = !ordenAscendente;
}

function ordenarPorInicioCerradas () {

    filasPosicionesCerradas.sort(function(a,b) {
        
        const celdaFechaA = a.querySelector(
            '[data-campo="fecha-apertura"]'
        );
        
        const celdaFechaB = b.querySelector(
            '[data-campo="fecha-apertura"]'
        );
        
        const textoFechaA = celdaFechaA.textContent.trim();
        const textoFechaB = celdaFechaB.textContent.trim();
        
        const fechaA = new Date(textoFechaA);
        const fechaB = new Date(textoFechaB);
        
        return ordenAscendenteCerradas
        ? fechaA - fechaB
        : fechaB - fechaA;
    
    });
    
    tablaCerradas.append(...filasPosicionesCerradas);
    
    ordenAscendenteCerradas = !ordenAscendenteCerradas;
    
}

botonInicio.addEventListener("click",ordenarPorInicio);
botonInicioCerradas.addEventListener("click",ordenarPorInicioCerradas);