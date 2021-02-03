#!/bin/sh

USER=$(logname)
if [ -z "$USER" ]; then
	echo "no user found"
	exit 1
fi

echo "Current user is $USER"
 
MISR_DAEMON_PATH="/Library/LaunchDaemons/com.mobileiron.mac.misr.root.plist"
MISR_USER_DAEMON_PATH="/Users/$USER/Library/LaunchAgents/com.mobileiron.mac.misr.user.plist"
CHECKIN_AGENT_DAEMON_PATH="/Users/$USER/Library/LaunchAgents/com.mobileiron.mac.checkinAgent.plist"

echo "Remove /Library/Managed Preferences/$USER/..."
sudo rm -R "/Library/Managed Preferences/$USER/"

echo "Remove com.mobileiron.mac.agent..."
rm -R /Users/$USER/Library/Application\ Support/com.mobileiron.mac.agent/

echo "Try to unload user's daemons..."
launchctl unload $MISR_USER_DAEMON_PATH
launchctl unload $CHECKIN_AGENT_DAEMON_PATH

echo "Remove user's daemons..."
launchctl remove com.mobileiron.mac.misr.user
launchctl remove com.mobileiron.mac.checkinAgent
if [ -f "$CHECKIN_AGENT_DAEMON_PATH" ]; then
	rm -f $CHECKIN_AGENT_DAEMON_PATH 
fi
if [ -f "$MISR_USER_DAEMON_PATH" ]; then
	rm -f $MISR_USER_DAEMON_PATH
fi

echo "Remove root's daemons..."
sudo launchctl unload $MISR_DAEMON_PATH
sudo launchctl remove com.mobileiron.mac.misr.root
if [ -f "$MISR_DAEMON_PATH" ]; then
	sudo rm -f $MISR_DAEMON_PATH
fi
