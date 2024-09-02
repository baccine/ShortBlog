
erDiagram
    User {
        int id PK
        string username
        string email
        string password
    }
    
    Post {
        int id PK
        string title
        string content
        date created_at
        date updated_at
        int user_id FK
        int category_id FK
    }
    
    Category {
        int id PK
        string name
        string slug
    }
    
    Comment {
        int id PK
        string content
        date created_at
        int user_id FK
        int post_id FK
    }
    
    Tag {
        int id PK
        string name
        string slug
    }
    
    PostTag {
        int post_id FK
        int tag_id FK
    }
    
    User ||--o{ Post : "writes"
    User ||--o{ Comment : "makes"
    Category ||--o{ Post : "categorizes"
    Post ||--o{ Comment : "receives"
    Post ||--o{ PostTag : "has"
    Tag ||--o{ PostTag : "tags"
