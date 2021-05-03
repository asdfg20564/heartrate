# server_mts      

#### 실시간 bpm 측정 프로그램 output인 data_log.txt에서 결과를 불러와 서버에 출력한다.<br>
#### Request 받을 때마다 Database(MySQL)에 현 시간의 output을 저장한 후 Response한다. <br>

##### Response로 보내지는 정보 (JSON 형식)
- bpm : int. bpm <br>
- resp : int. 분 당 호흡 수<br>
- time : DateTime. output에서 bpm이 계산된 시간.<br>

##### URL 정보
/data/log : 지금까지 저장된 bpm, resp, time을 모두 Response. 해당 페이지를 Request할 때마다 실시간 측정 프로그램의 결과를 가져온 후 현재부터 과거 데이터 전부를 가져온다.<br>
(데이터가 많아지는 경우 100개 이상일 때 자르는 식으로 개선할 수 있을 것 같다.)<br>
/data/cur : 현재 output에서 도출된 bpm, resp, time을 보여준다. 실시간 측정 프로그램에서 결과를 가져와 저장한 후 그 결과 하나만 보여준다.<br>




