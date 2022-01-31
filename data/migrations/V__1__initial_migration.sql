create table if not exists migrations (
    version integer primary key,
    filename text not null,
    migration_date text
);

create table if not exists users (
    id integer primary key,
    username text unique not null,
    password text not null,
    is_admin bit not null,
    created_at text not null,
    firstname text,
    lastname text
);

-- default password is admin-password
insert into users
values('1', 'admin', '861dc45fb50349654a615674099ed594', 1, current_date, '', 'Administrator');

insert into migrations
values ('1', 'Initial migration', current_date);