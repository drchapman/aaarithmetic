PRAGMA foreign_keys=ON;

-- Questions and Answers
create table questions
	(q_id integer primary key,
	question_text text,
	answer_text text);

-- Category Descriptions
create table categories
	(category_id integer primary key,
	category text
);

-- Definition of Question Sets
create table sets
	(set_id integer primary key,
	question_set text,
	category_id integer,
	foreign key(category_id) references categories(category_id)
);

-- Assignment of Questions to Sets
create table set_questions
	(set_id integer,
	q_id integer,
	foreign key(set_id) references sets(set_id),
	foreign key(q_id) references questions(q_id),
	constraint set_questions_pk1 primary key (set_id, q_id)
);

-- Session Creation
create table sessions 
	(session_id integer primary key,
	session_time default CURRENT_TIMESTAMP,
	set_id integer,
	user_name text,
	foreign key(set_id) references sets(set_id)
);


-- Log Attempts to Answer Questions
create table attempts
	(attempt_id integer primary key,
	session_id integer,
	q_id integer,
	attempt_time default CURRENT_TIMESTAMP,
	attempt_answer text,
	correct boolean default 0
);

-- Compare Attempt with Correct Answer and Update attempts to Record Result
create trigger attempts_answer_check
after insert on attempts
when
	new.attempt_answer = (select answer_text from questions where q_id=new.q_id)
begin
	update attempts
	set correct = 1
	where attempt_id = new.attempt_id;
end


