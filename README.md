# Shorts Blog Project
장고를 활용한 유튜브 쇼츠 블로그 프로젝트

## 1.1 프로젝트 소개
이 프로젝트는 Django를 활용하여 유튜브 쇼츠 스타일의 블로그를 구축하는 것을 목표로 합니다. 사용자 친화적인 UI와 강력한 백엔드 시스템을 통해 쇼츠 관련 컨텐츠를 관리하고, 사용자 간의 상호작용을 지원합니다.

- 주요 목표
    - **쇼츠 블로그 설계 및 구현**: 쇼츠 영상과 관련된 게시글을 관리하고, 사용자 간의 상호작용을 촉진하는 기능 구현.
    - **데이터베이스 모델링 및 CRUD 기능 구현**: 효율적인 쇼츠 컨텐츠 관리 기능 구현.
    - **사용자 인증 및 권한 관리**: 안전하고 개인화된 사용자 경험 제공.
    - **프로젝트 문서화 및 설계**: 체계적인 프로젝트 관리 및 유지보수 지원.



## 1.2 주요 기능
- **게시글 관리 기능**
    - **게시글 작성, 수정, 삭제 기능**
        - **설명:** 사용자가 쇼츠 관련 글을 작성, 수정, 삭제할 수 있는 기능.
        - **주요 기능:**
            - 이미지 업로드 기능.
            - 카테고리 및 태그 지정.
            - 게시글 상태 관리 (초안/발행됨/보류 중).

    - **게시글 조회 및 상세보기 기능**
        - **설명:** 작성된 글을 목록으로 보거나 상세 내용을 확인하는 기능.
        - **주요 기능:**
            - 페이지네이션.
            - 검색 및 필터링.
            - 조회수 표시.
            - 좋아요 및 싫어요 기능.

    - **댓글 기능**
        - **설명:** 게시글에 대한 의견을 나눌 수 있는 기능.
        - **주요 기능:**
            - 댓글 작성, 수정, 삭제.
            - 대댓글 지원.

- **사용자 인증 및 프로필 관리 기능**
    - **회원가입 및 로그인/로그아웃 기능**
        - **설명:** 사용자 계정 생성 및 인증 관리 기능.
        - **주요 기능:**
            - 이메일을 통한 회원가입.
            - 로그인/로그아웃.

    - **프로필 수정 및 비밀번호 변경 기능**
        - **설명:** 사용자 정보 관리 및 보안 설정 기능.
        - **주요 기능:**
            - 프로필 이미지 업로드.
            - 개인정보 수정 (닉네임, 자기소개 등).
            - 비밀번호 변경.

- **추가 기능**
    - **검색 기능**
        - 키워드를 통한 게시글 검색.
        - 카테고리 및 태그 기반 필터링.

    - **반응형 디자인**
        - 최적화된 레이아웃 제공.



### ERD

```mermaid
erDiagram
    CustomUser ||--o{ Post : writes
    CustomUser ||--o{ Comment : writes
    CustomUser ||--o{ Like : makes
    Post ||--o{ Comment : has
    Post ||--o{ Like : receives
    Post ||--o{ Bookmark : receives
    Post }o--|| Category : belongs_to
    Post }o--o{ Tag : has

    CustomUser {
        int id PK
        string username
        string email
        string password
        string nickname
        image profile_image
        text bio
        string location
        date birth_date
        url website
    }

    Post {
        int id PK
        string title
        text content
        image image
        datetime created_at
        date updated_at
        int views
        int author FK
        int category FK
    }

    Category {
        int id PK
        string name
        string slug
    }

    Tag {
        int id PK
        string name
        string slug
    }

    Comment {
        int id PK
        text content
        datetime created_at
        datetime updated_at
        int post FK
        int author FK
        int parent FK
    }

    Like {
        int id PK
        int user FK
        int post FK
    }

    Bookmark {
        int id PK
        int user FK
        int post FK
    }



