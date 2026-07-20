CREATE TYPE employment_type_enum AS ENUM (
    'full_time',
    'part_time',
    'contract'
);

CREATE TYPE job_status_enum AS ENUM (
    'open',
    'closed',
    'draft'
);

CREATE TYPE application_status_enum AS ENUM (
    'pending',
    'reviewed',
    'shortlisted',
    'rejected'
);

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    bio TEXT,
    years_of_experience INT NOT NULL DEFAULT 0
        CHECK (years_of_experience >= 0),
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE companies (
    company_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    website VARCHAR(255),
    location VARCHAR(255),
    is_verified BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE skills (
    skill_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE jobs (
    job_id SERIAL PRIMARY KEY,
    company_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    location VARCHAR(255),
    salary_min INT NOT NULL
        CHECK (salary_min >= 0),
    salary_max INT NOT NULL
        CHECK (salary_max >= salary_min),
    employment_type employment_type_enum NOT NULL,
    status job_status_enum NOT NULL DEFAULT 'open',
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),

    CONSTRAINT fk_jobs_company
        FOREIGN KEY (company_id)
        REFERENCES companies(company_id)
        ON DELETE CASCADE
);

CREATE TABLE applications (
    application_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    job_id INT NOT NULL,
    cover_letter TEXT,
    status application_status_enum NOT NULL DEFAULT 'pending',
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
	
    CONSTRAINT fk_applications_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_applications_job
        FOREIGN KEY (job_id)
        REFERENCES jobs(job_id)
        ON DELETE CASCADE,

    CONSTRAINT uq_user_job
        UNIQUE (user_id, job_id)
);

CREATE TABLE user_skills (
    user_id INT NOT NULL,
    skill_id INT NOT NULL,

    PRIMARY KEY (user_id, skill_id),

    FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE,

    FOREIGN KEY (skill_id)
        REFERENCES skills(skill_id)
        ON DELETE CASCADE
);

CREATE TABLE job_skills (
    job_id INT NOT NULL,
    skill_id INT NOT NULL,

    PRIMARY KEY (job_id, skill_id),

    FOREIGN KEY (job_id)
        REFERENCES jobs(job_id)
        ON DELETE CASCADE,

    FOREIGN KEY (skill_id)
        REFERENCES skills(skill_id)
        ON DELETE CASCADE
);