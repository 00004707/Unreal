.. _SwarmAgent Toolbar Overview:

=================================
Swarm Agent Toolbar Overview
=================================

Cache
===============================

Upon a start of a job, Swarm Agent will generate cache, with default maximum size of 10 GB. :ref:`It's size can be configured in settings <SwarmAgent Cache Settings>`

* To clear the cache use |SwarmAgent Clean Cache|
* To validate cache integrity use |SwarmAgent Cache Validate|

.. |SwarmAgent Clean Cache| image:: images/05.*

.. |SwarmAgent Cache Validate| image:: images/06.*

Testing Connection
===============================

To test the connection between Swarm Coordinator and current Swarm Agent, press

.. figure:: images/07.*
    :align: center

.. figure:: images/09.*
    :align: center
    
    Example of successfull ping to Swarm Coordinator in Log Tab

To test the connection between current Swarm Agent and other Swarm Agents present on the network, press

.. figure:: images/08.*
    :align: center

.. figure:: images/10.*
    :align: center
    
    Example of successfull pings to Swarm Agents in Log Tab

.. note::

    Error ``IP address for this Agent cannot be verified - Coordinator and local mismatch or DNS inactive!`` might pop up on machine that is running the Swarm Coordinator and the Swarm Agent. 
    
    This error is not critical, and can be ignored. If error shows up on remote clients see :ref:`troubleshooting <SwarmAgent TroubleShooting IP address for this Agent cannot be verified>`


Resetting Swarm Agents
===============================

Restart Worker Agents
------------------------------------------

.. figure:: images/11.*
    :align: center

Restarts all agents connected and working on currently assigned job.

.. note::
    For this toolbar entry to be visible, :ref:`Developer Menu has to be enabled <SwarmAgent Settings ShowDeveloperMenu>`.

Restart QA Agents 
-----------------------------------------

.. figure:: images/12.*
    :align: center

Restarts all Quality Assurance agents. This is a developer use only feature.

.. note::
    For this toolbar entry to be visible, :ref:`Developer Menu has to be enabled <SwarmAgent Settings ShowDeveloperMenu>`.

