-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/5dsVHw
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "Departments" (
    "dept_id" VARCHAR(10)   NOT NULL,
    "dept_name" VARCHAR(200)   NOT NULL,
    CONSTRAINT "pk_Departments" PRIMARY KEY (
        "dept_id"
     )
);

CREATE TABLE "Dept_Emp" (
    "emp_no" int   NOT NULL,
    "dept_no" VARCHAR(10)   NOT NULL,
    "from_date" date   NOT NULL,
    "to_date" date   NOT NULL
);

CREATE TABLE "Employee" (
    "emp_no" int   NOT NULL,
    "birth_date" date   NOT NULL,
    "first_name" VARCHAR(200)   NOT NULL,
    "last_name" VARCHAR(200)   NOT NULL,
    "gender" VARCHAR(200)   NOT NULL,
    "hire_date" date   NOT NULL,
    CONSTRAINT "pk_Employee" PRIMARY KEY (
        "emp_no"
     )
);

CREATE TABLE "titles" (
    "emp_no" int   NOT NULL,
    "title" VARCHAR(200)   NOT NULL,
    "from_date" date   NOT NULL,
    "to_date" date   NOT NULL
);

CREATE TABLE "salary" (
    "emp_no" int   NOT NULL,
    "salary" float   NOT NULL,
    "from_date" date   NOT NULL,
    "to_date" date   NOT NULL,
    CONSTRAINT "pk_salary" PRIMARY KEY (
        "emp_no"
     )
);

CREATE TABLE "Dept_manager" (
    "dept_id" VARCHAR(10)   NOT NULL,
    "emp_no" int   NOT NULL,
    "from_date" date   NOT NULL,
    "to_date" date   NOT NULL
);

ALTER TABLE "Dept_Emp" ADD CONSTRAINT "fk_Dept_Emp_emp_no" FOREIGN KEY("emp_no")
REFERENCES "Employee" ("emp_no");

ALTER TABLE "Dept_Emp" ADD CONSTRAINT "fk_Dept_Emp_dept_no" FOREIGN KEY("dept_no")
REFERENCES "Departments" ("dept_id");

ALTER TABLE "titles" ADD CONSTRAINT "fk_titles_emp_no" FOREIGN KEY("emp_no")
REFERENCES "Employee" ("emp_no");

ALTER TABLE "salary" ADD CONSTRAINT "fk_salary_emp_no" FOREIGN KEY("emp_no")
REFERENCES "Employee" ("emp_no");

ALTER TABLE "Dept_manager" ADD CONSTRAINT "fk_Dept_manager_dept_id" FOREIGN KEY("dept_id")
REFERENCES "Departments" ("dept_id");

ALTER TABLE "Dept_manager" ADD CONSTRAINT "fk_Dept_manager_emp_no" FOREIGN KEY("emp_no")
REFERENCES "Employee" ("emp_no");

select * from "Departments"
select * from "Dept_Emp"
select * from "Dept_manager"
select * from "Employee"
select * from "salary"
select * from "titles"

--List the following details of each employee: employee number, last name, first name, gender, and salary.
select "Employee".emp_no, last_name, first_name, gender,salary from "Employee" join "salary" on "Employee".emp_no="salary".emp_no

--List employees who were hired in 1986.
select * from "Employee" where cast((hire_date)as varchar(20)) like '1986%'

--List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.
select dm.dept_id, d.dept_name, e.emp_no, e.last_name, e.first_name,s.from_date, s.to_date
from "Employee" as e join "salary" as s on e.emp_no = s.emp_no join "Dept_manager" as dm on e.emp_no = dm.emp_no
join "Departments" as d on dm.dept_id=d.dept_id

--List the department of each employee with the following information: employee number, last name, first name, and department name.
select e.emp_no, last_name, first_name, d.dept_name from "Employee" as e join "Dept_Emp" as de on e.emp_no=de.emp_no
join "Departments" as d on de.dept_no = d.dept_id

--List all employees whose first name is "Hercules" and last names begin with "B."
select * from "Employee" where first_name = 'Hercules' and last_name like 'B%'

--List all employees in the Sales department, including their employee number, last name, first name, and department name
select e.emp_no, last_name, first_name, d.dept_name from "Employee" as e join "Dept_Emp" as de on e.emp_no=de.emp_no
join "Departments" as d on de.dept_no = d.dept_id where d.dept_name ='Sales'

--List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
select e.emp_no, last_name, first_name, d.dept_name from "Employee" as e join "Dept_Emp" as de on e.emp_no=de.emp_no
join "Departments" as d on de.dept_no = d.dept_id where d.dept_name ='Sales' or d.dept_name='Development'

--In descending order, list the frequency count of employee last names, i.e., how many employees share each last name
select count(last_name), last_name from "Employee" group by last_name order by last_name desc


