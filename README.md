# Fare4U: Flight Fare Prediction Web Application
- 프로젝트 기간: 2021.10.06 - 2021.10.12
---
## 프로젝트 목표
- 데이터 파이프라인 설계
- 항공료 예측 모델 만들기
- 웹어플리케이션 개발 및 배포하기
- 구글 데이터스튜디오를 통해 대시보드 만들기
---

## 데이터셋 설명
- Kaggle 데이터 활용<br>
> - xlsx data
> - 10,683의 행과 11개의 열로 구성<br>

해당 프로젝트는 데이터파이프라인 설계 및 웹앱 배포가 목표이기 때문에 Kaggle에서 항공료가 포함된 인도의 비행 여정을 설명하는 다양한 속성을 포함한 데이터를 가져와 진행하였습니다.

---
## 데이터 파이프라인 소개
<img width="636" alt="pg2" src="https://user-images.githubusercontent.com/87054081/137450136-2f7e48a0-f963-496e-af4b-9d7a6120b430.PNG"><br>
- Kaggle에서 가져온 데이터를 MongoDB에 저장<br>
MongoDB Atlas는 클라우드 데이터베이스 서비스로 인터넷을 이용해 어디서든 접속 가능한 서비스입니다.

- 데이터 전처리 및 분석 진행<br>
 Random Forest Regression으로 모델을 돌렸고 1에 가까울 수록 높은 성능을 나타내는 지표인 R square score가 0.85가 나왔습니다. 이 과정에 있어서 성능을 더 높일 수 있게 모델링을 위해 설정해주는 값인 하이퍼파라미터를 조정했습니다. 항공료 예측 서비스이기 때문에 항공료에 영향을 미치는 중요한 특성들을 추출하고자 각 특성들 간의 중요도 측정을 했습니다. 

- 웹 프레임워크인 Flask를 통해 항공료 예측 서비스인 'Fare4U'라는 웹앱을 개발<br>
 웹 프레임워크는 쉽게 말해 뭔가를 만들어낼 수 있는 도구 모음을 제공한다고 보시면 됩니다.

- 개발한 웹앱을 Heroku를 통해 웹에 배포
- 수집한 데이터를 구글 데이터스튜디오를 통해 시각화하여 대시보드를 만듦<br>
 이 또한 배포하는 과정을 마무리로 해당 서비스가 구현되었습니다.

---
## 결과
> Bootstrap과 HTML, CSS, JavaScript을 활용하여 웹사이트 구조를 만들고 디자인함

![india4u_overall](https://user-images.githubusercontent.com/87054081/137173265-e5762a67-1807-4846-9929-6653a2c8fc84.gif)
![fare4u_app](https://user-images.githubusercontent.com/87054081/137173788-2bc9c0e3-59ea-4f32-b10f-3547c4b2a442.gif)
