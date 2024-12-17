PCA(Principal Component Analysis) 는 데이터를 가장 잘 설명하는 vector를 찾는 방법입니다.

<img width="671" alt="image" src="https://github.com/user-attachments/assets/3d310065-0fb7-4c7f-9fb6-871a34b11525" />

<br>

다음과 같이 해당 데이터를 가장 잘 설명하는 빨간색 vector가 존재한다고 합시다. 이때 임의이 x에 대해서 빨간 vector와의 차이를 구하게 되면 파란색처럼 error vector를 구할수 있게 됩니다. PCA는 이렇게 error vector의 크기를 최소하하는 방법입니다. 

이를 수식으로 표현해보면 아래와 같이 표현할 수 있습니다. 이떄 우리가 모든 데이터 $d$에  대해서 모듬 데이터들의 평균을 빼서 평균 = 0 으로 만들기 위해서 $\tilde{d} = d_i - \bar{d}$를 구했다고 설정을 합니다.  그리고 주성분 벡터를 $U$ 벡터라고 가정을 하게 되면 자연스럽게 error vector의 크기는  $\|d_i - d_i^TUU\|_2^2$  다음과 같이 정의할 수 있습니다. 그리고 만일 U 벡터 자체가 너무 작아지게 되면 데이터와는 상관없이 error vector의 크기가 작아지게 되기에 U벡터의 크기는 1로 가정을 하게 됩니다. 즉 아래와 같은 수식을 풀게 됩니다.

$$
{1 \over n } \sum^n_{i=1}\|d_i - d_i^TUU\|^2_2
$$

위의 식을 minimize 하게 됩니다. 그리고 가정으로 아래와 같은 조건을 만족해야합니다.

$$
S.T) \|U\|_2^2 = 1
$$

해당 식을 만족해야합니다. 우선 위의 mimize해야하는 식을 전개하면 아래와 같은 식을 얻을수 있게 됩니다.

$$
-U^T {1 \over N} \sum^n_{i-1}(\tilde{d_i} - \tilde{d})(\tilde{d_i} - \tilde{d})^TU
$$

여기서 중요한 것은 바로 $(\tilde{d_i} - \tilde{d})(\tilde{d_i} - \tilde{d})^T$ 값이 결국 covariance matrix가 된다는 것입니다.

즉, covariance를 최대화 하는것이 결국 해당 식을 최소화하는 방향이라는 결과를 얻게 됩니다. 추가적으로 covariance matrix의 경우 symmetric matrix입니다. 

그래서 PCA는 데이터의 분산이 가장 큰 방향을갖게 되는것 입니다.

그리고 마저 해당 식을 풀기 위해서는 Lagrange multiplier를 사용해서 풀수 있습니다. 왜냐하면 U 벡터의 길이가 1이어야 하는 가정이 필요하기 때문입니다.

라그랑주 승수법을 통해서 해당 식을 풀게되면 $R_dU = \lambda U$ 라는 식을 얻게 됩니다. ( $R_d$는 covariance matrix를 의미합니다 ) 즉, PCA는 결국 eigen vector중에 존재하게 됩니다. 그렇다면 우리는 조건이 있는 최적화 문제를 풀었으니 해당 값을 만족하기 위해서  ( $-U^T {1 \over N} \sum^n_{i-1}(\tilde{d_i} - \tilde{d})(\tilde{d_i} - \tilde{d})^TU$ 해당 값을 minimize말고 max로 풀었습니다. ) 조건이 만족하는 값 내에서 가장 큰 값을 골라야합니다. 
이는 곧 가장 큰 eigen value를 갖는 eigen vector가 됩니다. 

최종적으로 PCA는 convariance 행렬에서 가장 큰 eigen value를 갖는 eigen vector가 되고, 이는 결국 covariance를 최대화하는 방향입니다. 그리고 그 다음으로 데이터를 가장 잘 설명하는 vector는 다음으로 큰 eigen value를 갖는 eigen vector가 됩니다. 그리고 covariance maxtirx는 orthogonal matrix이기에 자연스럽게 모든 vector들이 직교하게 됩니다. 그래서 2차원에서 PCA를 구할때 두번째로 데이터를 잘 설명하는 벡터가 데이터를 가장 잘 설명하는 벡터와 수직 관계를 이루게 됩니다.

### 정리

PCA는 데이터를 가장 잘 표현하는 vector를 찾는 문제이다. 그래서 데이터와 vector들사이의 에러를 줄이기 위해서 식을 전개해보면 결국에는 covariance를 최대화하는 방향으로 가야 error를 최소화할수 있습니다. 그리고 라그랑주 승수법을 통해서 식을 풀게되면 최적의 vector들이 바로 covariance matrix의 eigen vector들이고, 그중 가장 영향력이 큰 vector는 가장 큰 eigen value를 갖는 eigen vector가 되게 됩니다.
