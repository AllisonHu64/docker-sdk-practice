from api.kubernetes.deployment.handler import KubeClientHandler
import docker
import urllib3
from os import path
import yaml

clienthandler = KubeClientHandler()
# clienthandler.listDeployments()
clienthandler.createNginxDeployment()
