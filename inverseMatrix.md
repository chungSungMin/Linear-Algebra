역행렬을 구하는것은 간단하게 가우스 조던 소거법을 통해서 구할수 있습니다.

가우스 조던 소거법의 경우 행렬A를 항등 행렬로 만들면서 각각의 값들을 구하게 되는 것 입니다.

2차원 행렬 에서 역행렬은 아래와 같습니다.

$$
A = {a b \brack c d}
$$

$$
A^{-1} = { 1 \over ad -bc } {d -b \brack -c a }
$$

위의 식에서 $ad -bc$ 가 바로 determinant입니다. 해당 값이 0이 되면 수학적으로 정의가 되지 않기에 det(A) ≠ 0 이되어야 역행렬이 정의될수 있게 됩니다.

행렬 A invertable하다 라는 것은 결국에는 행렬 A의 역행렬이 존재하는것이고, 이는 기하학적으로 생각 해보면 결국 어떠한 점이라도 고차원에서 저차원으로 매핑되지 않는다는 것을 의미합니다. 즉 $Ax = 0$ 을 만족하는 벡터가 0벡터 뿐이라는것을 의미합니다.

만일 Null space가 존재하는 경우 해당 벡터들은 선형 변환을 통해서 0벡터로 매핑되고 이를 다시 되돌릴 수가 없기 때문에 A 행렬이 invertable하지 않게 됩니다. 그리고 determinant가 결국 면적을 의미하게 되는데 이를 3차원에서 보면 만약 3차원에서 2차원 혹은 1차원을 span하게 되면 부피가 0이 됩니다.결국에는 Det(A)가 0이 되면 안 된다는 말이 결국에는 Null space가 없다라는 것을 의미하게 됩니다. 

즉, 아래와 같은 조건을 만족해야지 행렬 A가 invertable하다 라는것 입니다.

<aside>
📢

1. Det(A) ≠ 0
2. N(A) = 0
3. Full rank여야 한다
</aside>