# 효율적인 알고리즘 설계와 순서도 의사코드 작성

> 프로젝트 개발에도 설명서 같은 설계서가 필요

> 코딩을 하기 앞서 알고리즘 설계, Flowchart, Psuedo-code 작성을 통해 효율적이고 최적화된 개발을 하여 누가 어떤 언어로 작성하여도 비슷한 품질로 결과가 나올 수 있게끔 한다

<br/>

<br/>

## 알고리즘 디자인 설계

- 무엇을 어떻게 개발할지에 대한 답을 하는 작업
- 이 작업이 잘 되어야지만 나중에 필요하지 않은 기능을 개발하는 불상사 예방

<br/>

<br/>

## Flowchart

- 일의 진행 순서도 혹은 프로세스를 보여주는 다이어그램
- 복잡한 프로세스를 명확하고 이해하기 쉬운 다이어그램으로 문서화하기 위해 사용
- 순서도에는 각 도형의 요소들이 의미하는 바가 있음(도형과 화살표 등)

<br/>

### Flowchart 요소

([아래 그림 출처](https://www.smartdraw.com/flowchart/flowchart-symbols.htm))

![image-20211227223859736](README.assets/image-20211227223859736.png)

<br/>

<br/>

## Psuedo-code(의사코드)

> [참고자료1](https://medium.com/djangogirlsseoul-codecamp/%EC%9D%98%EC%82%AC%EC%BD%94%EB%93%9C-pseudo-code-%EB%9E%80-d892a3479b1d), [참고자료2](https://42kchoi.tistory.com/114)

- 컴퓨터 프로그램이나 알고리즘이 수행해야할 내용을 일상언어로 간략히 서술해 놓은 것
- 개발자가 아닌 지식이 전혀 없는 사람이 봐도 이해할 수 있도록 가독성 좋게 작성하는 것

<br/>

### 사용 이유

- 코딩을 하기 전 사고를 좀더 명확히 정립하게 만들어주어 프로그램 설계하는데 도움이 됨
- 나중에 디버깅을 하고 코드를 수정하는데 걸리는 시간을 단축할 수 있음

<br/>

### 의사코드 작성의 표준(Standard)

1. 한줄에 하나의 명령만 적는다
2. 영어로 의사코드 작성시 명령문의 첫 단어를 대문자로 작성한다
3. 실제 프로그램 코드처럼 작성하지 말고 하고 싶은 이야기를 기록한다.
   - "if a % 2 == 1 then"과 같이 작성하지 않고 "숫자가 홀수라면(if an odd then)"과 같이 작성한다.
4. 프로세스에 필요한 모든 것을 빠짐없이 기록한다. 
   - "g=54/r 이라고 하자" 대신에 "필요한 양은 54 나누기 거리로 정의하자"와 같이 적는다.
5. 블록으로 코드의 구조를 정리힌디
   1. 중괄호 {...}
   2. 빈칸 사용: 블록 안에 블록이 들어간다면, 들여 쓰기는 더 깊어져야 한다.

