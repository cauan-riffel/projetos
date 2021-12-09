// function diasDVida(){
//     var nome = document.getElementById('nome').value;
//     var anos = Numeber(document.getElementById('anos').value) * 365;
//     document.getElementById('dias').textContent = nome, 'você têm', anos, 'anos de vida';
// }
// var resposta = document.getElementById('dias');
// resposta.onclick = diasDVida;
function diasDVida() {
    var nome = document.getElementById('nome').value;
    var dias = Number(document.getElementById('anos').value) * 365 + Number(document.getElementById('mes').value) * 30 + Number(document.getElementById('dia').value);
    document.getElementById('mostrar').textContent = nome + ' sua idade em dias é de ' + dias + ' dias';
}
var mostrar = document.getElementById('mostrar');
mostrar.onclick = diasDVida;