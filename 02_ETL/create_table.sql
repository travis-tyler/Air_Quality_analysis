CREATE TABLE daily_aqi (
	id SERIAL PRIMARY KEY,
    state VARCHAR(40),
    county VARCHAR,
    county_code Integer,
    date DATE,
    aqi Integer,
    category VARCHAR,
    defining_parameter VARCHAR,
    number_sites Integer,
    month_day VARCHAR);