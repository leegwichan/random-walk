# 랜덤 워크 기반 몬테카를로 시뮬레이션을 이용한 확산 모델 연구

## 사용 수식
### 확산 방정식 : 
$$\langle r^2(\Delta t) \rangle = 2 d D \Delta t$$

- $\langle r^2(\Delta t) \rangle$ : 시간 간격 $\Delta t$에서의 평균 제곱 변위 (m$^2$)  
- $d$ : 공간 차원 (1, 2, 또는 3)  
- $D$ : 확산 계수 ($m^2/s$)
- $\Delta t$ : 시간 간격 ($s$)

### 확산 계수
$$D = \frac{k_B T}{6 \pi \eta r}$$ 

- $D$ : 확산 계수 ($m^2/s$)
- $k_B$ : 볼츠만 상수 ($1.38 \times 10^{-23} J/K$)  
- $T$ : 절대 온도 (K)  
- $\eta$ : 유체의 점도 (Pa·s = kg/(m·s))  
- $r$ : 입자의 반지름 (m)

### Random Walk 평균 제곱 변위 (3차원)
$$\langle r^2(n) \rangle = n \cdot l^2$$
- $\langle r^2(n) \rangle$ : n 스텝 후의 평균 제곱 변위 ($m^2$)
- $n$ : 스텝 수
- $l$ : 각 스텝의 길이 (m)
- n=1 일 때, $l = \sqrt{6D\Delta t}$

### 침강 속도
$$v_{\text{terminal}} = \frac{(m - \rho_{\text{fluid}} V) g}{6 \pi \eta r}$$
- $v_{\text{terminal}}$ : 침강 속도 (m/s)
- $m$ : 입자의 질량 (kg)
- $\rho_{\text{fluid}}$ : 유체의 밀도 ($kg/m^3$)
- $V$ : 입자의 부피 ($m^3$)
- $g$ : 중력 가속도 (9.81 $m/s^2$)
- $\eta$ : 유체의 점도 (Pa·s = kg/(m·s))
- $r$ : 입자의 반지름 (m)


