

####
Local port : 4399 


####
XComs [“cross-communication”]
Note that XComs are similar to Variables, but are specifically designed for inter-task communication rather than global settings.

XComs let tasks exchange messages, allowing more nuanced forms of control and shared state.
The name is an abbreviation of “cross-communication”. XComs are principally defined by a key, value, and timestamp,
but also track attributes like the task/DAG that created the XCom and when it should become visible. 

Any object that can be pickled can be used as an XCom value, so users should make sure to use objects of appropriate size.

XComs can be “pushed” (sent) or “pulled” (received). When a task pushes an XCom, 
it makes it generally available to other tasks. Tasks can push XComs at any time by calling the xcom_push() method. 
In addition, if a task returns a value (either from its Operator’s execute() method, or from a PythonOperator’s python_callable function), then an XCom containing that value is automatically pushed.

Tasks call xcom_pull() to retrieve XComs, optionally applying filters based on criteria like key, source task_ids, and source dag_id. By default, xcom_pull() filters for the keys that are automatically given to XComs when they are pushed by being returned from execute functions (as opposed to XComs that are pushed manually).

If xcom_pull is passed a single string for task_ids, then the most recent XCom value from that task is returned; if a list of task_ids is passed, then a corresponding list of XCom values is returned.

# inside a PythonOperator called 'pushing_task'
def push_function():
    return value

# inside another PythonOperator where provide_context=True
def pull_function(**context):
    value = context['task_instance'].xcom_pull(task_ids='pushing_task')
It is also possible to pull XCom directly in a template, here’s an example of what this may look like:

SELECT * FROM {{ task_instance.xcom_pull(task_ids='foo', key='table_name') }}





#######
Hive Partition Sensor:
Waits for a set of partitions to show up in Hive 

table (str) – The name of the table to wait for, supports the dot notation (my_database.my_table)

partition (str) – The partition clause to wait for. This is passed as is to the metastore Thrift client get_partitions_by_filter method, and apparently supports SQL like notation as in ds='2015-01-01' AND type='value' and comparison operators as in "ds>=2015-01-01"

metastore_conn_id (str) – reference to the metastore thrift service connection id

template_fields= ['schema', 'table', 'partition'][source]


#####
Stage Exchnage check operator : [https://airflow.apache.org/docs/apache-airflow/1.10.2/concepts.html?highlight=branch%20operator]

Airbnb uses the stage-check-exchange pattern when loading data. 
Data is staged in a temporary table, after which data quality checks are performed against that table. 
Once the checks all pass the partition is moved into the production table.

####
Branch Python Operator - BranchPythonOperator :
Sometimes you need a workflow to branch, or only go down a certain path based on an arbitrary condition 
which is typically related to something that happened in an upstream task. One way to do this is by using the BranchPythonOperator.

######
email operator :
to send out email on completion 
email.set_upstream(dag.leaves)
