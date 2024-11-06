CREATE TRIGGER trigger_name
{BEFORE | AFTER | INSTEAD OF} 
{INSERT | UPDATE | DELETE}
ON table_name
FOR EACH ROW
BEGIN
    -- Trigger logic (SQL statements)
END;
