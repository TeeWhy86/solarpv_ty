drop database if exists solarPVDB;

create database solarPVDB;

use solarPVDB;

CREATE TABLE User (
    UserID INT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    firstName VARCHAR(255) NOT NULL,
    middleName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    officePhone VARCHAR(255) NOT NULL,
    cellPhone VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);

CREATE TABLE Manufacturer (
    Name VARCHAR(255) NOT NULL,
    RegisteredCountry VARCHAR(255) NOT NULL,
    ContactPerson VARCHAR(255) REFERENCES User (username)
);

CREATE TABLE TestLab (
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    contactPerson VARCHAR(255) REFERENCES User (username)
);

CREATE TABLE TestResults (
    dataSource VARCHAR(255) REFERENCES TestLab (name),
    product VARCHAR(255) NOT NULL,
    reportingCondition VARCHAR(255) NOT NULL,
    testSequence VARCHAR(255) NOT NULL,
    testDate DATE NOT NULL,
    isc FLOAT NOT NULL,
    voc FLOAT NOT NULL,
    imp FLOAT NOT NULL,
    vmp FLOAT NOT NULL,
    pmp FLOAT NOT NULL,
    ff FLOAT NOT NULL,
    noct FLOAT NOT NULL
);

CREATE TABLE Product (
    modelnumber VARCHAR(255) NOT NULL,
    manufacturer VARCHAR(255) REFERENCES Manufacturer (Name),
    manufacturingdate DATE NOT NULL,
    length FLOAT NOT NULL,
    width FLOAT NOT NULL,
    weight FLOAT NOT NULL,
    cellarea FLOAT NOT NULL,
    celltechnology VARCHAR(255) NOT NULL,
    totalcells INT NOT NULL,
    cellsinseries INT NOT NULL,
    seriesstrings INT NOT NULL,
    bypassdiodes INT NOT NULL,
    seriesfuse FLOAT NOT NULL,
    material VARCHAR(255) NOT NULL,
    supplier VARCHAR(255) NOT NULL,
    supertype VARCHAR(255) NOT NULL,
    supermanufacturer VARCHAR(255) NOT NULL,
    subtype VARCHAR(255) NOT NULL,
    submanufacturer VARCHAR(255) NOT NULL,
    framematerial VARCHAR(255) NOT NULL,
    frameadhesive VARCHAR(255) NOT NULL,
    encaptype VARCHAR(255) NOT NULL,
    encapmanufacturer VARCHAR(255) NOT NULL,
    junctype VARCHAR(255) NOT NULL,
    juncmanufacturer VARCHAR(255) NOT NULL,
    juncadhesive VARCHAR(255) NOT NULL,
    cabletype VARCHAR(255) NOT NULL,
    connectortype VARCHAR(255) NOT NULL,
    maxvolt FLOAT NOT NULL,
    rvoc FLOAT NOT NULL,
    risc FLOAT NOT NULL,
    rvmp FLOAT NOT NULL,
    rimp FLOAT NOT NULL,
    rpmp FLOAT NOT NULL,
    rff FLOAT NOT NULL
);


INSERT INTO User (UserID, username, Password, firstName, middleName, lastName, address, officePhone, cellPhone, email) VALUES
(1, 'JChap', 'AhfahChoo7', 'Jeanette', 'Flag', 'Chapman', '706 Davis Avenue', '707-737-7333', '662-373-5527', 'JeanetteWChapman@armyspy.com'),
(2, 'AMoral', 'weeF7eyeimie', 'Athena', 'Hicks', 'Morales', '2492 Brownton Road', '707-737-7333', '662-373-5527', 'AthenaWMorales@teleworm.us'),
(3, 'RBuck', 'Fu4TaeJah3j', 'Robert', 'Cobra', 'Buckman', '832 Granville Lane', '707-737-7333', '662-373-5527', 'RobertEBuckman@teleworm.us'),
(4, 'SPars',  'Ahs6Vavee9Ee', 'Steven', 'Clock', 'Parsons', '750 Primrose Lane', '707-737-7333', '662-373-5527', 'StevenMParsons@armyspy.com'),
(5, 'CClem', 'ahShaeth1', 'Chelsea', 'Tuft', 'Clemmer', '2214 Arthur Avenue', '707-737-7333', '662-373-5527', 'ChelseaGClemmer@rhyta.com'),
(6, 'MPat', 'ef0EileeFoh', 'Matthew', 'Sing', 'Patrick', '3908 Sunrise Road', '707-737-7333', '662-373-5527', 'MatthewKPatrick@armyspy.com');

-- auto-generated definition
create table certificate
(
    ID            int auto_increment
        primary key,
    certnumber    int  not null,
    location      int  not null,
    reportnumber  int  not null,
    contactID     int  not null,
    teststandard  int  not null,
    product       int  not null,
    certissuedate date not null,
    constraint certificate_location_locationID_fk
        foreign key (location) references location (locationID)
            on update cascade on delete cascade,
    constraint certificate_product_modelNum_fk
        foreign key (product) references product (modelNum)
            on update cascade on delete cascade,
    constraint certificate_teststandard_standardID_fk
        foreign key (teststandard) references teststandard (standardID)
            on update cascade on delete cascade,
    constraint certificate_user_UserID_fk
        foreign key (contactID) references user (UserID)
            on update cascade on delete cascade
);

-- auto-generated definition
create table client
(
    clientID   int auto_increment
        primary key,
    clientCode varchar(255) not null,
    clientName varchar(255) not null,
    clientType varchar(255) not null
);

-- auto-generated definition
create table location
(
    locationID  int auto_increment
        primary key,
    clientID    int          not null,
    address1    varchar(255) not null,
    address2    varchar(255) null,
    city        varchar(255) not null,
    state       varchar(255) not null,
    postalcode  int          null,
    country     varchar(3)   not null,
    phonenumber varchar(12)  null,
    faxnumber   varchar(12)  null,
    constraint location_client_clientID_fk
        foreign key (clientID) references client (clientID)
            on update cascade on delete cascade
);

-- auto-generated definition
create table product
(
    modelNum          int          not null
        primary key,
    name              varchar(255) not null,
    celltechnology    varchar(255) not null,
    manufacturer      varchar(255) null,
    totalcells        int          not null,
    cellsinseries     int          not null,
    seriesstrings     int          not null,
    bypassdiodes      int          not null,
    length            float        not null,
    width             float        not null,
    weight            float        not null,
    supertype         varchar(255) not null,
    supermanufacturer varchar(255) not null,
    subtype           varchar(255) not null,
    submanufacturer   varchar(255) not null,
    frametype         varchar(255) not null,
    frameadhesive     varchar(255) not null,
    encaptype         varchar(255) not null,
    encapmanufacturer varchar(255) not null,
    junctype          varchar(255) not null,
    juncmanufacturer  varchar(255) not null
);

-- auto-generated definition
create table teststandard
(
    standardID    int auto_increment
        primary key,
    standardname  varchar(255) not null,
    description   varchar(255) not null,
    publisheddate date         not null
);

-- auto-generated definition
create table user
(
    UserID      int auto_increment
        primary key,
    clientID    int          null,
    username    varchar(255) not null,
    password    varchar(255) not null,
    firstName   varchar(255) not null,
    middleName  varchar(255) not null,
    lastName    varchar(255) not null,
    jobtitle    varchar(255) not null,
    email       varchar(255) not null,
    officePhone varchar(255) not null,
    cellPhone   varchar(255) not null,
    prefix      varchar(5)   null,
    isstaff     binary(1)    not null,
    constraint user_client_clientID_fk
        foreign key (clientID) references client (clientID)
            on update cascade on delete cascade
);

