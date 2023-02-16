import 'dart:io';

void main() {
  Pessoa pessoa = Pessoa('Cauan', '123.456.789.12', 'xxxxx-xxxxx', '+55 (49) 912345678');
  print(pessoa.getName);
  print(pessoa.getCpf);
  print(pessoa.getEndereco);
  print(pessoa.getTelefone);
}

class Pessoa{
    String nome;
    String cpf;
    String endereco;
    String telefone;
    
    void set nameChange(String novoNome){
        nome = novoNome;
    }
    void set cpfChange(String novoNome){
        nome = novoNome;
    }
    void set enderecoChange(String novoNome){
        nome = novoNome;
    }
    void set telefoneChange(String novoNome){
        nome = novoNome;
    }
    String get getName{
        return nome;
    }
    String get getCpf{
        return cpf;
    }
    String get getEndereco{
        return endereco;
    }
    String get getTelefone{
        return telefone;
    }
    Pessoa(this.nome, this.cpf, this.endereco, this.telefone);
} 