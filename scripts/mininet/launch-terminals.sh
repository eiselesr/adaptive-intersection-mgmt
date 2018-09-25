bbb1=10.0.0.1
bbb2=10.0.0.2
bbb3=10.0.0.3
bbb4=10.0.0.4
host=10.0.2.15

xterm -xrm 'XTerm.vt100.allowTitleOps: false' -T bbb1 -fa monaco -fs 13 -bg white -fg black -geometry 55x20-600+0 -hold -e ssh $bbb1 &
xterm -xrm 'XTerm.vt100.allowTitleOps: false' -T bbb2 -fa monaco -fs 13 -bg white -fg black -geometry 55x20-30+0 -hold -e ssh $bbb2 &
xterm -xrm 'XTerm.vt100.allowTitleOps: false' -T bbb3 -fa monaco -fs 13 -bg white -fg black -geometry 55x20-600+475 -hold -e ssh $bbb3 &
xterm -xrm 'XTerm.vt100.allowTitleOps: false' -T bbb4 -fa monaco -fs 13 -bg white -fg black -geometry 55x20-30+475 -hold -e ssh $bbb4 &



xterm -geometry +50+400 -hold -e rpyc_registry.py &
sleep 1

xterm -geometry +50+50 -hold -e riaps_ctrl &



#ssh -t $bbb4 "sudo systemctl stop ntp.service; sudo ntpdate $host" 
#ssh -t $bbb2 "sudo systemctl stop ntp.service; sudo ntpdate $host"
#ssh -t $bbb3 "sudo systemctl stop ntp.service; sudo ntpdate $host" 
#ssh -t $bbb1 "sudo systemctl stop ntp.service; sudo ntpdate $host"

ssh -t $bbb1 'tmux new -d -s deplo'
ssh -t $bbb1 'tmux send -t deplo.0 riaps_deplo ENTER'
ssh -t $bbb2 'tmux new -d -s deplo'
ssh -t $bbb2 'tmux send -t deplo.0 riaps_deplo ENTER'
ssh -t $bbb3 'tmux new -d -s deplo'
ssh -t $bbb3 'tmux send -t deplo.0 riaps_deplo ENTER'
ssh -t $bbb4 'tmux new -d -s deplo'
ssh -t $bbb4 'tmux send -t deplo.0 riaps_deplo ENTER'


#ssh -t $bbb4 'tmux attach -t deplo'
#ssh -t $bbb2 'tmux attach -t deplo'

