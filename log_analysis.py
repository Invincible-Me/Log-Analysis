import psycopg2, bleach

dbname = "news"


ques_1 = "What are the most popular three articles of all time?"
ques_2 = "Who are the most popular article authors of all time?"
ques_3 = "On which days did more than 1% of requests lead to errors? "


Answer_1 = "select title, views from article_view limit 3"
Answer_2 = """select authors.name,sum(article_view.views) as views from article_view,authors where authors.id = article_view.author group by authors.name order by views desc"""
Answer_3 = "select * from error_log_view where \"Percent Error\" > 1"



def get_posts(ques):
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect("dbname=news")
  c = db.cursor()
  c.execute(ques)
  results = c.fetchall()
  db.close()
  return results

  sol_1 = get_posts(Answer_1)
  sol_2 = get_posts(Answer_2)
  sol_3 = get_posts(Answer_3)

 def print_post(Answer):
    print(Answer)
    for result in Answer:
      print ('\t' + str(result[0]) + '=' + str(result[1]) + '%')

 print(ques_1)
 print_post(sol_1)
 print(ques_2)
 print_post(sol_2)
 print(ques_3)
 print_post(sol_3)


