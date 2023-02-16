import 'dart:io';

void main(List<String> args) {
  String? x, y;
  print('digite o valor de x');
  x = stdin.readLineSync();
  while (x == null) {
    print('digite o valor de x');
    x = stdin.readLineSync();
  }
  print('digite o valor de y');
  y = stdin.readLineSync();
  while (y == null) {
    print('digite o valor de y');
    y = stdin.readLineSync();
  }
  print(verificar(int.parse(x), int.parse(y)));
}

int verificar(int x, int y) {
  if (x % y != 0) return 0;
  return 1;
}
