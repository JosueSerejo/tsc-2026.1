def analisar_notas(notas):
  if not notas:
    raise ValueError("A lista de notas não pode estar vazia")

  for nota in notas:
    if not isinstance(nota, (int, float)):
      raise TypeError(f"Elemento '{nota}' não é numérico")

    if nota < 0 or nota > 10:
      raise ValueError(f"Nota {nota} fora do intervalo permitido (0 a 10)")

  notas_ordenadas = sorted(notas)
  n = len(notas_ordenadas)

  media = sum(notas_ordenadas) / n
  
  if n % 2 == 0:
    mediana = (notas_ordenadas[n // 2 - 1] + notas_ordenadas[n // 2]) / 2
  else:
    mediana = notas_ordenadas[n // 2]

  aprovados = sum(1 for nota in notas if nota >= 6.0)
  reprovados = n - aprovados

  maior = max(notas_ordenadas)
  menor = min(notas_ordenadas)

  if media >= 8:
    situacao_turma = 'A'
  elif media >= 5:
    situacao_turma = 'B'
  else:
    situacao_turma = 'C'

  return {
    'media': round(media, 2),
    'mediana': round(mediana, 2),
    'aprovados': aprovados,
    'reprovados': reprovados,
    'maior': maior,
    'menor': menor,
    'situacao_turma': situacao_turma
  }