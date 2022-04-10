# 🎨 ART-ROUND

## 프로젝트 소개
- 전시회, 박물관들을 지도 형식으로 띄워 사용자 주변의 가까운 전시회들을 한눈에 보여줍니다. 

## 기술 스택
- React
- Django Rest Framework


##  기능 / 소개
- 카카오 소셜 로그인으로 회원가입, 로그인을 진행합니다.
- 사용자 주변의 전시회, 박물관이 지도에 나타납니다. (GPS 동의 필요)
- 전시회 혹은 박물관을 클릭하여 즐겨찾기에 등록, 공유 등이 가능합니다.
- 모바일 사이즈만 제작하였습니다.
- 이미지는 unsplash에서 받았습니다.


## 레파지토리
- Client: https://github.com/ArtRound/ArtRound-front
- Server: https://github.com/ArtRound/ArtRound-server


## 미리보기
### [회원가입/로그인]
- 카카오 계정으로만 로그인이 가능합니다. 2단계 인증까지 완료하면 회원가입됩니다.

![image](https://user-images.githubusercontent.com/66022264/162613275-c6c67a3d-66bf-47cc-8647-d32ee8d8580b.png)
![image](https://user-images.githubusercontent.com/66022264/162613828-f6acd194-2ec2-4275-8deb-4e540e8c49f6.png)


- 처음 가입 시(DB에 회원 정보가 없다면) 추가 정보를 입력받습니다.
- 정보 필드로는 이름(닉네임), 성별, 나이가 있습니다.

![image](https://user-images.githubusercontent.com/66022264/162613836-8b3913f9-aa66-4abf-a34d-b99401377644.png)

- 마이페이지 탭을 보면 입력한 정보가 보입니다.

![image](https://user-images.githubusercontent.com/66022264/162613623-974b27ae-7769-4122-ac36-b11900466aeb.png)

### [메인-지도]
- 공공데이터에서 가져온 데이터 목록을 지도에 보여줍니다.
- 데이터 양이 많기 때문에 로딩 중에는 로딩 스피너가 뜨고, 지도 화면이 보입니다.

![image](https://user-images.githubusercontent.com/66022264/162613844-7ff73304-5ce3-4e53-8c90-04039813c74a.png)
![image](https://user-images.githubusercontent.com/66022264/162613790-555dcb50-a89e-4d94-9eca-b79c1e333f86.png)

### [메인-상세페이지]
- 즐겨찾기 토글 시, 즐겨찾기 목록에서 추가/삭제되며, 방문도 마찬가지입니다.

![image](https://user-images.githubusercontent.com/66022264/162613779-5a0959d8-081a-4fd9-8ddf-8b3b7b5ff119.png)
![image](https://user-images.githubusercontent.com/66022264/162613472-ae1d1cca-ead6-4698-acc6-d70999400a61.png)

### [즐겨찾기, 방문]
-즐겨찾기, 방문한 전시회 페이지에는 전시회 세부 정보가 나오며, 이름 클릭 시 후기 페이지로 넘어갑니다.

![image](https://user-images.githubusercontent.com/66022264/162613373-5ac3f3c8-d0b5-4464-a1fe-56b7f08c1dca.png)
![image](https://user-images.githubusercontent.com/66022264/162613516-dd6c0674-761e-44fb-84ea-b60b57570cdb.png)

### [후기 페이지]
- 후기 페이지에서는 정렬 기능, 후기 리스트, 후기 작성 버튼이 있으며 작성 페이지에서는 하트 개수, 후기 작성, 사진 추가 기능이 있습니다.

![image](https://user-images.githubusercontent.com/66022264/162613751-ec430fe1-a631-42fa-9085-dac321e43190.png)
![image](https://user-images.githubusercontent.com/66022264/162613754-1ac6a33f-2c26-4771-a77e-6bd31a54962d.png)


### [고객센터]
- 서비스 소개, 공지사항, 문의 게시판, 이용약관 등을 확인할 수 있는 고객센터 페이지입니다.

![image](https://user-images.githubusercontent.com/66022264/162613579-4063c38c-5ce4-4675-a267-946d789567dc.png)
![image](https://user-images.githubusercontent.com/66022264/162613713-d3ae0846-b196-4395-bb06-e53ea6cff294.png)

---
## 아트라운드 소개 및 회고
https://breathtaking-life.tistory.com/161?category=834790
