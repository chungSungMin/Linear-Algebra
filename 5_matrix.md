## 역행렬 (inverse matrix)

$$
A A^{-1} = I
$$

이를 만족하는 $A^{-1}$을 A의 역행렬이라고 합니다.

$A^{-1}$은 정사각행렬로 정의하고 A에 따라서 inverse matrix가 존재할수 도 있고, 존재하지 않을수도 있습니다. 그리고 A의 역행렬이 존재하는 경우 A는 invertable 하다라고 합니다.

## Diagonal Matrix

대각 행렬로 대각 성분을 제외하고 모든 element 의 값이 0 인행렬을 의미합니다

대부분의 경우 정사각행렬을 의미합지만, 가끔 Rectangular diagonal이라고 정사각행렬이 아닌 대각행렬이 존재하긴 합니다.

그리고 주로 논문에서 D = diag(A)라는 수식을 주로 사용하는데 이는 대각행렬에 벡터 A 값을 채워 넣으라는 간단한 의미로 사용됩니다.

## Orthogonal Matrix

Orthgonal Matrix는 모든 column vector들이 서로 직교이면서 벡터의 크기가 1인 행렬을 의미합니다.

그리고 이렇게 서로 수직인 벡터들을 Orhonormal vector라고 부른다고 합니다.

즉 Orthogonal Matrix는 orthonormal vector들의 집합이라고 할수 있습니다.

<img width="246" alt="image" src="https://github.com/user-attachments/assets/1a3a6568-15d4-46ba-960d-ca000b3e055c" />

<br>

그리고 Orthogonal matrix의 최대의 정점은 아래와 같습니다.

$$
A^{-1} = A^T
$$

A의 역행렬과 A의 전치행렬이 동일하다는것 입니다.

이게 가능한 이유는 Matrix 곱을 내적의 관점에서 보면 dot product가 동일한 차원을 제외하고 0이 되어야지 I 행렬을 만들수 있습니다. 그런데 Orthogonal matrix의 경우 모든 벡터들이 수직이기에 0이 되지 않기위해서는 자기 자신과 dot product를 해야합니다. 그래서 자연스럽게 Orthogonal Matrix의 역행렬이 전치행렬이 되게 됩니다.
<br>

<img width="252" alt="image" src="https://github.com/user-attachments/assets/61751073-236c-45a0-93a3-db11eca293d1" />



