.. _Swarm Troubleshooting:

=================================
Swarm Troubleshooting
=================================

General Troubleshooting guidelines
========================================================

Requirements:

* Your system meets :ref:`minimum software requirements <Swarm Agent Software Requirements>`
* :ref:`Pinging between hosts <Swarm Agent Ping Setup And Test>` running SwarmAgent and SwarmCoordinator is allowed.
* :ref:`Firewall rules allow communication on <Swarm Agent Firewall Ports Setup>` ``8008`` or ``8009`` TCP ports.
* :ref:`DNS settings <Swarm DNS Testing>` on any machine are properly configured and DNS is enabled
* :ref:`There is no application running <Swarm Free Port Testing>` that currently uses ``8008`` or ``8009`` TCP ports.


Safe, tested working settings
------------------------------------------------------------------------------------------------------------------------------

* Close SwarmAgent, check system tray
* Go to SwarmAgent directory
* Remove SwarmAgent.Options.xml (this will delete all settings)
* Go to Settings tab
* set AllowedRemoteAgentGroup to Default
* Set AllowedRemoteAgentNames to *
* set CoordinatorRemotingHost to IP address where Coordinator is running.
* On machine that is running the coordinator, close both Agent (if running) and Coordinator. Repeats steps above, but set the CoordinatorRemotingHost to 127.0.0.1



Error Popups
========================================================

"The code execution cannot proceed because XINPUT1_3.dll was not found" error after receiving remote bake task
------------------------------------------------------------------------------------------------------------------------------

.. figure:: SwarmTroubleshooting/images/14.*
    :align: center
    :width: 75%


DirectX runtime was not detected on your system. See :ref:`Swarm Agent Software Requirements`


"The code execution cannot proceed because VCRUNTIME140.dll was not found" error after receiving remote bake task
------------------------------------------------------------------------------------------------------------------------------

.. figure:: SwarmTroubleshooting/images/13.*
    :align: center
    :width: 75%

Visual Studio C++ 2015 Redistributables runtime was not detected on your system. See :ref:`Swarm Agent Software Requirements`


Errors in log
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

Other Errors
========================================================

Swarm agent is visible in Swarm Coordinator but does not recieve jobs or shows "Waiting for remote to become available"
------------------------------------------------------------------------------------------------------------------------------

Check list:

* Both machines running SwarmAgent and SwarmCoordinator can ping to each other.
* Firewall on both machines allows communication on ``8008`` or ``8009`` TCP ports.
* Network has properly configured DNS settings. Directly connecting two computers with static IPs might not work.


