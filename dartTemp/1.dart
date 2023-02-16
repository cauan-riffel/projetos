import 'dart:io';

void main() {
  List<String> meses = [
    'janeiro',
    'fevereiro',
    'março',
    'abril',
    'maio',
    'junho',
    'julho',
    'agosto',
    'setembro',
    'outubro',
    'novembro',
    'dezembro'
  ];
  print('digite o número do mês que deseja saber.');
  String? input = stdin.readLineSync();
  while (input == null || !(int.parse(input) >= 1 && int.parse(input) <= 12)) {
    print('valor incorreto');
    print('digite o número do mês que deseja saber.');
    input = stdin.readLineSync();
  }
  print(meses[int.parse(input) - 1]);
}
