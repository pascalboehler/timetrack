/* create test clients */
INSERT INTO client (
    client_name,
    contact_name,
    contact_phone,
    billing_address_street_and_housenumber,
    billing_address_postal_code,
    billing_address_city,
    billing_address_state,
    billing_address_country
)
VALUES (
    'Company A',
    'Hans Mueller',
    491234567890,
    'Industriestrasse 1',
    '12345',
    'Industriestadt',
    'HESSEN',
    'GERMANY'
);

INSERT INTO client (
    client_name,
    contact_name,
    contact_phone,
    billing_address_street_and_housenumber,
    billing_address_postal_code,
    billing_address_city,
    billing_address_state,
    billing_address_country
)
VALUES (
    'Company B',
    'Gert Zimmer',
    491234567890,
    'Industriestrasse 2',
    '12345',
    'Industriestadt',
    'HESSEN',
    'GERMANY'
);

/* Create test projects */
INSERT INTO project (title, client_id, hourly_rate, project_estimate, colour)
VALUES ('New Website', 1, 25.0, 1000.0, 'blue');
INSERT INTO project (title, client_id, hourly_rate, project_estimate, colour)
VALUES ('New App', 2, 50.0, 10000.0, 'blue');

/* Create test tasks */
INSERT INTO task (task_name, project_id, task_hourly_rate)
VALUES ('Documentation', 1, 10.0);
INSERT INTO task (task_name, project_id, task_hourly_rate)
VALUES ('Development', 1, 100.0);
INSERT INTO task (task_name, project_id, task_hourly_rate)
VALUES ('Documentation', 2, 10.0);
INSERT INTO task (task_name, project_id, task_hourly_rate)
VALUES ('Design', 1, 150.0);
INSERT INTO task (task_name, project_id, task_hourly_rate)
VALUES ('Development', 1, 150.0);

/* Create test time entries */
INSERT INTO time_entry (title, date_begin, time_begin, date_end, time_end, project_id, client_id, task_id)
VALUES ('Added new feature to project docs', '2021-09-21', '11:59:00', '2021-09-21', '13:30:00', 1, 1, 1);
INSERT INTO time_entry (title, date_begin, time_begin, date_end, time_end, project_id, client_id, task_id)
VALUES ('Designed new WebUI', '2021-09-22', '08:30:00', '2021-09-22', '19:30:00', 1, 1, 2);
INSERT INTO time_entry (title, date_begin, time_begin, date_end, time_end, project_id, client_id, task_id)
VALUES ('Fixed layout on mobile devices', '2021-09-23', '10:15:00', '2021-09-23', '10:35:00', 1, 1, 2);
INSERT INTO time_entry (title, date_begin, time_begin, date_end, time_end, project_id, client_id, task_id)
VALUES ('Added new feature to project docs', '2021-10-21', '11:59:00', '2021-09-21', '13:30:00', 2, 2, 3);
INSERT INTO time_entry (title, date_begin, time_begin, date_end, time_end, project_id, client_id, task_id)
VALUES ('Sketched out new App Interface', '2021-10-22', '8:00:00', '2021-10-22', '12:00:00', 2, 2, 4);
INSERT INTO time_entry (title, date_begin, time_begin, date_end, time_end, project_id, client_id, task_id)
VALUES ('Implemented new layout', '2021-09-23', '8:00:00', '2021-09-23', '19:00:00', 2, 2, 5);