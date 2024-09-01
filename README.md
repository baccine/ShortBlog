
## WBS 
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

