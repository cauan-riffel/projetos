"use strict"

function descriptografar(){
    let numero = prompt('digite um numero em binario para transforma-lo em decimal'), 
    comprimento = numero.length, 
    resultado = 0;
    for (let i = 0; i <= comprimento; i++){
         resultado += Number(numero[i]) * 2 ** comprimento;
         comprimento -= 1;
    }
    alert(resultado)
}


function criptografar(){
    let numero = prompt('digite um numero em decimal para transforma-lo em binario'), 
    resto = Number(numero), 
    total = '';
    while(!(resto == 0 || resto == 1)){
        total += String(resto % 2);
        resto = Math.floor(resto / 2);
    }
    if(resto == 1){
        total += '1';
    }else{
        total += '01';
    }
    total = total.split("").reverse().join("");
    alert(total);
}





