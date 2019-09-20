# LOG ANALYSIS

### In this project, you will stretch your SQL database skills. You will get practice interacting with a live database both from the command line and from your code. You will explore a large database with over a million rows. And you will build and refine complex queries and use them to draw business conclusions from data.

### Requirements
1. [Python3](https://www.python.org/download/releases/3.0/)
2. [Vagrant](https://www.vagrantup.com/)
3. [VirtualBox](https://www.vagrantup.com/)

### How to run the Project
1. Install Vagrant and Virtual Box
2. Download the data from [Here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
3. Open the file
4. Copy and paste the newsdata.sql file and content of this current repository
5. Navigate to the Udacity folder in your bash interface and inside that cd into the vagrant folder.
6. Open Git Bash and launch the virtual machine withvagrant up
7. Once Vagrant installs necessary files use vagrant ssh to continue.
8. The command line will now start with vagrant. Here cd into the /vagrant folder.
9. To load the database type `psql -d news -f newsdata.sql`
10. To run the database type `psql -d news`
11. You must run the commands from the Create views section here to run the python program successfully.
12. Use command `python3 log-results.py` to run the python program that fetches query results.
13. Create view article view using:
`create view logstar as select count(*) as stat, status, cast(time as date) as day from log where status like '%404' group by status, day order by stat desc limit 3;`
14. The second view code is:-`create view totalvisitors as select count(*) as visitors, cast(time as date) as errortime from log group by errortime;`
15. The last view code is:-`create  view errorcount as select * from logstar join totalvisitors on logstar.day = totalvisitors.errortime;`
