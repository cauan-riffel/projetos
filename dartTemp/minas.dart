import 'dart:io';

void main() {
  print('\n' * 100);
  int level = definirDificuldade('dificuldade');
  List<List<String>> campo = criarCampo(level);
  {
    int x = 0;
    while (x != campo[0].length) campo[0][x++] = '';
  }
  mostrarTabuleiro(campo);
  inputJogada(campo, true);
  // modificarCampo(campo);
  // while (possivel(campo)) {
  //   mostrarTabuleiro(campo);
  //   inputJogada(campo);
  // }
}

int definirDificuldade(String what) {
  if (what == 'dificuldade') {
    String? level;
    while (level == null || level == 'help') {
      print('digite o nivel que quiser, caso tenha dúvidas digite help.');
      level = stdin.readLineSync();
      if (level == null)
        print('não digite valores núlos.\n\n\n');
      else if (level == 'help') {
        print(
            '\n\n\n\n\n\n\n\n\neasy: campo minado 8x10 com 10 bombas\nmedium: campo minado 16x18 com 40 bombas\nhard: campo minado 20x24 com 99 bombas\n\n');
      } else if (level == 'easy') {
        return 1;
      } else if (level == 'mediun') {
        return 2;
      } else if (level == 'hard') {
        return 3;
      } else {
        print(
            '\n\n\n\n\n\n\n\n\nvalor inserido é incorreto, em caso de dúvida digite help.\n\n');
      }
    }
  }
  return 1;
}

List<List<String>> criarCampo(int level) {
  List<List<String>> campo = [];
  List<int> tipo = [
    (level == 1)
        ? 8
        : (level == 2)
            ? 16
            : 20,
    (level == 1)
        ? 10
        : (level == 2)
            ? 18
            : 24
  ];
  while (tipo[0] != 0) {
    int x = tipo[1];
    List<String> lista = [];
    campo.add(lista);
    while (x != 0) {
      lista.add(' ');
      x--;
    }
    tipo[0]--;
  }
  return campo;
}

void mostrarTabuleiro(List<List<String>> campo) {
  int x = 0;
  stdout.write('   ');
  while (x < campo[0].length) {
    stdout.write(' ${x + 1} ');
    x++;
  }
  print('');
  stdout.write('  +' + '-' * (campo[0].length * 3 + 15) + '+');
  print('');
  x = 0;
  while (x < campo.length) {
    int y = 0;
    stdout.write('${x + 1}');
    if (x < 9) stdout.write(' ');
    stdout.write('|');
    while (y < campo[x].length) {
      stdout.write(' ${campo[x][y]} ');
      if (y >= 9) stdout.write(' ');
      y++;
    }
    print('|${x + 1}');
    x++;
  }
  stdout.write('  +' + '-' * (campo[0].length * 3 + 15) + '+');
  print('');
  x = 0;
  stdout.write('   ');
  while (x < campo[0].length) {
    stdout.write(' ${x + 1} ');
    x++;
  }
  print('');
}

void inputJogada(List<List<String>> camp, [bool ft = false]) {
  int? x, y;
  String? jogada = null;
  if (ft) {
    jogada = 'abrir';
  } else {
    while (jogada == null || jogada == 'help') {
      print('qual jogada deseja realizar?\nabrir');
      jogada = stdin.readLineSync();
      if (jogada == 'abrir' ||
          jogada == 'bandeira' ||
          jogada == 'tirar bandeira') {
        break;
      } else if (jogada == 'help') {
        print(
            'abrir: irá abrir o terreno e caso o local selecionado seja uma bomba, você perde\nbandeira: colocorá uma bandeira no campo que irá evitar que o jogador abra o terreno onde estiver uma bandeira\ntirar bandeira: irá retirar uma bandeira que o jogador selecionará.');
      } else {
        print('Você digitou o comando errado, por favor tente novamente');
      }
    }
  }
  print('Digite o numero da linha que você realizará a sua jogada!!');
  String? tempY = stdin.readLineSync();
  while (
      tempY == null || int.parse(tempY) < 0 || int.parse(tempY) > camp.length) {
    print('jogada inválida! Favor jogar novamente');
    tempY = stdin.readLineSync();
  }
  y = int.parse(tempY);
  print('Digite o numero da linha que você realizará a sua jogada!!');
  String? tempX = stdin.readLineSync();
  while (
      tempX == null || int.parse(tempX) < 0 || int.parse(tempX) > camp.length) {
    print('jogada inválida! Favor jogar novamente');
    tempX = stdin.readLineSync();
  }
  x = int.parse(tempX);
}
