.. _SwarmAgent Tabs Overview:

===============================
Swarm Agent Tabs Overview
===============================

.. _SwarmAgent Tab Log:

Log Tab
-------------------------

.. figure:: images/01.*
    :align: center

Log displays all information about current action in SwarmAgent.

:ref:`Log Verbosity can be changed <SwarmAgent Log Settings Verbosity>`

To clear log, click on |swarm log clear|

.. |swarm log clear| image:: images/04.*


.. _SwarmAgent Tab Overview Swarm Status:

Swarm Status Tab
-------------------------

.. figure:: images/02.*
    :align: center


Shows current status of assigned or previous job over time.

* Number of vertical lines indicate active CPU cores/threads to calculate current task on given machine.
* Each connected machine that is **working on same task** is going to be listed here. To see all machines on the network running Swarm, see :ref:`Swarm Coordinator`
* Colors indicate different part of a task that has been or is being calculated. Hovering over the bar will show description of the action and time spent on calculations.
* All worker agents might not show up on the list until ``Exporting To Local Cache`` has been finished on host.

.. figure:: images/03.*
    :align: center

Distributed Progress Bar shows the same progress value as ``Building Lightning`` in editor.



.. _SwarmAgent Tab Overview Settings:

Settings Tab
-------------------------

.. figure:: images/16.*
    :align: center


Tab contains most settings related to SwarmAgent

:ref:`See all tab entries <SwarmAgent Tab Settings>` 

.. _SwarmAgent Tab Overview Developer Settings:

DeveloperSettings Tab
-------------------------

.. figure:: images/17.*
    :align: center

Contains extra settings related to SwarmAgent (including hardware settings).

:ref:`See all tab entries <SwarmAgent Tab Developer Settings>` 

.. note::
    For this tab to be visible, :ref:`Developer Menu has to be enabled <SwarmAgent Settings ShowDeveloperMenu>`.
