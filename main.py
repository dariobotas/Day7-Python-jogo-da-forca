import random


def escolher_palavra():
  palavras = ['casa', 'carro', 'computador', 'celular', 'notebook']
  palavra = random.choice(palavras)
  return palavra


def jogar():
  palavra = escolher_palavra()
  palavra_completa = "_" * len(palavra)
  tentativas = 6
  letras_erradas = []
  letras_certas = []

  print("Vamos jogar o jogo da forca!")

  while tentativas > 0 and "_" in palavra_completa:
    print(f"Palavra: {palavra_completa}")
    print(f"Tentativas restantes: {tentativas}")
    letra = input("Digite uma letra: ")

    if letra in palavra:
      letras_certas.append(letra)
      indices_letra = [i for i in range(len(palavra)) if palavra[i] == letra]
      for indice in indices_letra:
        palavra_completa = palavra_completa[:indice] + letra + palavra_completa[
          indice + 1:]
    else:
      letras_erradas.append(letra)
      tentativas -= 1

    print(f"Letras erradas: {letras_erradas}")
    print(f"Letras corretas: {letras_certas}")

  if "_" not in palavra_completa:
    print(f"Parabéns! Você ganhou! A palavra era {palavra}.")
  else:
    print(f"Você perdeu! A palavra era {palavra}.")

jogar()
