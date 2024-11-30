CREATE TABLE Conversations (
    ID INT IDENTITY(1,1) PRIMARY KEY, -- ستون شناسه (کلید اصلی)
    UserInput NVARCHAR(MAX) NOT NULL, -- ورودی کاربر
    AssistantResponse NVARCHAR(MAX) NOT NULL, -- پاسخ دستیار
    Timestamp DATETIME NOT NULL DEFAULT GETDATE() -- زمان مکالمه
);
