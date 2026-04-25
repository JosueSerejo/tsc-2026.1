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

## ID #72

---
D(63) = $\sqrt{(6,1-6,0)^2+(2,8-2,2)^2+(4,0-4,0)^2+(1,3-1,0)^2} =$

D(63) = $\sqrt{() + () + () + ()} =$

D(63) = $\sqrt{} =$

D(63) = 

---
D(105) =  $\sqrt{(6,1-6,5)^2+(2,8-3,0)^2+(4,0-5,8)^2+(1,3-2,2)^2} =$

D(105) = $\sqrt{() + () + () + ()} =$

D(105) = $\sqrt{()} =$

D(105) = 

---
D(83) =  $\sqrt{(6,1-5,8)^2+(2,8-2,7)^2+(4,0-3,9)^2+(1,3-1,2)^2} =$

D(83) = $\sqrt{() + () + () + ()} =$

D(83) = $\sqrt{()} =$

D(83) = 

---
D(33) =  $\sqrt{(6,1-5,2)^2+(2,8-4,1)^2+(4,0-1,5)^2+(1,3-0,1)^2} =$

D(33) = $\sqrt{() + () + () + ()} =$

D(33) = $\sqrt{()} =$

D(33) = 

---
D(148) =  $\sqrt{(6,1-6,5)^2+(2,8-3,0)^2+(4,0-5,2)^2+(1,3-2,0)^2} =$

D(148) = $\sqrt{() + () + () + ()} =$

D(148) = $\sqrt{()} =$

D(148) = 

---
D(6) =  $\sqrt{(6,1-5,4)^2+(2,8-3,9)^2+(4,0-1,7)^2+(1,3-0,4)^2} =$

D(6) = $\sqrt{() + () + () + ()} =$

D(6) = $\sqrt{()} =$

D(6) = 

---
D(124) =  $\sqrt{(6,1-6,3)^2+(2,8-2,7)^2+(4,0-4,9)^2+(1,3-1,8)^2} =$

D(124) = $\sqrt{() + () + () + ()} =$

D(124) = $\sqrt{()} =$

D(124) = 

---
D(40) =  $ \sqrt{(6,1-5,1)^2+(2,8-3,4)^2+(4,0-1,5)^2+(1,3-0,2)^2} =$

D(40) = $\sqrt{() + () + () + ()} =$

D(40) = $\sqrt{()} =$

D(40) = 


## Ranking e resultados de proximidade ID #7:

* d(40) = 
* d(33) = 
* d(6) =  
* d(83) = 
* d(63) = 
* d(124) = 
* d(148) =  
* d(105) = 


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