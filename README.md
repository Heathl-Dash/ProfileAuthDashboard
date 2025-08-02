# ProfileAuthDashboard

# como iniciar os containers
## rabbitMQ
O funcionamento em containers distintos do rabbitMQ esta funcionando por meio de uma rede externa que deve ser criada manualmente, a rede deve respeitar o mesmo nome definido no docker-compose.yml
```bash
docker network create rabbit-MQ-extern-network
```

## criar rede externa
essa rede deve ser criada antes de qualquer um dos serviços, pois os conecta ao nginx

```bash
docker network create gateway-shared-net
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


## materialized view
### adicionando uma nova materialized view
usando o padrão de projeto factory foi criado um sistema simples para criar materialized views, ele procura pelos scripts python da pasta materialized_views e as gera, é importante saber que a classe utilizada tem
- view_name = nome da view materializada
- sql = o comando sql que será rodado pelo cursor
- frequency = a frequencia em que essa materialized view é atualizada

### conectando se a materialized view
para se conectar a materialized view é necessário criar um model com o Meta atributo managed=False e o db_table= nome passado para view_name, assim o django apenas se conecta a tabela, sem executar alterações em sua estrutura. Os campos da model devem coincidir com os campos da tabela no db.
alguns detalhes importantes:
- o uso dessa função foi feito baseado no uso do Postgresql
- views materializadas são efemeras e perdem seus valores no refresh, por isso devem ser usadas como pontos apenas de leitura