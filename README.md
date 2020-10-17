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

## Where filter
Can be used with select/update/delete example

`select * from Track where Composer = 'U2'`

## Aliases
Change the name of a column for your own purpose so data makes more sense, ie,

`select Name as Track, Title as Album from Track;` - will display name as track and title as album

## Join
C1
`select Track.Name as Track, MediaType.Name as Media from Track inner join MediaType on Track.MediaTypeId = MediaType.MediaTypeId;`
Joins MediaType to Track through the use of MediaTypeId which is a column in common on both tables and renames both colums with aliases

## Order by
Order results by column, example
`select * from Album order by Title;` - Alphabetically order results using title, can also use desc modifier to descend
`select * from Album order by ArtistId, Title;` - Sort by ArtistId and within that by title. (double sort)
`Select EmployeeId, LastName, FirstName, HireDate from Employee order by HireDate desc limit 3;` Get last 3 employees that were hired

## Count
`select count(SupportRepId) as SupportRep4Clients from Customer where SupportRepId = 4;` Count the number of SupportRepIds where the SupportRep has a value of 4.

`select Employee.FirstName as RepFirstName, Employee.LastName as RepLastName, count(Customer.SupportRepId) from Employee inner join Customer on Employee.EmployeeId = Customer.SupportRepId where Employee.FirstName = 'Jane' and Employee.LastName = 'Peacock';` - Counts all instances of customers whos rep is called Joan Peacock

C2
`select Track.Name as TrackName, Genre.Name as GenreType from Track inner join Genre on Track.GenreId = Genre.GenreId where Genre.Name = 'Jazz';`
Selects track name and genre type, filters all but Jazz genre.

C3 - Multiple where clauses
`select Track.Name as TrackName, MediaType.Name as MediaType, Genre.Name as Genre from Track inner join MediaType on Track.MediaTypeId = MediaType.MediaTypeId inner join Genre on Track.GenreId = Genre.GenreId where MediaType.Name = 'Protected AAC audio file' and Genre.Name = 'Soundtrack';`

C4 - Show Playlist, Trackname, Album on Grunge Playlist
`select Playlist.Name as PlayListName, Track.Name as Track, Album.Title as Album from Playlist inner join PlaylistTrack on Playlist.PlaylistId = PlaylistTrack.PlaylistId inner join Track on PlaylistTrack.TrackId = Track.TrackId inner join Album on Track.AlbumId = Album.AlbumId where Playlist.Name = 'Grunge';`

C5 - In progress
`select Playlist.PlaylistId as ID, PlaylistTrack.TrackId as TrackName, Track.Name as Track from Playlist inner join PlaylistTrack on Playlist.PlaylistId = PlaylistTrack.PlaylistId inner join Track on PlaylistTrack.TrackId = Track.TrackId where Playlist.PlaylistId < 2;`