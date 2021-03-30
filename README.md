# heartrate      

#### 실시간 bpm 측정 프로그램 output인 bpm_log.txt에서 결과를 불러와 서버에 출력한다.<br>Request 받을 때마다 Database(MySQL)에 현 시간의 output을 저장한 후 Response한다. <br>

##### Response로 보내지는 정보 (JSON 형식)
- bpm : int. bpm 정보<br>
- time : DateTime. output에서 bpm이 계산된 시간.<br>
- (예정)resp : int 분 당 호흡 수<br>




