Determinant의 정의는 정사각행렬을 Scalar로 만드는 특정 함수이고, 이 scalar 값에는 해당 행렬을 표현할수 있는 다양한 정보가 담겨져 있습니다.

3차원에서의 determinant를 구하는 방법을 간단하게 알아보면 아래와 같이 표현할수 있습니다.

$$
A = { \begin{bmatrix} a b c \\ d e f \\g h i \end{bmatrix} }
$$

위와 같은 행렬이 존재하는 경우 A의 determinant는 아래와 같습니다.

$$
det(A) = a(ei-fg) + b(di -fg) +c(db -eg)
$$

< determinant 관련 수식 >

1. 행렬 A가 대각행렬이거나 삼각행렬인 경우 det(A)의 값은 대각요소들의 곱으로 결정된다. 그래서 만일 대각행렬 중 하나라도 0의 값을 갖게 되면 역행렬이 존재하지 않게 된다. 
2. $det(A) = det(A^{T})$ 이다.
3.  $det(A) = { 1 \over det(A^{-1}) }$  이를 만족한다.
4. $det(AB) = det(A) det(B)$ 를 만족한다
5. $det(A) = \lambda_1\lambda_2\lambda_3...\lambda_n$ 을 만족한다 ( $\lambda_n$ 은 eigen value를 의미한다 ) 즉 하나의 고유값이라도 0이라면 역행렬이 존재하지 않는다.
