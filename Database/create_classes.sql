CREATE TABLE time_entries (
    entry_id INT NOT NULL UNIQUE,
    title VARCHAR(100),
    date_worked DATE,
    time_begin TIME(),
    time_ended TIME(),
    project_id INT,
    client_id INT,
    task_id INT,
    billable BOOLEAN,
    PRIMARY KEY (entry_id)
);

CREATE TABLE project (
    project_id INT NOT NULL UNIQUE,
    title VARCHAR(100),
    client_id INT,
    hourly_rate FLOAT(24),
    project_estimate FLOAT(24),
    colour VARCHAR(20),
    PRIMARY KEY (project_id)
);

CREATE TABLE client (
    client_id INT NOT NULL UNIQUE,
    client_name VARCHAR(100),
    default_hourly_rate FLOAT(24),
    contact_name VARCHAR(100),
    contact_phone INT,
    billing_address_street_and_housenumber VARCHAR(100),
    billing_address_postal_code VARCHAR(12),
    billing_address_city VARCHAR(50),
    billing_address_state VARCHAR(25),
    billing_address_country VARCHAR(20),
    PRIMARY KEY (client_id)
);

CREATE TABLE task (
    task_id INT NOT NULL UNIQUE,
    task_name VARCHAR(50),
    task_hourly_rate FLOAT(24),
    PRIMARY KEY (task_id)
);
