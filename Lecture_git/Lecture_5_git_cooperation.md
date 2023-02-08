# 협엄하기

## 공동 작업자 추가하기

gitHub의 공개 저장소는 주소만 알면 누그든지 소스를 볼 수 있다. 또한 gitHub 회원이면 누구나 오픈 소스에 접근하여 파일을 내려받을 수 있다. 하지만 주소를 안다고 해도 내가 작성한 파일을 접근한 공개 저장소에 add-commit-push을 할 수 있는 것은 아니다.
팀장, 팀원 1, 팀원 2가 공동작업을 한다고 가정을 하자.
그럼 보통 팀장이 github 저장소를 만든다. manim-mathani를 저장소를 만들었다고 가정하자. 저장소로 접속을 하고 settings 버튼을 누르자.
![저장소1](./img/Lecture5_img1.png "저장소1")
그러면 왼쪽 메뉴가 보이고 collaborators를 선택하자. 그리고 아래 중간에 보면 녹색의 'Add people' 버튼이 있다. 이 버튼을 누르자.
![저장소2](./img/Lecture5_img2.png "저장소2")
초대할 사람을 username 또는 email으로 초대할 수 있다. 그래서 아래 그림의 입력 폼에 username 또는 email을 적고 'Sellect a collaborator above' 버튼을 누르자. 그러면 초대가 된다.
![저장소3](./img/Lecture5_img3.png "저장소3")

## 원격 저장소에 첫 commit-push 하기

먼저 팀장이 원격 저상소를 연결하고 test.md 파일을 만들어 원격 저장소의 main 브랜치에 push를 하자.

```git
git remote add origin [원격 저장소 URL]
echo 'Manim-mathani project' >> test.md
git add test.md
git commit -m "collaboration test"
git push -m origin main
```

그러면원격 저장소에 test.md 파일이 보일 것이다.

## 공동 작업자(팀원1, 팀원2) 로컬 pc에 원격 저장소를 clone하기

공동 작업자인 팀원 1, 팀원 2는 팀장이 만들어 놓은 원격 저장소를 clone하여야 한다.

```git
git clone [원격 저장소 주소]
```

## 첫 번째 commit이 아니라면 pull을 하자

github로 협업을 할 때는 여러 사람이 함께 문서를 수정하고 commit-push를 하기 때문에 반드시 pull로 원격 저상소의 최신 commit를 당겨운 다음 자신의 commit를 push하여야 한다. 아직 브랜치를 만들지 않고 main에서만 변경하는 것으로 하자.

팀원 1, 팀원 2 모두 clone을 하였다고 하자.

팀장이 다른 문 test00.md를 만들고 commit 하고 push를 하였다고 하자.

그리고 팀원 1인 test01.md를 작성하여 'uploade test01.md'라는 commit를 하고 push를 한다고 하자.

```git
git add test01.md
git comm -m "uploade test01.md"
git push -m origin main
```

그러면 ![rejected]로 시작하는 오류 메세지가 출력된다. 이것은 팀원 1의 로컬 pc에 새로운 commit 내역이 존재 하지 않기 때문에 발생하는 오류이다. 따라서 commit을 하기 전에 pull로 먼저 당겨와야 한다. pull명령을 사용하여 당겨오는 경우 자동으로 vim이 실행되면서 commit message가 표시된다. 원하는 내용으로 추가해도 되고 기본 메세지를 사용해도 된다.

```git
# git pull [원격저장소 명] [브랜치 명]
git pull origin main
```

pull로 당겨왔기 때문에 원격 저상소의 최선 commit을 당겨왔으므로 이제 commit을 할 수 있다. 이미 add 된 상태이므로 commit부터 하면 된다.

```git
git comm -m "uploade test01.md"
git push -m origin main
```

## branch로 push하기
