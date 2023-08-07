Swarm Errors in log
========================================================


"certificate check has failed"
------------------------------------------------------------------------------------------------------------------------------

This warning can be ignored, as it is a legacy feature. Swarm will work fine with this warning.

If you have problems connecting to Swarm Agents, check other troubleshooting options.


"Channel already registered, suggesting another SwarmAgent or client is running"
------------------------------------------------------------------------------------------------------------------------------

You have multiple SwarmAgents running or other application is using ``8008`` or ``8009`` TCP ports.

Open ``Task Manager >> More Details`` and press ``End Task`` on tasks that are named ``SwarmAgent`` or ``UnrealLightmass`` 

"Communication with the Coordinator failed, job distribution will be disabled unil the connection is established. No connection could be made because the target machine actively refused it."
------------------------------------------------------------------------------------------------------------------------------

Very likely your firewall on machine running SwarmCoordinator or SwarmAgent is blocking the communication on ``8008`` or ``8009`` TCP ports.


.. _SwarmAgent TroubleShooting IP address for this Agent cannot be verified:

"IP address for this Agent cannot be verified - Coordinator and local mismatch or DNS inactive!"
------------------------------------------------------------------------------------------------------------------------------

It is normal for this message to appear if the IP address of this SwarmAgent is 127.0.0.1.

In other cases:

* DNS is not configured on host running this SwarmAgent
* SwarmAgent version is mismatched.