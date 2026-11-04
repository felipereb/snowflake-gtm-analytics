-- Stage, file formats, raw tables and COPY INTO.
-- YOU WRITE THIS FILE (week 1 learning step). Claude reviews it.
--
-- Run as LOADER on LOAD_WH, in GTM.RAW.
--
-- What it needs:
--   1. A CSV file format for gzipped CSV with a header row.
--   2. A JSON file format for gzipped JSON Lines (activities).
--   3. One internal named stage for the raw files.
--   4. Raw tables for the five CSV entities, plus one table for activities
--      with a single VARIANT column and load metadata columns.
--   5. COPY INTO statements, one per entity, reading from the stage.
--
-- Questions to answer in comments as you go (these become README material):
--   - Why a named stage instead of the table stage or user stage?
--   - What does ON_ERROR do by default, and what did you choose?
--   - What happens if you run COPY INTO twice on the same files? Why?
--   - How do METADATA$FILENAME and METADATA$FILE_ROW_NUMBER help?
--
-- Upload files from your machine with SnowSQL / Snowflake CLI:
--   PUT file://data/raw/*.gz @<your_stage>/<entity>/ AUTO_COMPRESS = FALSE;

USE ROLE LOADER;
USE WAREHOUSE LOAD_WH;
USE SCHEMA GTM.RAW;

-- TODO: file formats

-- TODO: stage

-- TODO: raw tables

-- TODO: COPY INTO

-- TODO: checks (row counts per table, LOAD_HISTORY or COPY_HISTORY)
