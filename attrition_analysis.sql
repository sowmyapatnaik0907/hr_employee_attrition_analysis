
-- ==========================================
-- HR EMPLOYEE ATTRITION ANALYSIS
-- SQL BUSINESS QUERIES
-- ==========================================


-- QUERY 1: TOTAL EMPLOYEES

SELECT
    COUNT(*) AS Total_Employees
FROM employee_attrition;


-- QUERY 2: EMPLOYEES WHO LEFT

SELECT
    COUNT(*) AS Employees_Left
FROM employee_attrition
WHERE Attrition = 'Yes';


-- QUERY 3: ACTIVE EMPLOYEES

SELECT
    COUNT(*) AS Active_Employees
FROM employee_attrition
WHERE Attrition = 'No';


-- QUERY 4: OVERALL ATTRITION RATE

SELECT
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate
FROM employee_attrition;


-- QUERY 5: DEPARTMENT-WISE ATTRITION

SELECT
    Department,
    COUNT(*) AS Total_Employees,

    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
    AS Employees_Left,

    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate

FROM employee_attrition

GROUP BY Department

ORDER BY Attrition_Rate DESC;


-- QUERY 6: JOB ROLE-WISE ATTRITION

SELECT
    JobRole,
    COUNT(*) AS Total_Employees,

    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
    AS Employees_Left,

    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate

FROM employee_attrition

GROUP BY JobRole

ORDER BY Attrition_Rate DESC;


-- QUERY 7: OVERTIME VS ATTRITION

SELECT
    OverTime,
    COUNT(*) AS Total_Employees,

    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
    AS Employees_Left,

    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate

FROM employee_attrition

GROUP BY OverTime

ORDER BY Attrition_Rate DESC;


-- QUERY 8: JOB SATISFACTION VS ATTRITION

SELECT
    JobSatisfaction,
    COUNT(*) AS Total_Employees,

    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
    AS Employees_Left,

    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate

FROM employee_attrition

GROUP BY JobSatisfaction

ORDER BY JobSatisfaction;


-- QUERY 9: AGE GROUP VS ATTRITION

SELECT
    CASE
        WHEN Age <= 25 THEN '18-25'
        WHEN Age <= 35 THEN '26-35'
        WHEN Age <= 45 THEN '36-45'
        WHEN Age <= 55 THEN '46-55'
        ELSE '55+'
    END AS Age_Group,

    COUNT(*) AS Total_Employees,

    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
    AS Employees_Left,

    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS Attrition_Rate

FROM employee_attrition

GROUP BY Age_Group

ORDER BY Attrition_Rate DESC;


-- QUERY 10: MONTHLY INCOME VS ATTRITION

SELECT
    Attrition,
    ROUND(AVG(MonthlyIncome), 2) AS Average_Monthly_Income

FROM employee_attrition

GROUP BY Attrition;
