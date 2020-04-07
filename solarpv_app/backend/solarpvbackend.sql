drop database if exists solarPV;

create database solarPV;

use solarPV;

-- auto-generated definition
create table client
(
    clientID   int auto_increment
        primary key,
    clientCode varchar(60) not null,
    clientName varchar(60) not null,
    clientType varchar(60) not null
);

-- auto-generated definition
create table location
(
    locationID  int auto_increment
        primary key,
    clientID    int          not null,
    address1    varchar(255) not null,
    address2    varchar(255) null,
    city        varchar(60) not null,
    state       varchar(60) not null,
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
    name              varchar(60) not null,
    celltechnology    varchar(60) not null,
    manufacturer      varchar(60) null,
    totalcells        int          not null,
    cellsinseries     int          not null,
    seriesstrings     int          not null,
    bypassdiodes      int          not null,
    length            float        not null,
    width             float        not null,
    weight            float        not null,
    supertype         varchar(60) not null,
    supermanufacturer varchar(60) not null,
    subtype           varchar(60) not null,
    submanufacturer   varchar(60) not null,
    frametype         varchar(60) not null,
    frameadhesive     varchar(60) not null,
    encaptype         varchar(60) not null,
    encapmanufacturer varchar(60) not null,
    junctype          varchar(60) not null,
    juncmanufacturer  varchar(60) not null
);

-- auto-generated definition
create table teststandard
(
    standardID    int auto_increment
        primary key,
    standardname  varchar(60) not null,
    description   varchar(60) not null,
    publisheddate date         not null
);

-- auto-generated definition
create table user
(
    UserID      int auto_increment
        primary key,
    clientID    int          null,
    username    varchar(60) not null,
    password    varchar(60) not null,
    firstName   varchar(60) not null,
    middleName  varchar(60) not null,
    lastName    varchar(60) not null,
    jobtitle    varchar(60) not null,
    email       varchar(60) not null,
    officePhone varchar(60) not null,
    cellPhone   varchar(60) not null,
    prefix      varchar(5)   null,
    isstaff     binary(1)    not null,
    constraint user_client_clientID_fk
        foreign key (clientID) references client (clientID)
            on update cascade on delete cascade
);

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