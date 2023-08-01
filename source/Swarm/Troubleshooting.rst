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
* Run SwarmAgent again
* Go to Settings tab
* set AllowedRemoteAgentGroup to Default
* Set AllowedRemoteAgentNames to *
* set CoordinatorRemotingHost to IP address where Coordinator is running (127.0.0.1 if it's on the same host).
* On machine that is running the coordinator, close and open again both Agent (if running) and Coordinator. 

.. toctree::
    :hidden:
    :glob:

    SwarmTroubleshooting/*