# Soma Alvo

O script principal de vocês deve estar no arquivo `main.py`.

## 📝 Instruções 📝

Complete o arquivo `main.py` alterando a função `target_sum` para que ela receba uma lista de inteiros e um número alvo, ela deve retornar os dois números que na lista somados deem o alvo.
O resultado deve ser uma tupla com os dois números.
O primeiro número da tupla deve ser o menor número e o segundo número da tupla deve ser o maior número.
Se a lista tiver menos de dois números, a função deve retornar `None`.
Se não existirem números na lista que somados deem o alvo, a lista deve retornar `None`.

## 🧑‍💻 Exemplo de Execução 🧑‍💻

```python
>>> lista1 = [1, 2, 3, 4, 5]
>>> target_sum(lista1, 7)
(3, 4)

>>> lista2 = [10, -5, 20, 15, -30]
>>> target_sum(lista2, -10)
(-30, 10)

>>> lista3 = [0, 0, 0, 0]
>>> target_sum(lista3, 0)
(0, 0)

>>> lista4 = [-10, -5, -2, -1]
>>> target_sum(lista4, -3)
(-2, -1)

>>> lista5 = [5]
>>> target_sum(lista5)
None

>>> lista6 = [2, 4, 5]
>>> target_sum(lista6, 10)
None
```

## ❗ IMPORTANTE ❗

Veja as instruções sobre como proceder com o exercício no link [Instruções Gerais Para os Exercícios](https://github.com/ProfRonan/python-exercise-instructions).
