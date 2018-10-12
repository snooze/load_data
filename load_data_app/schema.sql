DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS metallic_load;
DROP TABLE IF EXISTS shotshell_load;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE metallic_load (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  load_type TEXT NOT NULL,
  caliber TEXT NOT NULL,
  cart_case TEXT NOT NULL,
  powder_man TEXT NOT NULL,
  powder_name TEXT NOT NULL,
  powder_wt REAL NOT NULL,
  bullet_man TEXT NOT NULL,
  bullet_desc TEXT NOT NULL,
  bullet_wt REAL NOT NULL,
  primer_man TEXT NOT NULL,
  primer_type TEXT NOT NULL,
  coal REAL NOT NULL,
  notes TEXT,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

CREATE TABLE shotshell_load (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  load_type TEXT NOT NULL,
  guage TEXT NOT NULL,
  cart_case TEXT NOT NULL,
  powder_man TEXT NOT NULL,
  powder_name TEXT NOT NULL,
  powder_wt REAL NOT NULL,
  shot_type TEXT NOT NULL,
  shot_size TEXT NOT NULL,
  shot_weight TEXT NOT NULL,
  primer_man TEXT NOT NULL,
  primer_type TEXT NOT NULL,
  hull_type REAL NOT NULL,
  notes TEXT,
  FOREIGN KEY (author_id) REFERENCES user (id)
);
