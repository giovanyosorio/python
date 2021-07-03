function matriz(input) {
  var cont = 0;

  for (let index = 0; index < input.length; index++) {
    cont++;
    const element = input[index];
    console.log(cont);
    console.log(element);
  }
}

matriz("5");
