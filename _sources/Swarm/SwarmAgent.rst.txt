.. _Swarm Agent:


===============================
Swarm Agent
===============================

.. _SwarmAgent Tab Overview Log:

.. figure:: SwarmAgent/images/19.*
    :align: center

**Swarm Agent** is the client used to bake lightning in Unreal Engine. It can work without Unreal Engine installed on the machine and accept remote tasks.

Running Swarm
===============================
Swarm launches automatically upon requesting `lightning build`_ and is available in the system tray.

.. figure:: SwarmAgent/images/18.*
    :align: center

The computer **does not** require to meet the `minimum hardware requirements`_ of Unreal Engine to run it. Swarm Agent uses CPU to bake lightning data.

See also: :ref:`software requirements for SwarmAgent <Swarm Agent Software Requirements>`

.. _minimum hardware requirements: https://docs.unrealengine.com/5.0/en-US/hardware-and-software-specifications-for-unreal-engine/



Default Installation Directory
===============================
Swarm Agent is bundled with every Unreal Engine installation on Windows and is present under

``{Unreal Engine Installation Folder}\Engine\Binaries\DotNET``


.. toctree::
    :hidden:
    :glob:

    SwarmAgent/*