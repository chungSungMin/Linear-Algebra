eigen decomposition이란 행렬 A를 eigen vector와 eigen value로 분해할수 있다는 것을 의미합니다.

Eigen Decomposition을 할수 있는 가정은 행렬 A가 N x N인 경우 independent한 eigen value가 N개 존재야합니다.

행렬 A가 2x2 크기이고 서로다른 eigen value와 eigen vector가 2개 씩 존재한다는 가정하고 이를 증명해보면 아래와 같습니다.

$$
Av_1 = \lambda_1v_1
$$

$$
Av_2 = \lambda_2v_2
$$

다음과 같이 나타낼수 있습니다. 그리고 이를 한번에 표현해보면 아래와 같이 표현해볼 수 있습니다.

$$
A[v_1, v_2] = [\lambda_1v_1, \lambda_2v_2]
$$

그리고 $[\lambda_1v_1, \lambda_2v_2]$ 해당 식을 다르게 표현하면 $[v_1, v_2]\begin{bmatrix} \lambda_1 0 \\ 0 \lambda_2 \end{bmatrix}$다음과 같이 표현해볼 수 있습니다. 그리고 우리가 위에서 가정했듯이 v1, v2는 independent하기에 각 항에 역행렬을 곱해줄수 있습니다.

그래서 $[v_1, v_2]$ 를 V라고 치환을하고 $\begin{bmatrix} \lambda_1 0 \\ 0 \lambda_2 \end{bmatrix}$ 을 $\Lambda$로 치환을 해서 표현해보면 아래와 같이 표현이 됩니다.

$$
A = V\Lambda V^{-1}
$$

이를 통해서 우리는 행렬 A를 다음과 같이 분해할수 있습니다. 이렇게 eigen value와 eigen vector를 통해서 행렬 A를 분리하는 것을 Eigen Decomposition이라고 하는 것 입니다.

그리고 추가적으로 $V^{-1}AV = \Lambda$ 로현할수 있는데, 이떄 $\Lambda$가 diagonal matrix이기 때문에 행렬 A를 대각행렬로 만든다라고 해서 행렬 A가 diagonalizable하다 라고 한다고 합니다. 즉 A라는 행렬을 대각행렬로 만들 수 있다는 것입니다.

이를 다시 정리해보면 행렬 A가 Eigen Decomposition 된다 = A가 diagonalizable하다 = A가 N개의 linear independent한 eigen vector가 존재한다 로 정리해볼수 있습니다.

Eigen Decomposition의 장점

1. $A^K$  를 구하기 쉽다. $(V^{-1}\Lambda V)(V^{-1}\Lambda V)...(V^{-1}\Lambda V)$ 이 반복되고 결국에는 $(V^{-1}\Lambda^K V)$ 만 남게 되기 떄문입니다.
2. $A^{-1}$을 구하기 쉽습니다.
3. det(A)을 구하기 쉽습니다. 왜냐하면 $\lambda_1 \lambda_2 ... \lambda_n$ = det(A)이기 때문이다. ( $det(V^{-1})det(\Lambda)det(V)$ 인데 역행렬의 det() 역수이기에 제거 되어 결국 대각 행렬만 남기 떄문이다. 즉 $\prod^n_{i=1}\lambda_i$ = det(A)이다.
4. tr(A)를 구하기 쉽다. $\sum^n_{i=1}\lambda_i$  = tr(A) 이기 떄문이다
5. 만일 A라는 행렬이 rank deficient 하다면 결국 eigen value가 적어도 하나는 0임을 암시합니다.

알아두면 좋은점

1. $A^T$의 eigen value와 A의 eigen value는 동일하다.
2. A가 orthogonal하다면 eigen value는 +1 혹은 -1만 갖게 된다.
(수식적으로 자신을 dot product해보면 자연스럽게 eigen value의 제곱이 1이 나와야한다 )
3. Diagonalizable matrix의 non-zero eigein value의 수 = rank(A)이다. ( 어차피 V, $V^{-1}$ 은 full rank이니 결국 $\Lambda$에 달렸는데 이는 eigen value로 이루어져있기 떄문이다 )

추가적으로 행렬 A가 symmetric ( $A = A^T)$  한 행렬인 경우 더욱 특별한 해석이 가능해 집니다.

symmetric 행렬의 큰 특징은 $A = A^T$ 입니다. 이에 우리가 위해서 했던 eigen decomposition을 적용해서 나타내면 아래와 같이 나타낼수 있습니다.

$$
V\Lambda V^{-1}  =(V\Lambda V^{-1})^T
$$

이는 결국 $V\Lambda V^{-1} = V^{-T}\Lambda^TV^T$ 으로 표현할수 있습니다.

여기서 중요한점은 바로 $V^{-1} = V^T$ 라는 점 입니다. 즉 eigen vector들이 모두 orthonormal vector들 이라는 사실입니다. 그래서 우리는 (3 x 3 ) 크기의 orthognonal matrix를 Q라고 치환해서 이게 어떤걸 의미하는지 알아보도록 하겠습니다.

$$
A = Q\Lambda Q^T
$$

$$
A = [q_1, q_2, q_3] \begin{bmatrix} \lambda_1 0 0 \\ 0 \lambda_2 0 \\ 0 0 \lambda_3 \end{bmatrix} \begin{bmatrix} q_1^T \\ q_2^T \\ q_3^T \end{bmatrix}
$$

결국 다음과 같이 표현이 가능이 가능하게 됩니다. 이를 다시 정리해보면 아래와 같이 표현이 가능해 집니다.

$$
A = \lambda_1q_1q_1^T + \lambda_2q_2q_2^T + \lambda_3q_3q_3^T
$$

이를 자세히 살퍄보면 q벡터 자체는 orthonormal vector로 결국에는 각각이 rank = 1인 matrix가 됩니다. 즉 행렬 A를 rank = 1인 matrix로 분해하게 됩니다. 그리고 각각의 값들은 각 벡터의 차원을 의미하게 됩니다.


<img width="244" alt="image" src="https://github.com/user-attachments/assets/90f801db-6acb-4dc9-9776-de53221a6cd8" />

<br>
위 사진 처럼 A라는 빛이 들어오고 이들을 각각의 색상으로 분해하는 것을 의미한다고 저는 생각헀습니다. 각 색상은 단일 색상으로 Rank = 1 이 되게 됩니다.

이는 결국에는 데이터 축소에도 사용이 가능합니다. 예를들어 행렬 A가 N개의 eigen vector들로 분해가 되는 경우 이중에서 eigen value가 큰 M개 ( M < N ) 개의 차원을 이용해서 데이터를 압축 해서 표현할수 있게 됩니다.

그렇다면 특정 x 라는 벡터를 symmetric A를 통해서 선형변환 하면 어떻게 될까요?

$$
Ax = \lambda_1q_1q_1^Tx + \lambda_2q_2q_2^Tx + \lambda_3q_3q_3^Tx
$$

 다음과 같이 나타낼수 있습니다. 근데 여기서 중요한점은 바로 $q_nq_n^Tx$ 입니다. 우리가 이전에 Least Square에 대해 배웠는데, 그때 특정 벡터 x를 우리가 span할 수 있는 차원에서 표현할 때 특정 벡터에 projection matrix를 곱한다고 했스니다. projection matrix의 식을 살펴보면 아래와 같습니다.

$$
A(A^TA)^{-1}A^T
$$

하지만 현재 matrix는 symmetric이기에 Q로 대신해서 표현해보면 

$$
Q(Q^TQ)^{-1}Q^T
$$

입니다. 하지만 여기서 중요한 점은 Q를 decomposition시 모든 vector들이 orthonormal이기에 $Q^TQ = 1$ 이 됩니다. 그래서 결국 projection matrix가 $QQ^T$가 됩니다. 결국 우리가 위에서 봤던 $q_nq_n^Tx$ 가 의미하는게 각 x에 대해서 각 q라는 차원에 projection 내린것을 의미합니다. 
결국 x라는 벡터를 각 차원에 대해서 얼마나 영향을 미치는지 나타내게 됩니다. 이후 $\lambda$ 만큼 scale을 조절하여 더해서 Ax를 만들게 됩니다.

만일 모든 $\lambda$가 $\lambda = 1$을 만족하는 경우 Ax = x가 되게 됩니다. 왜냐면 x를 각 차원에 projection 시킨 후 단순히 다시 합치는 과정이기 떄문입니다. 그리고 Q라는 행렬 자체가 $I$ 행렬이 되기 떄문입니다.

<aside>
📢

정리

</aside>

N * N 정사각 행렬 A가 N개의 eigen value, vector를 갖는 경우 행렬 A를 아래와 같이 분해할수 있습니다.

$$
A = V\Lambda V^{-1}
$$

이렇게 분해 가능한 A를 diagonalizable 하다고 할수 있습니다.

만일 행렬 A가 symmetric 인 경우에는 rank(A) = non zero eigen value 갯수를 의미합니다. 그리고 추가로 행렬 A가 대칭행렬이면 아래와 같이 표현이 가능해집니다.

$$
A = Q\Lambda Q^T
$$

즉, eigen vector들이 모두 직교하는 orthogonal matrix로 분해할수 있다는 것 입니다.
