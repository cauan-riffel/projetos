import 'dart:io';

void main(List<String> args) {
  String? idade;
  print('digite a idade do nadador');
  idade = stdin.readLineSync();
  while (idade == null) {
    print('digite a idade do nadador');
    idade = stdin.readLineSync();
  }
  print(verificar(int.parse(idade)));
}

String verificar(int idade) {
  if (idade > 17)
    return 'adulto';
  else if (idade > 13)
    return 'juvenil B';
  else if (idade > 10)
    return 'juvenil A';
  else if (idade > 7)
    return 'infantil B';
  else if (idade > 4)
    return 'infantil A';
  else
    return 'não aceitamos menores de 5 anos';
}
