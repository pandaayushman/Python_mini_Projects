import boto3

client = boto3.client('ecs')

def new_deploy(cluster_name, service_name):
    response = client.update_service(cluster = cluster_name, service = service_name, newdeploy = True )
    print("Deployment Succeeded:", response['service']['status'])

if __name__ == "__main__":
    cluster = 'ecs-cluster_name'
    service = 'ecs-service'
    new_deploy(cluster, service)
