정사각 행렬 A에 대해 아래 수식을 만족하는 v와 $\lambda$ 를 각각 eigen vector와 eigen value라고 합니다.

$$ Ax = \lambda x $$

<img width="190" alt="image" src="https://github.com/user-attachments/assets/9f2540ad-1977-4f34-8f3e-d9d97342af8f" />
<br>

벡터 x가 행렬 A를 통해서 선형변환이 되는데, 이때 x의 방향은 변하지 않고 크기만 변하는 벡터들을 eigen vector ( 고유벡터 )라고 합니다. 그리고 크기의 변화량을 의미하는 $\lambda$를 eigen value ( 고유값) 이라고 합니다.

추가적으로 선형변환의 관점에서 역행렬 존재 경우를 살펴보면 특정 값 a,b라는 값을 A를 통해서 선형변환 시키는 경우 c,d라는 서로 다른 값으로 매핑이 되는 경우 우리는 A행렬이 invertable하다고 합니다. 왜냐하면 a → c → a 혹은 b →d → b 처럼 원상태로 되돌릴수 있습니다. 하지만 만일 a와 b가 모두 c라는 동일한 값으로 매핑 되는경우 c라는 값을 되돌릴때 a,b중 어디로 가야될지 모릅니다. 이에 행렬 A는 invertable하지 않게 됩니다. 이게 의미하는게 결국 N차원인 경우 N 차원 보다 작은 차원으로 매핑 되기 떄문에 N차원에 어떤 값을 가져야 하는지 모른다는 것을 의미하며 이는 결룩  저차원으로 매핑됨 → det(A) = 0 을 의미하게 됩니다. 이에 자연스럽게 Invertable하지 않는다 = det(A)가 0이다 = rank deficient 하다 로 정리할수 있습니다.

아무튼 우리는 행렬 A의 eigen value와 eigen vector에 대해 알아보도록 하겠습니다.

$$
Av = \lambda v
$$

$$
(A - \lambda ) v = 0
$$

$$
(A -I\lambda)v = 0
$$

이때 중요한 가정이 필요합니다. 단순히 v = 0 인 경우를 제외합니다. 그리고 추가적으로 만일 $A - I\lambda$ 행렬이 invertable하다면 양변에 $(A - I\lambda)^{-1}$을 곱하게 되면 자연스럽게 v = 0이 되기 떄문에 $A - I\lambda$ 행렬은 invertable 하면 안됩니다 ( 역행렬이존재하면 안된다 ). 그렇기 때문에 자연스럽게 $det(A - I\lambda) = 0$ 을 만족하는 $\lambda$를 찾은 후 이를 대입하여 v를 찾게 됩니다.

그리고 dot product로 행렬을 살펴보면 만일 $\lambda$를 찾았다고 해서 이를 대입한 $A - I\lambda$ 행렬과 v 벡터의 값이 0이 되어야 합니다. 즉 $A - I\lambda$ 행렬의 null space가 결국 eigen vector가 되게 됩니다. 그 말은 즉슨 실수계에서는 eigen vector가 0개 혹은 $\infin$개 존재함을 의미합니다.

그리고 $\lambda$가 의미하는 것은 만일 eigen vector가 선형변환 될 경우 $\lambda$만큼 크기가 변한다는 겻을 의미합니다.
예를들어 $\lambda = 3$  인 경우 벡터가 행렬 A에 의해 선형변환 될경우 벡터의 크기가 3배 증가한다는 것을 의미합니다.
