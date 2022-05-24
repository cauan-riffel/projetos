function rangeOfNumbers(numInicial, numFinal) {
    if (numFinal == numInicial) {
      return [numFinal];
    }else {
       const lista = rangeOfNumbers(numInicial, numFinal-1);
      lista.push(numFinal);
      return lista;
    }
}
alert(rangeOfNumbers(Number(prompt('qual o valor de inicio da função? ')), Number(prompt('qual o valor final da função? '))));
alert(i)
