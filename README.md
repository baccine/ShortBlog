유튜브 쇼츠 블로그 프로젝트
프로젝트 기간: 2024.08.26 ~ 2024.09.02
프로젝트 인원: 1명

목차
프로젝트 개요
프로젝트 소개
주요 기능
기술 스택
개발 환경
프로젝트 구조
폴더 트리
ERD
구현 내용
사용 화면
주요 기능 설명
트러블 슈팅
프로젝트에서 배운 점
프로젝트 개요
프로젝트 소개
이 프로젝트는 Django를 활용하여 유튜브 쇼츠 블로그를 구현하는 것을 목표로 합니다. 블로그는 쇼츠 비디오와 관련된 다양한 게시글을 다루며, 사용자 친화적인 UI와 강력한 백엔드 시스템을 갖추고 있습니다.

주요 기능
게시글 관리 기능

게시글 작성, 수정, 삭제 기능
이미지 업로드 기능
카테고리 및 태그 지정
게시글 조회수 증가 기능
사용자 인증 및 관리

회원가입, 로그인, 로그아웃 기능
프로필 수정 및 비밀번호 변경
프로필 이미지 업로드
댓글 및 소셜 기능

댓글 및 대댓글 작성, 수정, 삭제
게시글 좋아요 및 북마크 기능
기타 기능

반응형 웹 디자인
검색 및 필터링 기능
페이지네이션
기술 스택
프레임워크: Django
언어: Python, HTML, CSS, JavaScript
데이터베이스: SQLite
기타 라이브러리: Pillow (이미지 처리)
개발 환경
Python: 3.11
Django: 5.0.7
Pillow: 10.4.0
프로젝트 구조
폴더 트리
## WBS
구글 링크 : https://docs.google.com/spreadsheets/d/1ErtJS_64mhxFPxHf5niv7E0dq3oHF8GtwhF3tCdfJ1g/edit?gid=0#gid=0


graph TD
    A[프로젝트 기획 (8/26)] --> B[요구사항 분석 (8/26)]
    A --> C[WBS 작성 (8/26)]

    C --> D[디자인 및 설계 (8/27)]
    D --> E[UI/UX 디자인 (8/27)]
    D --> F[DB 설계 (ERD 작성) (8/27)]
    D --> G[URL 구조 설계 (8/27)]

    G --> H[개발 환경 설정 (8/28)]
    H --> I[가상환경 설정 (8/28)]
    H --> J[Django 프로젝트 생성 (8/28)]
    H --> K[Static/Media 설정 (8/28)]

    K --> L[기능 개발 (8/29~8/31)]
    L --> M[회원가입/로그인 기능 개발 (8/29)]
    L --> N[메인 페이지 개발 (8/29)]
    L --> O[게시글 CRUD 기능 개발 (8/30)]
    L --> P[이미지 업로드 기능 추가 (8/30)]
    L --> Q[좋아요/싫어요 기능 개발 (8/30)]
    L --> R[댓글 기능 개발 (8/31)]

    R --> S[테스트 및 디버깅 (8/31)]
    S --> T[기능 테스트 및 디버깅 (8/31)]
    S --> U[디자인/레이아웃 수정 (8/31)]

    U --> V[배포 및 발표 준비 (9/1)]
    V --> W[배포 준비 (9/1)]
    V --> X[README 작성 및 문서화 (9/1)]
    V --> Y[최종 점검 및 발표 준비 (9/1)]

erDiagram
    USER {
        int id PK
        string username
        string password
        string email
        string first_name
        string last_name
        bool is_staff
        bool is_superuser
        datetime date_joined
    }
    
    POST {
        int id PK
        string title
        text content
        datetime created_at
        datetime updated_at
        int views
        int author_id FK
        int category_id FK
        string image
    }

    CATEGORY {
        int id PK
        string name
        string slug
    }

    TAG {
        int id PK
        string name
    }

    COMMENT {
        int id PK
        text content
        datetime created_at
        int post_id FK
        int author_id FK
    }

    POST_LIKES {
        int post_id PK FK
        int user_id PK FK
    }

    POST_DISLIKES {
        int post_id PK FK
        int user_id PK FK
    }

    POST_TAGS {
        int post_id PK FK
        int tag_id PK FK
    }

    USER ||--o{ POST : "writes"
    USER ||--o{ COMMENT : "writes"
    USER ||--o{ POST_LIKES : "likes"
    USER ||--o{ POST_DISLIKES : "dislikes"
    POST ||--o{ COMMENT : "has"
    POST ||--o{ POST_TAGS : "has"
    POST ||--o{ POST_LIKES : "has"
    POST ||--o{ POST_DISLIKES : "has"
    CATEGORY ||--o{ POST : "categorizes"
    TAG ||--o{ POST_TAGS : "tags"


## URL 구조

```mermaid
graph TD
    A[메인 페이지 '/'] --> B[회원가입 '/register/']
    A --> C[로그인 '/login/']
    A --> D[로그아웃 '/logout/']
    A --> E[게시글 목록 '/posts/']
    E --> F[게시글 작성 '/post/new/']
    E --> G[게시글 상세보기 '/post/<int:pk>/']
    G --> H[게시글 수정 '/post/<int:pk>/edit/']
    G --> I[게시글 삭제 '/post/<int:pk>/delete/']
    G --> J[게시글 좋아요 '/post/<int:pk>/like/']
    G --> K[게시글 싫어요 '/post/<int:pk>/dislike/']
    G --> L[댓글 작성 '/post/<int:pk>/comment/']
    L --> M[댓글 삭제 '/comment/<int:pk>/delete/']
    A --> N[관리자 페이지 '/admin/']

    classDef default fill:#f9f,stroke:#333,stroke-width:2px;
    classDef admin fill:#fcf,stroke:#f66,stroke-width:2px;
    class N admin;

