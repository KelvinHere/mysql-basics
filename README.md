# A journey into the basics of MySql

A repo to learn MySql basics.

## Simple commands

* `mysql` to enter MySql CLI
* `show databases;` list databases
* `use DatabaseName;` changes database to use
* `desc TableName` describes table, shows attributes
* `Select * from TableName` Returns all from TableName (* for all or replace with fields seperated by comma)

## Join command
`mysql> select Title, Name from Album
    -> join Artist on Album.ArtistId = Artist.ArtistId
    -> limit 5;`

* Gets Title and Name from Album table
* joins the Artist table and pulls artist name from Artist table

## Insert command
`insert into TableName (Name) values ('New');` Inserts a new value into a table

* Don't worry about creating a primary key for fields that include an Auto-Increment 

`select last_insert_id();` will show you the last intserted ID

## Select command
`select Name FROM TableName where PrimaryKeyId = 27;` Will return the field Name from a table where 27 matches the primary key


## Update command
`update TableName set Name = 'NewName' where Name = 'OldName';` Takes a table and will update the field 'Name' with a new name by giving it an old name

## Delete command
`delete from TableName where Name = ‘Record’;` deletes 'Record' record from TableName