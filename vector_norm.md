Norm : 벡터의 크기를 나타내는 방법입니다. 즉 0 포함 양수 스칼라를 갖게됩니다.

### 2-Norm

$$
\|a\|_2 = \sqrt{a^Ta}
$$

### 1-Norm

$$
\|a\|_1 = \sum|a|
$$

즉 N-Norm의 경우 각 element들을 P 제곱을 하고 이를 1/P로 나누는 것이 바로 $L_p-norm$이 됩니다.

Norm에 대한 일반식을 살펴보면 아래와 같이 정리할 수 있습니다.

<img width="667" alt="image" src="https://github.com/user-attachments/assets/0542c940-f66d-4a23-814e-08e94b904e45" />


그리고 각 Norm을 시각화 해보면 아래와 같이 시각화할 수 있습니다.

<img width="674" alt="image" src="https://github.com/user-attachments/assets/b89924ce-74e0-4532-a728-f4e70cc8417a" />

위의 내용을 통해서 Norm의 p 값이 커질수록 norm = 1 을 표현하는 영역이 넓이짐을 확인할수 있고 이는 결국 벡터들의 자유성을 의미하게 됩니다. 최대 벡터만 고려하기 떄문에 다른 벡터들의 값이 뭘 갖는 상관없기에 벡터들이 보다 넓게 분포할 수 있습니다.

즉, Norm에서 P가 의미하는것이 더 큰 벡터의 기여도를 어떻게 구성할지 입니다.

L1 Norm의 경우 모든 차원이 동등하게 기여합니다.

L2 Norm의 경우 제곱을 하기에 더 큰 차원의 값이 더욱 강조되게 됩니다.

L INF의 경우 가장 큰 차원을 제외하고 나머지는 모두 무시가 되게 됩니다.

그래서 만일 [3,4]라는 벡터를 각 Norm으로 표현하게 되면 L1 Norm이 가장 큰 값을 갖게 되고 L무한대 Norm이 가장 작은 값을 갖게 됩니다.

```bash
L1 = 7
L2 = 5
LINF = 4

L1 > L2 > ..... > L INF
```

위와 같이 정리할 수 있습니다.
