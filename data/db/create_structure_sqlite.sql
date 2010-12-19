drop table if exists Video;
drop table if exists Music;
drop table if exists Pictures;

/* Video table definition */
create table Video (
	id integer primary key,
	parent_video_id integer,
	owner_id integer,
	/* Movie info, mainly form IMDb site */
	original_title text,
	localized_title text,
	release_date integer,
	director text,
	genres text,
	description text,
	cast text,
	imdb_rate real,
	/* Movie media info */
	file_path text,
	vcodec varchar(16),
	acodec varchar(16),
	resolution varchar(16),
	bitrate varchar(16),
	auidio_streams text
);