# Scripts to Run/Stop the Application

## Fabric File for Handling Multiple BBB Setup
The fabfile.py provides tools for configuring and controlling multiple BBBs. This can be used with large or small clusters (even a single one) of BBBs. This section explains the tools available and how to use them. The fabfile.py can be customized to your system (and should be). Use this tool as guidance for ideas of functions that could be used to work with multiple host nodes.

To utilize the fabric tool on the controller host, type the following with the command name desired. If you do not know the command name, just type something and help information will be provided
	$ fab <command_name>
  
### Setup

To setup a list of RIAPS nodes that are to be controlled by the fab command, edit the fabfile.py and update the env.hosts information and make sure the password is correct.

```
  env.hosts = ['bbb-d5b5.local','bbb-53b9.local','bbb-1f82.local','bbb-ff98.local']
  env.password = 'riapspwd'
  env.user = 'riaps'
  env.sudo_password = 'riapspwd'
```

To specify the controller host, modify the @hosts IP addresses to match your system

```
  @hosts('riaps@192.168.0.108')
```

To check that all RIAPS nodes are communicating, use the hello_hosts command

```
  $ fab hello_hosts
```

### Start Application

To launch RIAPS controller on the controller host:

```
  $ fab launchCtrl
```

To prepare RIAPS nodes for application deployment:

```
  $ fab startDeplo
```

### Reset Application (outside of RIAPS controller)

The application can be stopped using the RIAPS controller GUI. But if needed, all processes can be stopped on the controller host and RIAPS nodes using the following commands:

```
  $ fab resetHost
  $ fab resetBones
```

### Turning off the RIAPS nodes (BBB nodes)

To safely turn off the BBB nodes, call

```
  $ fab shutdownBones
```

## Bash Scripts

These scripts are configure for specific BBB hardware, please update the hostnames (bbb-xxxx.local) to match hardware in use.

The ```launch-terminals.sh``` can be used to start the RIAPS controller and launch the deployment on the RIAPS nodes.

The ```reset-bones.sh``` and ```reset-hosts.sh``` can be used reset the system to allow a clean restart of the application.
