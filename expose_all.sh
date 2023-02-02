microk8s.kubectl expose deployment logr-deployment  --type=NodePort --name=logr-service  --port=5002
microk8s.kubectl expose deployment front-deployment --type=NodePort --name=front-service --port=5000
microk8s.kubectl expose deployment back-deployment  --type=NodePort --name=back-service  --port=5001
microk8s.kubectl expose deployment db-deployment    --type=NodePort --name=db-service    --port=7000

