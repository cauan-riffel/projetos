var valor = '';

function calc(vr){
    if(valor=='1 + 1'){
        valor = 3 ;
        document.getElementById('resposta').textContent = valor;
        valor = '';
    }else if(vr != '='){
        valor += vr
        document.getElementById('resposta').textContent = valor;
    }else{
        valor = eval(valor);
        document.getElementById('resposta').textContent = valor;
        valor = '';}
}

function limpar(){
    valor = '';
    document.getElementById('resposta').textContent = valor;
}