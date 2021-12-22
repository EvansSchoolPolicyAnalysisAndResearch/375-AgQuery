-- data/update_data.sql
-- Copyright 2019 Evans Policy Analysis and Research Group (EPAR)

-- This project is licensed under the 3-Clause BSD License. Please see the 
-- license.txt file for more information.

-------------------------------------------------------------------------------
--                             CREATE NEW TABLES                             --
-------------------------------------------------------------------------------
CREATE TABLE public.estimates_update (
    id bigserial PRIMARY KEY,
    hexid text,
    geography text,
    survey text,
    instrument text,
    year text,
    "indicatorCategory" text,
    indicator text,
    units text,
    "cropDisaggregation" text,
    "genderDisaggregation" text,
    "farmSizeDisaggregation" text,
    ruralortotal text,
    subpopulation text,
    "currencyConversion" text,
    "indicatorLevel" text,
    weight text,
    "variableName" text,
    mean numeric,
    se numeric,
    sd numeric,
    p25 numeric,
    median numeric,
    p75 numeric,
    minim numeric,
    maxim numeric,
    n numeric,
    nover30 text
);

CREATE TABLE public.indcons_update (
    hexid text,
    indicator text PRIMARY KEY,
    "indicatorCategory" text,
    varnamestem text,
    "genderDisaggregation" text,
    "farmSizeDisaggregation" text,
    "cropDisaggregation" text,
    subpopulation text,
    rowsperinstrument text,
    "numerator" text, 
    "denominator" text,
    "units" text,
    "indicatorLevel" text,
    weight text,
    constructiondecision text,
    winsorizing text
);

CREATE TABLE public.cntrycons_update (
    id bigserial PRIMARY KEY,
    instrument text,
    cntrydec text,
    indicator text REFERENCES indcons_update
);


-------------------------------------------------------------------------------
--                             MODIFY THE TABLES                             --
-------------------------------------------------------------------------------

-- Import the data from the respective csv files --
\COPY estimates_update FROM 'estimates_cleaned.csv' CSV;
-- Remove the AgDev results
DELETE FROM public.estimates_update WHERE survey = 'AgDev Baseline';
\COPY indcons_update FROM 'decs_cleaned.csv' CSV;
\COPY cntrycons_update FROM 'ctry_decs_cleaned.csv' CSV;



-- Change owners of the new tables to epardata --
-- ALTER TABLE public.estimates_update OWNER TO epardata;
-- ALTER TABLE public.indcons_update OWNER to epardata;
-- ALTER TABLE public.cntrycons_update OWNER to epardata;

-- Suppress Nigerian Yield Estimates --
UPDATE estimates_update
SET
	mean = 0.0,
	se = 0.0,
	sd = 0.0,
	median = 0.0,
	minim = 0.0,
	maxim = 0.0,
	p25 = 0.0,
	p75 = 0.0
WHERE
	indicator LIKE 'Yield%' AND 
	geography = 'Nigeria';


-------------------------------------------------------------------------------
--                             REPLACE OLD TABLE                             --
-------------------------------------------------------------------------------
-- Out with the old -- 
DROP TABLE estimates, indcons, cntrycons;

-- In with the new --
ALTER TABLE estimates_update RENAME TO estimates;
ALTER TABLE indcons_update RENAME TO indcons;
ALTER TABLE cntrycons_update RENAME TO cntrycons;
