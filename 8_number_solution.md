## Full Column Rank인 경우 ( 해 = 1개 혹은 0개 ):

A행렬이 (10,3) 크기를 갖는다고 가정해 봅시다. 이때는 full column rank이기에 총 3차원을 span하게 됩니다. 그러면 x 벡터들도 3 * N 차원이 되게 됩니다. 그리고 최종적으로 그려진 결과 또한 10 * N으로 10차원을 갖게됩니다. 이때 10차원에서 오직 3차원만을 span하기 때문에 만약 정답이 존재하는 경우 1개의 정답을 갖게되고, 3차원 내에 있지 않는 벡터에 대해서는 표현할수가 없게 됩니다.

## Full Row Rank인 경우 (해 = 무한개 ):

A행렬이 (3, 10) 크기를 갖는다고 가정해 봅시다. 이때는 full row rank이기에 총 3차원을 span할수 있습니다. 그리고 x벡터들은 10 * N 크기를 갖게 됩니다. 그러면 최종적으로 3 * N 크기의 결과를 얻게 되는데, 결국 결과가 3차원만을 표현할수 있습니다.근데 3차원을 표현할수 있는데 10개의 변수를 가지고 나타내기 때문에 총 7차원이 null space가 되게 됩니다. 즉 solution이 무한하게 됩니다.

이때는**Particular solution + Null space = Complete solution**다음과 같은 수식으로 표현이 가능합니다. 여기서 Particular solution의 경우 해를 갖는 3차원 벡터들을 의미하고, Null space는 어떠한 값이 들어와도 상관이 없는 Null space가 됩니다. 즉 모든 해를 particular solution과 null space의 합으로 나타낼 수 있다고 합니다. 

## Full Rank인 경우 ( 해= 1개 존재 )

Full Rank인 경우에는 invertable하기 때문에 간단하게 아래 수식을 통해서 1개의 해가 존재함을 알수 있습니다.

$$
AA^{-1}x = A^{-1}b
$$

즉 A의 역행렬을 구하게 되면 자연스럽게 x 값을 얻을 수 있게 됩니다.

## Rank deficient일 경우 ( 해 = 0개 혹은 무한개 )

Rank deficient인 경우에는 full row/column rank가 아닙니다. 그래서 예를 들면 A = (2,3) 행렬이고 rank = 1인 경우에 대해 예를 들어보면, rank = 1이기 때문에 총 1차원을 span할 수 있습니다.근데 2차원에서 1차원 span하기에 만일 span할 수 있는 곳에 값이 있다면 이 값들은 표현할 수 없습니다. 

반대로 만일 span 가능한 1차원 위에 값이 존재하는 경우 이를 표현할 수 있고 추가적으로 앞에서 살펴봤던 complete solution 공식에 의해서 column vector의 수 = 3, rank = 1 즉 null space는 2차원을 갖게 되고,결국 particular solution 1개와 2차원을 span하는 null space의 조합을 고려해 보면 무한개의 정답이 존재할 수 있게 됩니다.
