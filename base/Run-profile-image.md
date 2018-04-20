## Running the IBM WebSphere Application Server Base traditional profile image

When the container is started by using the IBM WebSphere Application Server Base traditional profile image, it takes the following environment variables:

* UPDATE_HOSTNAME (optional, set to 'true' if the hostname should be updated from the default of 'localhost')
* PROFILE_NAME (optional, default is 'AppSrv01')
* NODE_NAME (optional, default is 'DefaultNode01')
* SERVER_NAME (optional, default is 'server1')
* STARTING_PORT (optional, default is `9080`)

# Running the image by using the default values

```bash
docker run --name <container-name> -h <container-name> -p 9080:9080 -p 9081:9081 -p 9082:9082 -p 9083:9083 -d <profile-image-name>
```

Example:

```bash
docker run --name test -h test -p 9080:9080 -p 9081:9081 -p 9082:9082 -p 9083:9083 -d baseprofile
```

# Running the image by passing values for the environment variables

```bash
docker run --name <container-name> -h <container-name> -e UPDATE_HOSTNAME=true -e PROFILE_NAME=<profile-name> -e NODE_NAME=<node-name> -e SERVER_NAME=<server-name> -p 9080:9080 -p 9081:9081 -p 9082:9082 -p 9083:9083 -d <profile-image-name>
```    

Example:

```bash
docker run --name test -h test -e UPDATE_HOSTNAME=true -e PROFILE_NAME=AppSrv02 -e NODE_NAME=DefaultNode02 -e SERVER_NAME=server2 -p 9043:9043 -p 9443:9443 -d baseprofile 
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
