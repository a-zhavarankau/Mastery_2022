CREATE DATABASE mastery_sql;

USE mastery_sql;

CREATE TABLE IF NOT EXISTS employee (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    login VARCHAR(25) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    employee_role enum('Default','PM','Administrator') NOT NULL,
    salary MEDIUMINT unsigned DEFAULT NULL,
    department INT DEFAULT NULL,
    last_login_date DATE DEFAULT NULL,
    created_date DATE DEFAULT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_employee_department_id FOREIGN KEY (department) REFERENCES department(id)
);

CREATE TABLE IF NOT EXISTS department (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    create_date DATE DEFAULT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS project (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255) DEFAULT NULL,
    project_status enum('Planned','Ongoing','Stopped') NOT NULL,
    created_status TINYINT DEFAULT 0,
    start_date DATE DEFAULT NULL,
    stop_date DATE DEFAULT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS empl_proj (
    empl_id INT NOT NULL,
    proj_id INT NOT NULL,
    PRIMARY KEY (empl_id,proj_id),
    CONSTRAINT fk_empl_proj_employee_id FOREIGN KEY (empl_id) REFERENCES employee(id),
    CONSTRAINT fk_empl_proj_project_id FOREIGN KEY (proj_id) REFERENCES project(id)
);

