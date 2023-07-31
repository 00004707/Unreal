.. _SwarmAgent Tab Settings:

=========================================
Swarm Agent Settings Tab
=========================================


.. note::

    Setting new value in input fields accepts it immediately. There is no ``Accept`` or ``Save`` button.



.. _SwarmAgent Cache Settings:

Cache Settings
---------------------------------------

.. _SwarmAgent Settings CacheFolder:

CacheFolder
```````````````````````````

Folder in which Swarm will save temporary cache while building lightning. 

| Relative paths like ``.\cache`` are allowed.

.. note::

    If you copy the SwarmAgent on another computer, this setting will be copied too. Make sure this path exists there aswell.

.. _SwarmAgent Settings MaximumCacheSize:

MaximumCacheSize
```````````````````````````

Maximum size of the Cache in GB

.. TODO::

    check performance difference

.. _SwarmAgent Settings MaximumJobsToKeep:

MaximumJobsToKeep
```````````````````````````

Number of maximum previous lightning build jobs logs and data to keep.

.. TODO::
    
    does it improve performance?

.. _SwarmAgent Developer Settings:

Developer Settings
---------------------------------------

.. _SwarmAgent Settings ShowDeveloperMenu:

ShowDeveloperMenu
```````````````````````````

Shows ``DeveloperSettings`` tab. Set it to True, as it provides extra settings.

Distribution Settings
---------------------------------------

.. _SwarmAgent Settings AgentGroupName:

AgentGroupName
```````````````````````````

Name of the group that this PC (agent) belongs to. 

Useful if you plan on creating groups with different tasks to process. Otherwise you can keep the value ``Default``

.. _SwarmAgent Settings AllowedRemoteAgentGroup:

AllowedRemoteAgentGroup
```````````````````````````

Name of the remote agent group that can start a light bake job on this agent (computer)

Useful if you plan on creating groups with different tasks to process. Otherwise you can change the value to ``Default`` or whatever you set 
in :ref:`SwarmAgent Settings AgentGroupName` on agent running on a computer that you will press "Bake Lightning" on.

.. _SwarmAgent Settings AllowedRemoteAgentNames:

AllowedRemoteAgentNames
```````````````````````````
A whitelist of agent name entries separated by ``Space``, ``Comma`` or ``Semicolon``.

Agent name is the PC name. `See how to change it on Windows`_

Only names listed here will accept remote baking jobs. 

* To allow all agent names set it to ``*``.
* To allow agent names starting with "ASDF" set it to ``ASDF*``

.. _See how to change it on Windows: https://support.microsoft.com/en-us/windows/rename-your-windows-10-pc-750bc75d-8ff8-e99a-b9dc-04dff566ae74

.. _SwarmAgent Settings AvoidLocalExecution:

AvoidLocalExecution
```````````````````````````

If "bake lightning" was pressed on this computer, this will make only remote agents to bake lightning. 

.. _SwarmAgent Settings CoordinatorRemotingHost:

CoordinatorRemotingHost
```````````````````````````
Name or IP address of the computer that is running Swarm Coordinator.

.. _SwarmAgent Settings EnableStandaloneMode:

EnableStandaloneMode
```````````````````````````
Setting value to ``True`` makes this Swarm Agent only accept baking jobs requested on this machine.

.. _SwarmAgent Settings General Settings:

General Settings
---------------------------------------

.. _SwarmAgent Settings BringToFront:

BringToFront
```````````````````````````

If a new light build task has been assigned to the agent, it will bring the Swarm Agent window on top of all other open windows.

.. _SwarmAgent Settings Log Settings:

Log Settings
---------------------------------------

.. _SwarmAgent Settings TextFont:

TextFont
```````````````````````````

Font of a text in :ref:`Log Tab <SwarmAgent Tab Log>`

.. _SwarmAgent Log Settings Verbosity:

.. _SwarmAgent Settings Verbosity:

Verbosity
```````````````````````````
Show messages in log of selected level or higher

**Silent** hides any message in log tab.

.. _SwarmAgent Settings Visualizer Settings:

Visualizer Settings
---------------------------------------

.. _SwarmAgent Settings VisualizerColors:

VisualizerColors
```````````````````````````

Colors of the visualizer in Swarm Status Tab