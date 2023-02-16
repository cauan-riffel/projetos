import 'dart:io';

void main(List<String> args) {
  String? num;
  print('digite um número para ser escrito por extenso');
  num = stdin.readLineSync();
  while (num == null || int.parse(num) < 1 || int.parse(num) > 20) {
    print('digite um número para ser escrito por extenso');
    num = stdin.readLineSync();
  }
  print(porExtenso(int.parse(num)));
}

String porExtenso(int num) {
  List<String> lista = [
    'um',
    'dois',
    'três',
    'quatro',
    'cinco',
    'seis',
    'sete',
    'oito',
    'nove',
    'dez',
    'onze',
    'doze',
    'treze',
    'quatorze',
    'quinze',
    'dezesseis',
    'dezessete',
    'dezoito',
    'dezenove',
    'vinte'
  ];
  return lista[num - 1];
}
