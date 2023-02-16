import 'dart:io';

void main(List<String> args) {
  String? media;
  print('digite a média do aluno');
  media = stdin.readLineSync();
  while (media == null) {
    print('digite a média do aluno');
    media = stdin.readLineSync();
  }
  print(verificar(double.parse(media)));
}

String verificar(double media) {
  if (media > 10)
    return 'media inválida';
  else if (media > 8.9)
    return 'A';
  else if (media > 6.9)
    return 'B';
  else if (media > 4.9)
    return 'C';
  else
    return 'D';
}
