const prompt = require("prompt-sync")(); // Importar prompt-sync

let personas = []
let cantidad = prompt("¿Cuántas personas deseas registrar?" +" "  );

for(let i = 0; i < cantidad; i++) {
    let nombre = prompt("Ingrese el nombre de la persona :"+" "  );
    let edad = parseInt(prompt("Ingrese la edad de " + nombre + ": " ));
    let nota = parseFloat(prompt("Ingrese la nota de " + nombre +": " ));

    personas.push([nombre, edad, nota])
}

 // Mostrar la lista de personas tal como fueron ingresadas
 console.log("Datos ingresados:");
 console.table(personas);

 // Ordenar por nota de mayor a menor
personas.sort((a, b) => b[2] - a[2]);

// Mostrar la lista ordenada
console.log("Datos ordenados por nota (de mayor a menor):");
console.table(personas);