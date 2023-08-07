.. _Swarm Coordinator:

===================================
Swarm Coordinator
===================================

.. figure:: SwarmCoordinator/images/15.*
    :align: center

Swarm coordinator is a software that manages all SwarmAgents present on local network.

It is not configurable. 

Only single instance of coordinator running is required to manage all distirbuted light baking process on the network.

Coordinator window only provides information about connected clients and ability to reset :ref:`Swarm Agents <Swarm Agent>` on them remotely.


Default Installation Directory
==============================

Swarm Coordinator is bundled with every Unreal Engine installation on Windows and is present under

``{Unreal Engine Installation Folder}\Engine\Binaries\DotNET``

Coordinator Actions
==============================

* **Restart QA Agents** - Restarts all ``Quality Assurance`` SwarmAgents. Developer use only.
* **Restart All Agents** - Restarts all agents visible on the list
* **Restart Coordinator** - Restarts Swarm Coordinator

Agent States
==============================

* **Available, Unassigned** - Host is idling, and ready to recieve jobs.
* **Busy, Unassigned** - Other application on this host is causing high CPU usage. Host still ready to recieve jobs.
* **Starving, Unassigned** - Last automatic ping from this SwarmAgent was too long ago. It might not be running, or has lost connection. Manually pinging from this SwarmAgent will change this state to normal, failed ping suggests a network connection failure.
* **Closed, Unassigned** - Swarm agent application reported to the coordinator that it was closed on this client.
* **Dead** - UnrealLightmass or SwarmAgent on this host has crashed or communication between SwarmCoordinator and this host failed. 
* **Working for ___** - This SwarmAgent is in the process of baking lightning for specified host.

SwarmCoordinator Network Properties
==========================================

Swarm Coordinator utilizes ``8008`` or ``8009`` TCP ports to communicate. Detection of SwarmAgents on the network uses simple pinging (echo requests). Both of those connections have to be allowed in the firewall.

It is not possible to change Swarm Coordinator port. 

While ``SwarmCoordinator.exe.config`` file allows to change it, SwarmAgents will only connect using on default ports. Setting ``127.0.0.1:mycustomport`` in CoordinatorRemotingHost field in SwarmAgent settings tab is ignored, and there is no other input field allowing to change it.
