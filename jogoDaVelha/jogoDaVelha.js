let jogadores = [prompt('jogador1, digite seu nome'), prompt('jogador2, digite seu nome')]

let vitorias = [0, 0]

var vez = 0;

var valoresDiferentes = 0;

var TrueFalseOuNone = 0;

var celas = {
    1:document.getElementById('cela1').getAttribute('src'),
    2:document.getElementById('cela2').getAttribute('src'),
    3:document.getElementById('cela3').getAttribute('src'),
    4:document.getElementById('cela4').getAttribute('src'),
    5:document.getElementById('cela5').getAttribute('src'),
    6:document.getElementById('cela6').getAttribute('src'),
    7:document.getElementById('cela7').getAttribute('src'),
    8:document.getElementById('cela8').getAttribute('src'),
    9:document.getElementById('cela9').getAttribute('src')
}

function casa(qc){
    // qc = Qual casa
    if(celas[qc] != 'img/o.png' && vez == 0 && celas[qc] != 'img/x.png' && vez == 0){
        eval('cela' + qc).setAttribute('src', 'img/o.png');
        vez ++;
        atualizar()
        TrueFalseOuNone = ganhou()
        if(TrueFalseOuNone == true){
           alert('o jogador ' + jogadores[0] + ' ganhou essa rodada!!!!');
           vitorias[0] ++;
        }else if(TrueFalseOuNone == null){
           alert('ninguém ganhou!!!!!')
        }
    }else if(celas[qc] != 'img/o.png' && vez == 1 && celas[qc] != 'img/x.png' && vez == 1){
        eval('cela' + qc).setAttribute('src', 'img/x.png');
        vez --;
        atualizar()
        TrueFalseOuNone = ganhou()
        if(TrueFalseOuNone == true){
           alert('o jogador ' + jogadores[1] + ' ganhou essa rodada!!!!');
           vitorias[1] ++;
        }else if(TrueFalseOuNone == null){
           alert('ninguém ganhou!!!!!')
        }
    }else{
        alert('movimento inválido');
    }
    mostrarTudo()
}


function atualizar(){
    celas[1] = document.getElementById('cela1').getAttribute('src')
    celas[2] = document.getElementById('cela2').getAttribute('src')
    celas[3] = document.getElementById('cela3').getAttribute('src')
    celas[4] = document.getElementById('cela4').getAttribute('src')
    celas[5] = document.getElementById('cela5').getAttribute('src')
    celas[6] = document.getElementById('cela6').getAttribute('src')
    celas[7] = document.getElementById('cela7').getAttribute('src')
    celas[8] = document.getElementById('cela8').getAttribute('src')
    celas[9] = document.getElementById('cela9').getAttribute('src')
}


function ganhou(){
    if(
    // horizontal
    celas[1] == celas[2] && celas[2] == celas[3] ||
    celas[4] == celas[5] && celas[5] == celas[6] ||
    celas[7] == celas[8] && celas[8] == celas[9] ||
    // vertical
    celas[1] == celas[4] && celas[4] == celas[7] ||
    celas[2] == celas[5] && celas[5] == celas[8] ||
    celas[3] == celas[6] && celas[6] == celas[9] ||
    // diagonal
    celas[1] == celas[5] && celas[5] == celas[9] && celas[1] != 'img/preto.png' ||
    celas[3] == celas[5] && celas[5] == celas[7] && celas[3] != 'img/preto.png'){
        limpar()
        return true
    }else{
        for(var i in celas){
            if(celas[i] != 'img/preto.png' && celas[i] != 'img/cinza.png'){
                valoresDiferentes ++;
                break
            }
        }
        if(valoresDiferentes == 9){
            limpar()
            return null
        }else{
            return false
        }
        
      }
}


function mostrarTudo(){
    if(vez == 0){
        document.getElementById('vez').innerHTML = 'quem joga agora é ' + jogadores[0];
    }else{
        document.getElementById('vez').innerHTML = 'quem joga agora é ' + jogadores[1];
    }
    document.getElementById('nomeJogador1').innerHTML = jogadores[0]
    document.getElementById('nomeJogador2').innerHTML = jogadores[1]
    document.getElementById('pontuacao1').innerHTML = vitorias[0]
    document.getElementById('pontuacao2').innerHTML = vitorias[1]
}


function limpar(){
    document.getElementById('cela1').setAttribute('src', 'img/preto.png')
    document.getElementById('cela2').setAttribute('src', 'img/cinza.png')
    document.getElementById('cela3').setAttribute('src', 'img/preto.png')
    document.getElementById('cela4').setAttribute('src', 'img/cinza.png')
    document.getElementById('cela5').setAttribute('src', 'img/preto.png')
    document.getElementById('cela6').setAttribute('src', 'img/cinza.png')
    document.getElementById('cela7').setAttribute('src', 'img/preto.png')
    document.getElementById('cela8').setAttribute('src', 'img/cinza.png')
    document.getElementById('cela9').setAttribute('src', 'img/preto.png')
    valoresDiferentes = 0
    atualizar()
}


