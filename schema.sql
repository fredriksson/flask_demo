drop table if exists entries;
create table entries (
	id intger primary key autoincrement,
	title string not null,
	text string not null
);
