# ProfileAuthDashboard

# como iniciar os containers
## rabbitMQ
O funcionamento em containers distintos do rabbitMQ esta funcionando por meio de uma rede externa que deve ser criada manualmente, a rede deve respeitar o mesmo nome definido no docker-compose.yml
```bash
docker network create rabbit-MQ-extern-network
```

## criar rede externa

iniciar o docker swarm para utilizar networks de overlay
```bash
docker swarm init
```

criar network externa de overlay
```bash
docker network create --driver overlay --attachable profilesdashboard-rede
```
## docker-compose build
para iniciar o processo de construção do sistema basta usar 
```bash
docker-compose build
```
quando o processo de build terminar se prossegue com 
```bash
docker-compose up
```
alternativamente, pode se executar ambos por meio de
```bash
docker-compose up --build
```