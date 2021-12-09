CREATE TABLE client (
    client_id INT NOT NULL UNIQUE AUTO_INCREMENT,
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

CREATE TABLE project (
    project_id INT NOT NULL UNIQUE AUTO_INCREMENT,
    title VARCHAR(100),
    client_id INT NOT NULL,
    hourly_rate FLOAT(24),
    project_estimate FLOAT(24),
    colour VARCHAR(20),
    PRIMARY KEY (project_id),
    FOREIGN KEY (client_id) REFERENCES client(client_id)
);

CREATE TABLE task (
    task_id INT NOT NULL UNIQUE AUTO_INCREMENT,
    task_name VARCHAR(50),
    task_hourly_rate FLOAT(24),
    PRIMARY KEY (task_id)
);

CREATE TABLE time_entries (
    entry_id INT NOT NULL UNIQUE AUTO_INCREMENT,
    title VARCHAR(100),
    date_worked DATE,
    time_begin TIME,
    time_ended TIME,
    project_id INT NOT NULL,
    client_id INT NOT NULL,
    task_id INT NOT NULL,
    billable BOOLEAN,
    PRIMARY KEY (entry_id),
    FOREIGN KEY (project_id) REFERENCES project(project_id),
    FOREIGN KEY (client_id) REFERENCES client(client_id),
    FOREIGN KEY (task_id) REFERENCES task(task_id)
);
