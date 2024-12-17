PCA의 한계를 극복하기 위해서 나온 알고리즘 방식이다.

PCA의 한계 :

1. A가 정사각행렬이어야 한다.
2. A가 Symmetric Matrix여야 한다
    
    

SVD를 수식으로 표현하면 아래와 같습니다.

$$
A = U\Sigma V^T
$$

위와 같이 행렬 A를 $U와 V^T$ 라는 2개의 orthogonal matrix와 정사각 행렬인 $\Sigma$ 로 분해할수 있다는 것 입니다.

$A^TA$  행렬이 바로 대칭행렬 이라는 점을 이용해서 증명하게 됩니다.

$$
AA^T = (U\Sigma V^T)(U\Sigma V^T)^T
$$

$$
AA^T = (U\Sigma V^T)(V\Sigma^T U^T)
$$

$$
AA^T = U\Sigma \Sigma^T U^T
$$

위와 같이 표현할수 있습니다. 다음과 같이 전개가 되는 이유는 $V$ 라는 행렬 이orthogonal 행렬이기에 $VV^T$ 가 $I$ 행렬이 되기 떄문에 사라지게 되기에 위와 같은 식을 얻을수 있다.

이를 우리가 앞서 배운 Eigen Decomposition을 통해서 (  $AA^T$ 함수가 symmetric 하기에 eigen decomposition가능) 해당 값들을 구할수 있게 됩니다.

즉 아래와 같은 부등식을 세울수 있습니다.

$$
U\Sigma \Sigma^T U^T = Q\Lambda Q^T
$$

즉 $U$ 라는 행렬이 결국에는 $AA^T$ 의 Eigen vector가 되게 됩니다. 
그리고 $\Sigma \Sigma^T$ 행렬과 eigen value의 행렬이 동일하기 때문에 $\Sigma$는 결국 eigen value의 양의 제곱근의 행렬입니다.

이와 동일하게 $A^TA$ 행렬로 Eigen Decomposition을 진행하게 되면 $U$와 비슷하게 $V$를 얻게 됩니다.

그리고 이러한 행렬 A로 선형변환을 한다는 것을 기하학적으로 살펴보면 다음과 같습니다.

$$
A = U\Sigma V^T
$$

$$
AV = U\Sigma
$$

$$
A[v_1, v_2, ..., v_n] = [\sigma_1v_1 + \sigma_2v_2, ...., \sigma_nv_n]
$$

같이 표현을 할수있습니다. ( V 행렬이 orthogonal이기에 역행렬과 전치행렬이 동일하기 때문입니다. )

그래서 결국 A라는 행렬로 선형변환을 시킨다면 만일 서로 수직인 벡터들이 들어오게 되면 결과 또한 서로 수직인 관계를 유지하면서 scale이 조금 달라지게 되는 변환임을 의미합니다.

그리고 orthogonal matrix의 eigen value들은 +1 혹은 -1 값만 가지게 되기 떄문에 A라는 선형 변환을 하게 되면 U, $V^T$ 을 지나면 크기는 변하지 않고 단순히 방향이 바뀌고 $\Sigma$ 행렬을 통해서 스케일이 조절됨을 알수 있습니다.

즉 $V^T$ 행렬을 통해서 벡터가 반사, 뒤집혀지고, $\Sigma$ 행렬을 통해서 각 차원 별로의 영향력을 증가/감소를 시키고 $U$행렬을 통해서 다시 원래 좌표계로 반사, 뒤집어 주게 됩니다.
