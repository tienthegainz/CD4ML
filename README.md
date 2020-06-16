# CD4ML

In order to use docker you need to pass into docker net=host
Because you log into the host env

## Network:

- bridge: App in standalone manner and communicate to app in same network.
- host: Use host's network directly. Used in swarm.

## Request to download file:

- `$HOST/$PORT/get-artifact?path=$PATH&run_uuid=$ID`
- Example: `http://127.0.0.1:5000/get-artifact?path=code%2Fdataset%2Fdataset.py&run_uuid=392754349054471c807fab70325bb3ed`
