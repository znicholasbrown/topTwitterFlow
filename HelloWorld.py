from prefect import task, Flow

@task
def say_hello():
    print("Hello, world!")

with Flow("Hello world flow") as flow:
    say_hello()

state = flow.run()