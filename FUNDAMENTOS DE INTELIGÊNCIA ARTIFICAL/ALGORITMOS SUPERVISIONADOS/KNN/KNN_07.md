# DESAFIO JEDI - K-NN
## Tabela de Dados Relacionados à Flor Iris

| ID | SepalLength (cm) | SepalWidth (cm) | PetalLength (cm) | PetalWidth (cm) | Species |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 63 | 6.0 | 2.2 | 4.0 | 1.0 | Iris-versicolor |
| 105 | 6.5 | 3.0 | 5.8 | 2.2 | Iris-virginica |
| 83 | 5.8 | 2.7 | 3.9 | 1.2 | Iris-versicolor |
| 33 | 5.2 | 4.1 | 1.5 | 0.1 | Iris-setosa |
| 148 | 6.5 | 3.0 | 5.2 | 2.0 | Iris-virginica |
| 6 | 5.4 | 3.9 | 1.7 | 0.4 | Iris-setosa |
| 124 | 6.3 | 2.7 | 4.9 | 1.8 | Iris-virginica |
| 40 | 5.1 | 3.4 | 1.5 | 0.2 | Iris-setosa |

---

### Dados para Classificação (K-NN)
Utilize o algoritmo para classificar as amostras abaixo:

| ID | SepalLength (cm) | SepalWidth (cm) | PetalLength (cm) | PetalWidth (cm) | Espécie Alvo |
|:---:|:---:|:---:|:---:|:---:|:---:|
| #7 | 4.6 | 3.4 | 1.4 | 0.3 | **?** |
| #72 | 6.1 | 2.8 | 4.0 | 1.3 | **?** |

ID #07

---
D(63) = $\sqrt{(4,6-6,0)^2+(3,4-2,2)^2+(1,4-4,0)^2+(0,3-1,0)^2} =$

D(63) = $\sqrt{(1,96) + (1,44) + (6,76) + (0,49)} =$

D(63) = $\sqrt{} =$

D(63) = 3,26

---
D(105) =  $\sqrt{(4,6-6,5)^2+(3,4-3,0)^2+(1,4-5,8)^2+(0,3-2,2)^2} =$

D(105) = $\sqrt{(3,61) + (0,16) + (19,36) + (3,61)} =$

D(105) = $\sqrt{(26,74)} =$

D(105) = 5,17

---
D(83) =  $\sqrt{(4,6-5,8)^2+(3,4-2,7)^2+(1,4-3,9)^2+(0,3-1,2)^2} =$

D(83) = $\sqrt{(1,44) + (0,49) + (6,25) + (0,81)} =$

D(83) = $\sqrt{(8,99)} =$

D(83) = 2,99

---
D(33) =  $\sqrt{(4,6-5,2)^2+(3,4-4,1)^2+(1,4-1,5)^2+(0,3-0,1)^2} =$

D(33) = $\sqrt{(0,36) + (0,49) + (0,01) + (0,04)} =$

D(33) = $\sqrt{(0,89)} =$

D(33) = 0,95

---
D(148) =  $\sqrt{(4,6-6,5)^2+(3,4-3,0)^2+(1,4-5,2)^2+(0,3-2,0)^2} =$

D(148) = $\sqrt{(3,61) + (0,16) + (14,44) + (2,89)} =$

D(148) = $\sqrt{(21,10)} =$

D(148) = 4,59

---
D(6) =  $\sqrt{(4,6-5,4)^2+(3,4-3,9)^2+(1,4-1,7)^2+(0,3-0,4)^2} =$

D(6) = $\sqrt{(0,64) + (0,25) + (0,09) + (0,01)} =$

D(6) = $\sqrt{(0,99)} =$

D(6) = 0,99

---
D(124) =  $\sqrt{(4,6-6,3)^2+(3,4-2,7)^2+(1,4-4,9)^2+(0,3-1,8)^2} =$

D(124) = $\sqrt{(2,89) + (0,49) + (12,25) + (2,25)} =$

D(124) = $\sqrt{(17,88)} =$

D(124) = 4,23

---
D(40) =  $ \sqrt{(4,6-5,1)^2+(3,4-3,4)^2+(1,4-1,5)^2+(0,3-0,2)^2} =$

D(40) = $\sqrt{(0,25) + (0) + (0,01) + (0,01)} =$

D(40) = $\sqrt{(0,3)} =$

D(40) = 0,52


## Ranking e resultados de proximidade ID #7:

* d(40) = 0,52
* d(33) = 0,95
* d(6) = 0,99 

* d(83) = 2,99 
* d(63) = 3,26 
* d(124) = 4,23
* d(148) = 4,59 
* d(105) = 5,17


## Classificação ID #7 (K-NN)

Com base nas distâncias calculadas:
* **d(40)** = 0,52 (Iris-setosa)
* **d(33)** = 0,95 (Iris-setosa)
* **d(6)** = 0,99 (Iris-setosa)

| Modelo | Vizinhos Próximos (ID) | Classes Envolvidas | Classificação Final |
| :---: | :--- | :--- | :--- |
| **1-NN** | 40 | {Setosa} | **Iris-setosa** |
| **2-NN** | 40, 33 | {Setosa, Setosa} | **Iris-setosa** |
| **3-NN** | 40, 33, 6 | {Setosa, Setosa, Setosa} | **Iris-setosa** |

---

### Análise de Resultados
Como os três vizinhos mais próximos da amostra **#7** pertencem à mesma categoria, a classificação é consistente em todos os níveis de $K$ testados.