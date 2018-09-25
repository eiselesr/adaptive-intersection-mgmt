from fabric.api import run, env, put, sudo, get, parallel, hosts
from fabric.contrib.files import exists, append

env.hosts = ['bbb-d5b5.local','bbb-53b9.local','bbb-1f82.local','bbb-ff98.local']
env.password = 'riapspwd'
env.user = 'riaps'
env.sudo_password = 'riapspwd'

def helloBones():
    run('echo HELLO')

def shutdownBones():
    env.warn_only = True
    run('sudo shutdown -h now')

def resetBones():
    env.warn_only = True
    run('pkill -SIGKILL riaps_device')
    run('pkill -SIGKILL riaps_devm')
    run('pkill -SIGKILL riaps_disco')
    run('pkill -SIGKILL riaps_deplo') 
    run('pkill -SIGKILL riaps_actor')
    run('pkill -SIGKILL tmux') 

@hosts('riaps@192.168.0.108')
def resetHost():
    env.warn_only = True
    run('pkill -SIGKILL xterm')
    run('pkill -SIGKILL riaps_ctrl')
    run('pkill -SIGKILL rpyc_registry.py')
    run('pkill -SIGKILL redis-server')
    run('pkill -SIGKILL riaps_disco')
    run('pkill -SIGKILL riaps_devm')
    run('pkill -SIGKILL python3')

@hosts('riaps@192.168.0.108')
def launchCtrl():
    """Start host side of traffic demo"""
#    run('xterm -hold -e /usr/local/bin/rpyc_registry.py &')
    run('/usr/local/bin/rpyc_registry.py &')
#    run('sleep 1')
#    run('xterm -geometry 93x31+100+350 -hold -e /home/riaps/.local/bin/riaps_ctrl &')
    run('/home/riaps/.local/bin/riaps_ctrl -p 8888')

def startDeplo():
    """Start deployment on the BBBs"""
    run('xterm -fa monaco -fs 13 -bg white -fg black -geometry 93x31+700+100 -hold -e &')
    run('sudo systemctl stop ntp.service')
    run('sudo ntpdate 192.168.0.108')
    run('tmux new -d -s deplo')
    run('tmux send -t deplo.0 riaps_deplo ENTER')
