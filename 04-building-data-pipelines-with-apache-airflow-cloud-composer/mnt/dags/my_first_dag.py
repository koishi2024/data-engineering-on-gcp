from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.utils import timezone

def _world():
   print("world")

with DAG(
   dag_id="my_first_dag",
   start_date=timezone.datetime(2024,1,22),
   schedule="3 0 * * *",
   catchup=False
):
   start = EmptyOperator(task_id="start")


   hello = BashOperator(
      task_id="hello",
      bash_command="ech 'hello'",
   )

   world = PythonOperator(
      task_id="world",
      python_callable=_world,
   )
   end = EmptyOperator(task_id="end")

   start>>hello>>end
   


  