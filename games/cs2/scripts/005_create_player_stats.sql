CREATE TABLE kaggle_links (kaggle_game_id INTEGER PRIMARY KEY, game_id INTEGER NOT NULL UNIQUE REFERENCES maps, swapped INTEGER NOT NULL, overlap INTEGER NOT NULL);
CREATE TABLE player_stats (game_id INTEGER REFERENCES maps, player_id INTEGER REFERENCES players, team INTEGER CHECK (team IN (1, 2)), kills REAL, deaths REAL, assists REAL, adr REAL, kast REAL, PRIMARY KEY (game_id, player_id));
