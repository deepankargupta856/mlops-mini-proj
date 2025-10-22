import dagshub
import mlflow

mlflow.set_tracking_uri('https://dagshub.com/deepankargupta856/mlops-mini-proj.mlflow')
dagshub.init(repo_owner='deepankargupta856', repo_name='mlops-mini-proj', mlflow=True)


with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)