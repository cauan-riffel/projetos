import 'dart:io';
import 'dart:math';

void main() {
  List<int> placar = [0, 0];
  while (placar[0] != 2 && placar[1] != 2) {
    List<List<String>> tabuleiro = [
      [' ', ' ', ' '],
      [' ', ' ', ' '],
      [' ', ' ', ' '],
    ];
    List<String> ganhador = [''];
    while (ganhador[0] == '') {
      mostrarTabuleiro(tabuleiro);
      play(tabuleiro, 'X');
      verificar(tabuleiro, ganhador, placar);
      if (ganhador[0] != '') {
        break;
      }
      play(tabuleiro, 'O');
      verificar(tabuleiro, ganhador, placar);
    }
    print('o placar está ${placar[0]} a ${placar[1]}');
  }
  print('parabens, o jogador ${placar[0] == 2 ? 'X' : 'Y'} ganhou o jogo!!!');
}

void mostrarTabuleiro(tab) {
  int cont = 1;
  print('   1 2 3');
  print(' +-------+');
  for (final i in tab) {
    print('$cont| ' + i[0] + ' ' + i[1] + ' ' + i[2] + ' |');
    cont++;
  }
  print(' +-------+');
}

void play(tab, quem) {
  int x, y;
  if (quem == 'X') {
    y = -1;
    x = -1;
    while (y == -1 || x == -1 || tab[y][x] != ' ') {
      print(
          'qual o seu movimento?(lembre-se que inicialmente marque a casa vertical e depois a horisontal)');
      List<int> lista = input();
      y = lista[0] - 1;
      x = lista[1] - 1;
      if (tab[y][x] != ' ') {
        print('jogada inválida!!!');
      }
    }
  } else {
    x = Random().nextInt(3);
    y = Random().nextInt(3);
    while (tab[y][x] != ' ') {
      x = Random().nextInt(3);
      y = Random().nextInt(3);
    }
  }
  tab[y][x] = '$quem';
}

List<int> input() {
  String? move = stdin.readLineSync();
  bool test(move) {
    List<String> lista = ['1', '2', '3', '4', '5', '6', '7', '8', '9'];
    int letras = 0;
    for (final i in lista) {
      if (move[0] == i) letras++;
      if (move[1] == i) letras++;
    }
    if (letras != 2) return true;
    return false;
  }

  while (move == null || move == '' || move.length != 2 || test(move)) {
    print(
        'você digitou $move, um valor incorreto, tente escrever desta maneira xy.');
    move = stdin.readLineSync();
  }
  print('#$move#');
  return [int.parse(move[0]), int.parse(move[1])];
}

void verificar(tab, ganhador, placar) {
  List<List<List<int>>> casas = [
    [
      [0, 0],
      [0, 1],
      [0, 2]
    ],
    [
      [1, 0],
      [1, 1],
      [1, 2]
    ],
    [
      [2, 0],
      [2, 1],
      [2, 2]
    ],
    [
      [0, 0],
      [1, 0],
      [2, 0]
    ],
    [
      [0, 1],
      [1, 1],
      [2, 1]
    ],
    [
      [0, 2],
      [1, 2],
      [2, 2]
    ],
    [
      [0, 0],
      [1, 1],
      [2, 2]
    ],
    [
      [0, 2],
      [1, 1],
      [2, 0]
    ]
  ];
  for (final i in casas) {
    late String casa = '';
    int verdadeiros = 0;
    for (final j in i) {
      if (casa == '' && tab[j[0]][j[1]] != ' ') {
        casa = tab[j[0]][j[1]];
        verdadeiros++;
      } else if (casa != '' && tab[j[0]][j[1]] == casa) {
        verdadeiros++;
        continue;
      } else {
        break;
      }
    }
    if (verdadeiros == 3) {
      mostrarTabuleiro(tab);
      print('o jogador $casa ganhou!!!!');
      ganhador[0] = casa;
      placar[{'X': 0, 'O': 1}[casa]]++;
    }
  }
}
