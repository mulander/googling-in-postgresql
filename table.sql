CREATE TABLE emails(
        id bigserial,
        file_path text,
        subject text,
        body text,
        document tsvector
);
