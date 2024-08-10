install:
	pip install -r requirements.txt
run: install
	uvicorn app.main:app --reload
build:
	docker buildx build --network=host --platform linux/amd64 -f Dockerfile -t your-registry/pdf-parse-service:latest .
	# docker push your-registry/pdf-parse-service:latest
build-local:
	docker buildx build --network=host -f Dockerfile -t your-registry/pdf-parse-service:latest .
deploy:
	kubectl --kubeconfig ~/.kube/mlops_zjk apply -f k8s-manifests
	kubectl --kubeconfig ~/.kube/mlops_zjk rollout restart deploy pdf-parse-service
