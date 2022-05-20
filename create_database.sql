DROP DATABASE Mercy_Hospital;
CREATE DATABASE Mercy_Hospital;
USE Mercy_Hospital;
--
CREATE TABLE station (
	station_ID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT
);
--
CREATE TABLE pharmacist (
	pharmacist_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    telephone VARCHAR(255) NOT NULL,
    station_id INT NOT NULL
);

ALTER TABLE pharmacist ADD FOREIGN KEY (station_id) REFERENCES station (station_id)
ON DELETE CASCADE 
ON UPDATE CASCADE;
--
CREATE TABLE patient (
	patient_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    telephone VARCHAR(255) NOT NULL
);

CREATE TABLE file (
	file_id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    diagnosis TEXT NOT NULL,
    patient_id INT NOT NULL
);

ALTER TABLE file ADD FOREIGN KEY (patient_id) REFERENCES patient (patient_id)
ON DELETE CASCADE 
ON UPDATE CASCADE;
--
CREATE TABLE doctor (
	doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    telephone VARCHAR(255) NOT NULL
);

CREATE TABLE prescription (
	pres_id INT AUTO_INCREMENT PRIMARY KEY,
    is_valid BOOLEAN NOT NULL,
    special_instruction TEXT,
    station VARCHAR(255),
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    pharmacist_id INT NOT NULL
);

ALTER TABLE prescription ADD COLUMN isValid BOOLEAN NOT NULL;


ALTER TABLE prescription ADD FOREIGN KEY (patient_id) REFERENCES patient (patient_id)
ON DELETE CASCADE 
ON UPDATE CASCADE;

ALTER TABLE prescription ADD FOREIGN KEY (doctor_id) REFERENCES doctor (doctor_id)
ON DELETE CASCADE 
ON UPDATE CASCADE;

ALTER TABLE prescription ADD FOREIGN KEY (pharmacist_id) REFERENCES pharmacist (pharmacist_id)
ON DELETE CASCADE 
ON UPDATE CASCADE;

CREATE TABLE medicine (
	medicine_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price INT NOT NULL,
    description TEXT
);

CREATE TABLE medicine_included (
	pres_id INT NOT NULL,
    medicine_id INT NOT NULL,
    amount INT NOT NULL,
    PRIMARY KEY (pres_id, medicine_id)
);

ALTER TABLE medicine_included ADD FOREIGN KEY (pres_id) REFERENCES prescription (pres_id)
ON DELETE CASCADE 
ON UPDATE CASCADE;

ALTER TABLE medicine_included ADD FOREIGN KEY (medicine_id) REFERENCES medicine (medicine_id)
ON DELETE CASCADE 
ON UPDATE CASCADE;