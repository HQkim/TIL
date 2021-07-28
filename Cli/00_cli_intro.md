# 00_Cli_intro

### **Command 꿀팁**

- 과거 명령어 불러오기(위, 아래 방향키)

- 자동 완성(tab)

- `ctrl + a` 커서가 명령어 맨 앞으로 이동

- `ctrl + e` 커서가 명령어 맨 뒤로 이동

- `ctrl + w` 커서 앞에 단어 지워줌

- ">"에 갇혔을 때는 `컨트롤 + C`를 누르세요.

  

## 경로

- 파일이나 폴더의 고유한 위치를 나타내는 문자열 (주소)

- 운영체제에 따라서 다르게 표현된다.

  windows - `C:\\Users\\Document`

  macOS - `/Users/Document`

- 정확한 경로에서 명령어를 실행해야 한다.

------

### **루트 디렉토리**

- 모든 파일/폴더를 담고 있는 폴더
- windows의 경우 보통 C 드라이브를 의미함

### **상대 경로**

- 현재 워킹 디렉토리를 기준으로 계산된 경로
- 현재 워킹 디렉토리가 `C:\\Users\\User\\바탕 화면` 라면 `C:\\Users\\USER\\바탕 화면\\code`의 상대 경로는 `code` 가 된다.
- 간결해서 좋지만 만약 현재 워킹 디렉토리가 변한다면 상대 경로는 변경된다. (다시 계산해야함)
- 현재 워킹 디렉토리가`C:\\Users\\` 로 변한다면, `C:\\Users\\USER\\바탕 화면\\code` 상대경로는 `Users\\code` 가 된다.
- `..\\` 는 부모 데렉토리를 의미한다.

### 절대 경로

- 어느 위치에 있던지 특정절대경로를 이용하면 해당경로로 이동할 수 있다.

### **`~` 틸드(Tilde)**

- 현재 사용자의 홈 디렉토리를 의미함.

- 현재 사용자란 컴퓨터를 킬 때 로그인 하는 계정

  

## Command

### **cd**

- Change Directory
- 현재 워킹 디렉토리를 변경할 때 사용한다.
- `cd ..` 하면 부모 디렉토리로 이동 할 수 있다.
- `C:\\Users\\User\\바탕 화면` -> `C:\\Users\\User`

### **date**

```
Wed Jun 23 15:39:15     2021
```

- 지금 날짜가 나온다.
- 운영 체제마다 시간을 기록하는 방법이 다르기 때문에 실제와 약간 다를 수 있음

### **ls**

- 현재 워킹디렉토리의 폴더/파일 확인하기
- `ls -al` 을 활용하면 숨김 폴더와 자세한 정보를 알 수 있다.

### **touch**

- `touch a.txt` 형식으로 파일을 만들 수 있다.

### **mkdir**

- `mkdir 디렉토리이름` 형식으로 폴더를 만들 수 있다.
- 만약 폴더 이름(happy hacking)에 공백이 있다면? `mkdir happy hacking` 이라고 명령어를 사용하면 `happy` 와 `hacking` 2개의 폴더가 생긴다. 이를 방지하기 위해서는 따옴표를 사용해서 폴더 이름을 묶어줘야 한다. `mkdir 'happy hacking'`

### pwd

- 현재 작업중인 폴더(디렉토리)

### rm, cp, mv

- 파일 삭제
- `rm -r` 폴더 삭제

- cp, mv

  - 복사 (복사, 붙여넣기)

    ```bash
    $ cp a.txt b.txt
    $ cp a.txt aa.txt
    ```

  - 이동 (잘라내기, 붙여넣기)

    ```bash
    $ mv b.txt b/b.txt
    ```

- 이름 바꾸기

  ```bash
  $ mv aa.txt c.txt
  ```



### 여담

- 개념을 학습할 때는 구조를 세우자.
- 구조를 키워드 중심으로 세운 후에 자세한 내용을 채워 나가는 식으로 하면 개념이 오래 간다.