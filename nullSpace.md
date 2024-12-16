Null space의 정의는 아래 수식을 만족하는 벡터 $x$ 를 의미합니다.

$$
Ax = 0 
$$

조금더 자세히 설명하면

$$
v_1x_1 + v_2x_2 + ... + v_px_p = 0
$$

를 만족하는 $x_1, x_2, ...., x_p$의 집합을 null space라고 합니다.

<aside>
📢

Null space : 행렬 A가 0으로 변환시키는 모든 벡터x의 집합

Null space는 행렬 A의 space가 아니라 x의 집합입니다.

</aside>

만약 아래와 같은 행렬이 존재하는 경우

$$
A = {1 0 1\brack 011}
$$

이를 아래와 같이 표현할수 있습니다.

$$
Ax = x_1{1\brack0} + x_2{0\brack1} + x_3{1\brack 1} = 0
$$

이를 만족시키는 x 벡터들의 집합이 null space가 됩니다.

해당 경우에 대해서는 간단하게 연립방정식을 통해서 null space를 구할수가 있습니다. 해당 식의 null space는  

$$
\alpha \begin{bmatrix} 1 \\ 1 \\ -1 \end{bmatrix}
$$

즉 null sapce가 1차원을 span하게 됩니다. 이를 통해서 알수 있는 사실은 아래와 같습니다.

<aside>
📢

```bash
행렬 A의 column vector의 수 = Rank(A) + null space dimension
```

</aside>

다시 자세히 말하자면 행렬 A는 선형변화시에  $\alpha \begin{bmatrix} 1 \\ 1 \\ -1 \end{bmatrix}$ 위에 존재하는 모든 값들을 0으로 매핑시키는 선형 변환 입니다.

그리고 이를 만족하는 null space의 경우 모든 값을 0으로 만들어야되기 때문에 row space와 수직인 관계를 갖게 됩니다.

만일 A라는 행렬이 3 * 3 크기를 갖고, rank(A) = 2라는 가정한다면 null space는 1차원이 되게 됩니다.

그리고 이를 수식으로 살펴보면 아래와 같습니다.

$$
A =  \begin{bmatrix} a_1 a_2 a_3 \\ a_4 a_5 a_6 \\ a_7 a_8 a_9 \end{bmatrix} x = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}
$$

다음과 같이 존재하는 경우 하나의 예만 살펴보게 되면 $a_1x_1 + a_2x_2 + a_3x_3 = 0$ 을 만족해야 합니다. 이때 모든 x와 모든 row vector들의 값이 0이 나온다  = 서로 수직이다. 라는것이 증명되게 됩니다.

<img width="240" alt="image" src="https://github.com/user-attachments/assets/5c6bdbdf-4d0a-4457-a84a-5b1e98931157" />
<br>
다음과 같이 column vector의 수가 3개인 경우 rank인 2차원을 row vector들이 span하고, 이와 수직인 1차원 직선들은 null space가 됩니다.

그리고 3차원이 아니라 더 고차원에서의 경우에는 아래와 같이 표현한다고 합니다.

<img width="243" alt="image" src="https://github.com/user-attachments/assets/c1a2c909-42ea-48fa-8131-a48197eda863" />
<br>

여기서 left null space의 경우에는 아래 수식을 만족하는 null space를 의미하며, 그 떄는 null space가 column space와 수직한 관계를 갖게 됩니다.

$$
x^TA = 0
$$

중요한 개념이라 다시한번 정리해보면 아래와 같습니다.

<aside>
📢

행렬 A의 column vector의 수 = rank(A) + null space의 dimension

그리고 A행렬의 row vector와 null space는 항상 직교 입니다.

null space의 개념을 살펴보면 행렬A에 의해 벡터x들을 선형변환했을 때 0이 되는 모든 x들의 집합입니다.

</aside>
