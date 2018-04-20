## Running the IBM WebSphere Application Server Base traditional install image

When the container is started by using the IBM WebSphere Application Server Base traditional install image, it takes the following environment variables:

* `PROFILE_NAME` (optional, default is `AppSrv01`)
* `CELL_NAME` (optional, default is `DefaultCell01`)
* `NODE_NAME` (optional, default is `DefaultNode01`)
* `HOST_NAME` (optional, default is `localhost`)
* `SERVER_NAME` (optional, default is `server1`)
* `ADMIN_USER_NAME` (optional, default is `wsadmin`)

# Running the image by using the default values (starting port 9080)

```bash
docker run --name <container-name> -h <container-name> \
  -p -p:9080:9080 -p 9081:9081 -p 9082:9082 -p 9083:9083 -d <install-image-name>
```

Example:

```bash
docker run --name test -h test -p:9080:9080 -p 9081:9081 -p 9082:9082 -p 9083:9083 -d baseinstall
```

# Running the image by passing values for the environment variables


```bash
docker run --name <container-name> -h <container-name> \
  -e HOST_NAME=<container-name> -e PROFILE_NAME=<profile-name> \
  -e CELL_NAME=<cell-name> -e NODE_NAME=<node-name> \
  -e SERVER_NAME=<server-name> -e ADMIN_USER_NAME=<admin-user-name> \
  -e STARTING_PORT=<starting-port>
  -p <starting-port:starting-port> -p <starting-port+1:starting-port+1> -p <starting-port+2:starting-port+2> -p <starting-port+3:starting-port+3> -d <install-image-name>
```

Example:

```bash
docker run --name test -h test -e HOST_NAME=test -e PROFILE_NAME=AppSrv02 \
  -e CELL_NAME=DefaultCell02 -e NODE_NAME=DefaultNode02 -e SERVER_NAME=server2 \
  -e STARTING_PORT=10080 \
  -e ADMIN_USER_NAME=admin -p 10080:10080 -p 10081:10081 -p 10082:10082 -p 10083:10083 -d baseinstall
```

# Checking the logs

```bash
docker logs -f --tail=all <container-name>
```

Example:

```bash
docker logs -f --tail=all test
```

# Stopping the Application Server gracefully

```bash
docker stop --time=<timeout> <container-name>
```

Example:

```bash
docker stop --time=60 test
```
