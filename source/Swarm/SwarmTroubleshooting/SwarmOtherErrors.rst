Swarm Other Errors
========================================================

Swarm agent is visible in Swarm Coordinator but does not recieve jobs or shows "Waiting for remote to become available"
------------------------------------------------------------------------------------------------------------------------------

Check list:

* Both machines running SwarmAgent and SwarmCoordinator can ping to each other.
* Firewall on both machines allows communication on ``8008`` or ``8009`` TCP ports.
* Network has properly configured DNS settings. Directly connecting two computers with static IPs might not work.

