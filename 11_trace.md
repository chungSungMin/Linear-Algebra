trace 정의: diagonal element들의 총합을 의미합니다. 그렇기 때문에 trace는 정사각 행렬에 대해서만 정의가 됩니다. $tr(A) = \sum^n_{i=1}a_{ii}$ 을 의미하게 됩니다. 결국 tr(A)의 결과는 하나의 스칼라 값이 나오게 됩니다.

정의 자체는 너무나 간단한데 너무나 유용해서 trace라는 개념이 널리 사용된다고 합니다.

1. $tr(A+B) = tr(A) + tr(B)$
2. $tr(AB) = tr(BA)$ ( s.t A =(n X m) 이라면 B = (m x n ) 이어야 한다
3. $tr(a^Tb) = tr(ba^T)$
4. $tr(ABCD) = tr(BCDA) = tr(CDAB) = tr(DABC)$ → cyclic property 라고 한다고 합니다.( 무조건 순서대로 가야된다. becase 행렬의 크기 떄문에 ) 
5. $tr(A) = \sum^n_{i=1}\lambda_i$         ( $\lambda_i$  는 eigen value 입니다. )
