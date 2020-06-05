# Git

> Git은 분산형버전관리시스템 (DVCS) 이다
>
> 소스코드 형상 관리 도구로, 코드의 이력을 관리 할 수 있다.

# Git 로컬 저장소 활용하기

> git은 reporitory (저장소)로 각각 프로젝트를 관리한다.

##  0. 기본 설정

Git에서 이력을 남기기 위해 작성자(author) 정보를 추가한다. 매 컴퓨터에서 최초로 한 번만 설정하면 된다. 

````bash
$ git config --global user.name (26future)
$ git config --global user.email(26future@hanmail.net)
​```
````

* 일반적으로 '(유저네임)', '(이메일)' 에는 github정보를 넣는다.

## 1. 저장소 생성

```bash
$ git init
Initialized empty Git repository in C:/Users/student/Desktop/.git/ (master) $


```

## 2. add

> 커밋 대상 파일을 staging.area 로 이동시킨다. 
>
> 즉, 이력을 남길 파일을 담아 놓는 것이다. 

. 은 현재 디렉토리(폴더)를 뜻한다.

```bash 
$ git add .  # 현재 디렉토리 

$ git add git.md  #특정 파일만 stage

$ git add images/  #특정 폴더만 stage

```


항상 git status 명령어를 통해 상태를 확인한다. 
```bash
$ git commit -m 'Git 기초'
[master (root-commit) 6c07b40] Git 기초
 2 files changed, 88 insertions(+)
 create mode 100644 "image/\353\247\210\355\201\254\353\213\244\354\232\264 \355\231\234\354\232\251\353\262\225.jpg"
 create mode 100644 "\353\247\210\355\201\254\353\213\244\354\232\264 \355\231\234\354\232\251\353\262\225.md"

```

## Git 원격 저장소 활용하기

### 0. 기본 설정

> 원격 저장소를 생성한다. (예 - github)

### 1. 원격 저장소 등록

origin 이라는 이름으로 해당 url을 원격 저장소르 등록

최초에 한 번만 하면 된다. 

```bash
$ git remote add origin https://github.com/26future/TIL.git

$ git remote -v # 원격 저장소 등록
d

```

