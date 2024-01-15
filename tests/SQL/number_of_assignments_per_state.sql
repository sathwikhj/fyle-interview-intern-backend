-- Write query to get number of assignments for each state
-- tests/SQL/number_of_assignments_per_state.sql

SELECT state, COUNT(*) FROM assignments GROUP BY state ORDER BY state;

