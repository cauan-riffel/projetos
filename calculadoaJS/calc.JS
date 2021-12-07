var valor = '';

function ad1(){
    valor += '1';
    document.getElementById('resposta').textContent = valor;
}

function ad2(){
    valor += '2';
    document.getElementById('resposta').textContent = valor;
}

function ad3(){
    valor += '3';
    document.getElementById('resposta').textContent = valor;
}

function ad4(){
    valor += '4';
    document.getElementById('resposta').textContent = valor;
}

function ad5(){
    valor += '5';
    document.getElementById('resposta').textContent = valor;
}

function ad6(){
    valor += '6';
    document.getElementById('resposta').textContent = valor;
}

function ad7(){
    valor += '7';
    document.getElementById('resposta').textContent = valor;
}

function ad8(){
    valor += '8';
    document.getElementById('resposta').textContent = valor;
}

function ad9(){
    valor += '9';
    document.getElementById('resposta').textContent = valor;
}

function ad0(){
    valor += '0';
    document.getElementById('resposta').textContent = valor;
}

function mais(){
    valor += ' + ';
    document.getElementById('resposta').textContent = valor;
}

function menos(){
    valor += ' - ';
    document.getElementById('resposta').textContent = valor;
}

function divd(){
    valor += ' / ';
    document.getElementById('resposta').textContent = valor;
}

function vezes(){
    valor += ' * ';
    document.getElementById('resposta').textContent = valor;
}

function ponto(){
    valor += '.';
    document.getElementById('resposta').textContent = valor;
}

function calc(){
    valor = eval(valor);
    document.getElementById('resposta').textContent = valor;
    valor = '';
}

function limpar(){
    valor = '';
    document.getElementById('resposta').textContent = valor;
}