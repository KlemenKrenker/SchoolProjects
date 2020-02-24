/*==============================================================*/
/* DBMS name:      ORACLE Version 10gR2                         */
/* Created on:     6. 01. 2017 15:39:14                         */
/*==============================================================*/


alter table "Je zaposlen"
   drop constraint "FK_JE ZAPOS_JE ZAPOSL_ORGANIZA";

alter table "Je zaposlen"
   drop constraint "FK_JE ZAPOS_JE ZAPOSL_STARS";

alter table "JeOtrok/Stars"
   drop constraint "FK_JEOTROK/_JE OTROK_STARS";

alter table "JeOtrok/Stars"
   drop constraint "FK_JEOTROK/_JE STARS_OTROK";

alter table Naslov
   drop constraint "FK_NASLOV_JE V_KRAJ";

alter table Oseba
   drop constraint FK_OSEBA_STANUJE_NASLOV;

alter table Otrok
   drop constraint "FK_OTROK_JE SPOLA_SPOL";

alter table Otrok
   drop constraint "FK_OTROK_PRIPADA S_SKUPINA";

alter table Otrok
   drop constraint FK_OTROK_PRIPADAOS_OSEBA;

alter table "Se udeleži"
   drop constraint "FK_SE UDELE_SE UDELEŽ_IZLET";

alter table "Se udeleži"
   drop constraint "FK_SE UDELE_SE UDELEŽ_OTROK";

alter table Soba
   drop constraint "FK_SOBA_JE V SOBI_SKUPINA";

alter table Stars
   drop constraint FK_STARS_PRIPADAOS_OSEBA;

alter table Vzgojitelj
   drop constraint FK_VZGOJITE_PRIPADAZA_ZAPOSLEN;

alter table Zaposlen
   drop constraint FK_ZAPOSLEN_PRIPADAOS_OSEBA;

drop table Izlet cascade constraints;

drop index "Je zaposlen_FK2";

drop index "Je zaposlen_FK";

drop table "Je zaposlen" cascade constraints;

drop index "Je stars_FK";

drop index "Je otrok_FK";

drop table "JeOtrok/Stars" cascade constraints;

drop table Kraj cascade constraints;

drop index "Je v_FK";

drop table Naslov cascade constraints;

drop table Organizacija cascade constraints;

drop index Stanuje_FK;

drop table Oseba cascade constraints;

drop index "Pripada skupini_FK";

drop index "Je spola_FK";

drop table Otrok cascade constraints;

drop index "Se udeleži_FK2";

drop index "Se udeleži_FK";

drop table "Se udeleži" cascade constraints;

drop table Skupina cascade constraints;

drop index "Je v sobi_FK";

drop table Soba cascade constraints;

drop table Spol cascade constraints;

drop table Stars cascade constraints;

drop table Vzgojitelj cascade constraints;

drop table Zaposlen cascade constraints;

/*==============================================================*/
/* Table: Izlet                                                 */
/*==============================================================*/
create table Izlet  (
   ID                   INTEGER                         not null,
   Datum                DATE                            not null,
   UraOd                DATE                            not null,
   UraDo                DATE                            not null,
   Cena                 FLOAT                           not null,
   Opis                 VARCHAR2(1024),
   constraint PK_IZLET primary key (ID)
);

/*==============================================================*/
/* Table: "Je zaposlen"                                         */
/*==============================================================*/
create table "Je zaposlen"  (
   ID                   INTEGER                         not null,
   EMSO                 VARCHAR2(30)                    not null,
   constraint "PK_JE ZAPOSLEN" primary key (ID, EMSO)
);

/*==============================================================*/
/* Index: "Je zaposlen_FK"                                      */
/*==============================================================*/
create index "Je zaposlen_FK" on "Je zaposlen" (
   ID ASC
);

/*==============================================================*/
/* Index: "Je zaposlen_FK2"                                     */
/*==============================================================*/
create index "Je zaposlen_FK2" on "Je zaposlen" (
   EMSO ASC
);

/*==============================================================*/
/* Table: "JeOtrok/Stars"                                       */
/*==============================================================*/
create table "JeOtrok/Stars"  (
   EMSO                 VARCHAR2(30)                    not null,
   Otr_EMSO             VARCHAR2(30)                    not null,
   constraint "PK_JEOTROK/STARS" primary key (EMSO, Otr_EMSO)
);

/*==============================================================*/
/* Index: "Je otrok_FK"                                         */
/*==============================================================*/
create index "Je otrok_FK" on "JeOtrok/Stars" (
   EMSO ASC
);

/*==============================================================*/
/* Index: "Je stars_FK"                                         */
/*==============================================================*/
create index "Je stars_FK" on "JeOtrok/Stars" (
   Otr_EMSO ASC
);

/*==============================================================*/
/* Table: Kraj                                                  */
/*==============================================================*/
create table Kraj  (
   PostnaStevilka       INTEGER                         not null,
   ImeKraja             VARCHAR2(100)                   not null,
   constraint PK_KRAJ primary key (PostnaStevilka)
);

/*==============================================================*/
/* Table: Naslov                                                */
/*==============================================================*/
create table Naslov  (
   PostnaStevilka       INTEGER                         not null,
   ID                   INTEGER                         not null,
   Ulica                VARCHAR2(100)                   not null,
   HisnaStevilka        VARCHAR2(100)                   not null,
   constraint PK_NASLOV primary key (PostnaStevilka, ID)
);

/*==============================================================*/
/* Index: "Je v_FK"                                             */
/*==============================================================*/
create index "Je v_FK" on Naslov (
   PostnaStevilka ASC
);

/*==============================================================*/
/* Table: Organizacija                                          */
/*==============================================================*/
create table Organizacija  (
   ID                   INTEGER                         not null,
   Naziv                VARCHAR2(100)                   not null,
   TelefonskaStevilka   VARCHAR2(30)                    not null,
   Email                VARCHAR2(30),
   constraint PK_ORGANIZACIJA primary key (ID)
);

/*==============================================================*/
/* Table: Oseba                                                 */
/*==============================================================*/
create table Oseba  (
   EMSO                 VARCHAR2(30)                    not null,
   PostnaStevilka       INTEGER                         not null,
   ID                   INTEGER                         not null,
   Ime                  VARCHAR2(30)                    not null,
   Priimek              VARCHAR2(30)                    not null,
   constraint PK_OSEBA primary key (EMSO)
);

/*==============================================================*/
/* Index: Stanuje_FK                                            */
/*==============================================================*/
create index Stanuje_FK on Oseba (
   PostnaStevilka ASC,
   ID ASC
);

/*==============================================================*/
/* Table: Otrok                                                 */
/*==============================================================*/
create table Otrok  (
   EMSO                 VARCHAR2(30)                    not null,
   ID                   INTEGER                         not null,
   Sku_ID               INTEGER                         not null,
   LetnicaRojstva       NUMBER                          not null,
   LetnicaUpisa         NUMBER,
   constraint PK_OTROK primary key (EMSO)
);

/*==============================================================*/
/* Index: "Je spola_FK"                                         */
/*==============================================================*/
create index "Je spola_FK" on Otrok (
   ID ASC
);

/*==============================================================*/
/* Index: "Pripada skupini_FK"                                  */
/*==============================================================*/
create index "Pripada skupini_FK" on Otrok (
   Sku_ID ASC
);

/*==============================================================*/
/* Table: "Se udeleži"                                          */
/*==============================================================*/
create table "Se udeleži"  (
   EMSO                 VARCHAR2(30)                    not null,
   ID                   INTEGER                         not null,
   constraint "PK_SE UDELEŽI" primary key (EMSO, ID)
);

/*==============================================================*/
/* Index: "Se udeleži_FK"                                       */
/*==============================================================*/
create index "Se udeleži_FK" on "Se udeleži" (
   EMSO ASC
);

/*==============================================================*/
/* Index: "Se udeleži_FK2"                                      */
/*==============================================================*/
create index "Se udeleži_FK2" on "Se udeleži" (
   ID ASC
);

/*==============================================================*/
/* Table: Skupina                                               */
/*==============================================================*/
create table Skupina  (
   ID                   INTEGER                         not null,
   Naziv                VARCHAR2(30)                    not null,
   constraint PK_SKUPINA primary key (ID)
);

/*==============================================================*/
/* Table: Soba                                                  */
/*==============================================================*/
create table Soba  (
   StevilkaSobe         INTEGER                         not null,
   ID                   INTEGER                         not null,
   Kapaciteta           INTEGER                         not null,
   Opis                 VARCHAR2(1024),
   constraint PK_SOBA primary key (StevilkaSobe)
);

/*==============================================================*/
/* Index: "Je v sobi_FK"                                        */
/*==============================================================*/
create index "Je v sobi_FK" on Soba (
   ID ASC
);

/*==============================================================*/
/* Table: Spol                                                  */
/*==============================================================*/
create table Spol  (
   ID                   INTEGER                         not null,
   Naziv                VARCHAR2(30),
   constraint PK_SPOL primary key (ID)
);

/*==============================================================*/
/* Table: Stars                                                 */
/*==============================================================*/
create table Stars  (
   EMSO                 VARCHAR2(30)                    not null,
   TelefonskaStevila    VARCHAR2(30)                    not null,
   Email                VARCHAR2(30),
   constraint PK_STARS primary key (EMSO)
);

/*==============================================================*/
/* Table: Vzgojitelj                                            */
/*==============================================================*/
create table Vzgojitelj  (
   EMSO                 VARCHAR2(30)                    not null,
   Placa                INTEGER,
   TelefonskaStevilka   VARCHAR2(30)                    not null,
   Email                VARCHAR2(30),
   DavcnaStevilka       VARCHAR2(30)                    not null,
   constraint PK_VZGOJITELJ primary key (EMSO)
);

/*==============================================================*/
/* Table: Zaposlen                                              */
/*==============================================================*/
create table Zaposlen  (
   EMSO                 VARCHAR2(30)                    not null,
   TelefonskaStevilka   VARCHAR2(30)                    not null,
   Email                VARCHAR2(30),
   DavcnaStevilka       VARCHAR2(30)                    not null,
   constraint PK_ZAPOSLEN primary key (EMSO)
);

alter table "Je zaposlen"
   add constraint "FK_JE ZAPOS_JE ZAPOSL_ORGANIZA" foreign key (ID)
      references Organizacija (ID);

alter table "Je zaposlen"
   add constraint "FK_JE ZAPOS_JE ZAPOSL_STARS" foreign key (EMSO)
      references Stars (EMSO);

alter table "JeOtrok/Stars"
   add constraint "FK_JEOTROK/_JE OTROK_STARS" foreign key (EMSO)
      references Stars (EMSO);

alter table "JeOtrok/Stars"
   add constraint "FK_JEOTROK/_JE STARS_OTROK" foreign key (Otr_EMSO)
      references Otrok (EMSO);

alter table Naslov
   add constraint "FK_NASLOV_JE V_KRAJ" foreign key (PostnaStevilka)
      references Kraj (PostnaStevilka);

alter table Oseba
   add constraint FK_OSEBA_STANUJE_NASLOV foreign key (PostnaStevilka, ID)
      references Naslov (PostnaStevilka, ID);

alter table Otrok
   add constraint "FK_OTROK_JE SPOLA_SPOL" foreign key (ID)
      references Spol (ID);

alter table Otrok
   add constraint "FK_OTROK_PRIPADA S_SKUPINA" foreign key (Sku_ID)
      references Skupina (ID);

alter table Otrok
   add constraint FK_OTROK_PRIPADAOS_OSEBA foreign key (EMSO)
      references Oseba (EMSO);

alter table "Se udeleži"
   add constraint "FK_SE UDELE_SE UDELEŽ_IZLET" foreign key (ID)
      references Izlet (ID);

alter table "Se udeleži"
   add constraint "FK_SE UDELE_SE UDELEŽ_OTROK" foreign key (EMSO)
      references Otrok (EMSO);

alter table Soba
   add constraint "FK_SOBA_JE V SOBI_SKUPINA" foreign key (ID)
      references Skupina (ID);

alter table Stars
   add constraint FK_STARS_PRIPADAOS_OSEBA foreign key (EMSO)
      references Oseba (EMSO);

alter table Vzgojitelj
   add constraint FK_VZGOJITE_PRIPADAZA_ZAPOSLEN foreign key (EMSO)
      references Zaposlen (EMSO);

alter table Zaposlen
   add constraint FK_ZAPOSLEN_PRIPADAOS_OSEBA foreign key (EMSO)
      references Oseba (EMSO);

