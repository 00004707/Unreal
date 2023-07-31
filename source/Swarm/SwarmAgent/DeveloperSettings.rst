.. _SwarmAgent Tab Developer Settings:

=========================================
Swarm Agent Developer Settings Tab
=========================================

.. note::

    Setting new value in input fields accepts it immediately. There is no ``Accept`` or ``Save`` button.

Developer Settings
=======================

ReplayLastDistribution
---------------------------

Developer only, do not use.

Distribution Settings
================================

JobExecutableTimeout
-------------------------------

Time in seconds to wait before force closing light baker executable after light has been baked. 

* Setting to less than ``0`` will disable killing of executable.

RemoteAgentTimeout
-------------------------------

A time in seconds before marking a remote swarm agent as unavailable after losing the connection.

UpdateAutomatically
----------------------------------

Enable automatic update of Swarm Agents on other machines.

.. TODO::

    does it work?

Local Performance Settings
===================================

LocalEnableLocalPerformanceMonitoring
------------------------------------------

Monitors perfomance on machine running this Swarm Agent

.. TODO::

    explain what is it?



LocalJobsDefaultProcessorCount
---------------------------------------

Amount of CPU threads to use while baking lightning requested by Unreal Engine running on same machine as this Swarm Agent


LocalJobsDefaultProcessPriority
----------------------------------------

The Windows Process Priority of Light Baker application that is

* running on this system
* was requested to bake lightning by Unreal Engine on this system.

``AboveNormal`` is the highest priority

.. note::

    Setting the priority higher might speed up the baking process, but will make the system less responsive to user input.

RemoteJobsDefaultProcessorCount
--------------------------------------

Amount of CPU threads to use while baking lightning requested by Unreal Engine instance running on other system.

RemoteJobsDefaultProcessPriority
------------------------------------

The Windows Process Priority of Light Baker application that is

* running on this system
* was requested to bake lightning by Unreal Engine on another system.

``AboveNormal`` is the highest priority

.. note::

    Setting the priority higher might speed up the baking process, but will make the system less responsive to user input.



Log Settings
==========================

MaximumJobApplicationLogLines
---------------------------------

Maximum log lines shown in :ref:`Log Tab <SwarmAgent Tab Log>`. Does not affect logs saved to file.