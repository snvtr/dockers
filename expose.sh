#kubectl expose deployment logr-deployment --type=NodePort --name=logr-service
#kubectl expose deployment front-deployment --type=NodePort --name=front-service

kubectl expose deployment back-deployment --type=NodePort --name=back-service
kubectl expose deployment db-deployment --type=NodePort --name=db-service

