CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    set N = N-1;
  RETURN (
    
    SELECT DISTINCT salary
    FROM employee
    ORDER BY salary desc
    LIMIT 1 OFFSET N 
  );
END
