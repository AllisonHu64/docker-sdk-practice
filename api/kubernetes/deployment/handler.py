from os import path
import yaml
from kubernetes import client, config
from kubernetes.client.rest import ApiException

class KubeClientHandler():
    def __init__(self): 
        self.config = config.load_kube_config()
        self.client = client.AppsV1Api()
    
    def createNginxDeployment(self):
        with open(path.join(path.dirname(__file__), "nginx-deployment.yaml")) as f:
            dep = yaml.safe_load(f)
            resp = self.client.create_namespaced_deployment(
                body=dep, namespace="default"
            )
        print("Deployment created. status='%s'" % resp.metadata.name)

    def listDeployments(self):
        namespace = 'default' # str | object name and auth scope, such as for teams and projects
        pretty = 'true' # str | If 'true', then the output is pretty printed. (optional)
        label_selector="app=nginx"
        try:
            api_response = self.client.list_namespaced_deployment(namespace, pretty=pretty, label_selector=label_selector)
            print(api_response)
        except ApiException as e:
            print("Exception when calling AppsV1Api->list_namespaced_deployment: %s\n" % e)