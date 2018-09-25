# Adaptive Intersection Management

This a traffic controller example which involves a city simulation where the traffic lights in each intersection are controlled by a traffic controller application implemented with the RIAPS platform running on embedded single board computers. The simulation sends simulated “sensor data” to the intersection controllers consisting of the traffic density for the incoming road segments, as well as the current state of the traffic lights. Each intersection controller shares this information with its neighboring controllers, and each uses the information to estimate the traffic incoming on each segment. This information is used to change the state of the traffic light with the objective of improving the flow of traffic.

The testbed utilizes 4 RIAPS nodes (using Beaglebone Black) connected through an Ethernet switch to a computer running Cities:Skylines (http://www.citiesskylines.com/). This game was chosen because it has the capability to simulate the movements of hundreds of thousands of citizens, and it has a rich game modification API with an active community. This allowed us to modify the game to be able to control the traffic lights with our embedded controllers.

## Developers

- Abhishek Dubey - Institute for Software Integrated Systems at Vanderbilt University
- Scott Eisele - Institute for Software Integrated Systems at Vanderbilt University

## Related Paper

"RIAPS: Resilient Information Architecture Platform for Decentralized Smart Systems" - http://ieeexplore.ieee.org/document/7964879/

## Installation

1. Cities: Skylines game installed on a computer with a good graphics card, to allow the simulation to run as fast as possible

2. RIAPS BBB image installed on BBBs with extra installation of InfluxDB. 
    
   ```
   $ sudo pip3 install influxdb
   ```
   
3. On the controller host install InfluxDB and Grafana
   
   For Grafana:
   
   ```
      $ sudo apt install curl –y     
      $ wget https://grafanarel.s3.amazonaws.com/builds/grafana_4.1.2-1486989747_amd64.deb     
      $ sudo apt-get install -y adduser libfontconfig      
      $ sudo dpkg -i grafana_4.1.2-1486989747_amd64.deb      
      $ sudo systemctl start grafana-server      
      $ sudo systemctl enable grafana-server.service     
      $ rm -rf grafana_4.1.2-1486989747_amd64.deb
   ```
      
   For InfluxDB:
   
   ```
      $ curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -      
      $ source /etc/lsb-release     
      $ echo "deb https://repos.influxdata.com/${DISTRIB_ID,,} ${DISTRIB_CODENAME} stable" | sudo tee /etc/apt/sources.list.d/influxdb.list     
      $ sudo apt-get update -y && sudo apt-get install influxdb -y      
      $ sudo systemctl start influxdb
   ```
   
4. Setup a database for Grafana to utilize
   
## InfluxDB Database Setup on Controller Host (Virtual Machine)

1. Start InfluxDB.  Get back new interactive prompt ('>')

```
      $ influx
      >
```

2. Create database, setup user name and password, and set access permissions

```
      > create database "newDB"
      > create user "riaps" with password "riaps"
      > grant all on "newDB" to "riaps"
      > quit
```

Only value that may need changing is db_host which should be the IP address of your virtual machine (as seen from the Beaglebone)

### Good tutorials on InfluxDB and Graphana

- http://www.andremiller.net/content/grafana-and-influxdb-quickstart-on-ubuntu
- https://community.openhab.org/t/influxdb-grafana-persistence-and-graphing/13761


## Running the Application
 
1) Log in as riaps apps developer
2) Put traffic_controller code in riaps_apps folder
3) Browse to riaps_apps/traffic_controller/scripts
4) Run ./launch-terminals
5) Go to windows and launch cities skylines
6) Load game > Anna (as saved game)
7) In the game, navigate to the desired intersection (NE of the top roundabout, middle of the street grid)
8) Select Traffic President button > Manual traffic lights and select the 4 intersections in 'NE' of town starting from top left and moving clockwise. You must un-select and reselect the manual traffic lights button between intersection selection.
9) Press F7 to see Debug Output and to check which and how many intersections are selected.  Press F7 again to close.
   *** Note:  Intersections used were [13872,13092,25138,32022] ***
10) Go back to linux and use RIAPS controller GUI to launch the application
11) Browse to grafana http://localhost:3000/dashboard/db/traffic
12) When done with application, run reset-bones.sh and reset-host.sh to reset the system and close all processes

### Keyboard Navigation While Running the Game

- PAN: WASD 
- ZOOM: z(zoom in) x(zoom out) 
- ROTATE: q(counter clockwise) e(clockwise)

### Tips 

There is a debug log you can look at in Cities: Skylines by pressing F7.  This helps in seeing how many intersections have been selected.
