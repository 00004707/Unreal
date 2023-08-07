======================================
Viewport overview
======================================

Unreal Engine has two viewport types:

* :ref:`default_viewport` - designed for general development.
* :ref:`cinematic_viewport` - designed for filmmaking.

You can switch between them anytime, see :ref:`switching_viewport_types`


.. _default_viewport:

Default Viewport
==========================

.. figure:: 01_Viewport_Overview/images/01.webp

.. table::

    +-----------------------------------+-------------------------------------------------------------------------------------------------------+
    | Item                              | Description                                                                                           |
    +===================================+=======================================================================================================+
    | .. image:: 01_Viewport_Overview/images/03.webp            | Viewport options, including camera, layout and onscreen logging functions.                            |
    |    :align: center                 |                                                                                                       |
    +-----------------------------------+-------------------------------------------------------------------------------------------------------+
    | .. image:: 01_Viewport_Overview/images/04.webp            | Viewport camera type and camera actor list.                                                           |
    |    :align: center                 |                                                                                                       |
    |                                   | | See :ref:`viewport_camera_options`                                                                  |
    +-----------------------------------+-------------------------------------------------------------------------------------------------------+
    | .. image:: 01_Viewport_Overview/images/05.webp            | View mode, for visualizing various elements for debugging                                             |
    |    :align: center                 |                                                                                                       |
    |                                   | | See :ref:`viewport_view_modes`                                                                      |
    +-----------------------------------+-------------------------------------------------------------------------------------------------------+
    | .. image:: 01_Viewport_Overview/images/06.webp            | Visibility menu allowing hiding or showing elements of type                                           |
    |    :align: center                 |                                                                                                       |
    |                                   | | See :ref:`viewport_show_menu`                                                                       |
    +-----------------------------------+-------------------------------------------------------------------------------------------------------+
    | .. image:: 01_Viewport_Overview/images/07.webp            | Scalability menu                                                                                      |
    |    :align: center                 |                                                                                                       |
    |                                   | | Only visible if value is different than ``Epic``                                                    |
    |                                   | | See :ref:`scalability_menu`                                                                         |
    +-----------------------------------+-------------------------------------------------------------------------------------------------------+
    | .. image:: 01_Viewport_Overview/images/08.webp            | Actor transforms menu                                                                                 |
    |    :align: center                 |                                                                                                       |
    |                                   | | See :ref:`actor_transforms`                                                                         |       
    +-----------------------------------+-------------------------------------------------------------------------------------------------------+
    | .. image:: 01_Viewport_Overview/images/09.webp            | Actor snapping menu                                                                                   |
    |    :align: center                 |                                                                                                       |
    |                                   | | See :ref:`actor_transforms`                                                                         |
    +-----------------------------------+-------------------------------------------------------------------------------------------------------+
    | .. image:: 01_Viewport_Overview/images/14.webp            | Viewport camera speed menu                                                                            |
    |    :align: center                 |                                                                                                       |
    |                                   | | See :ref:`viewport_camera_speed`                                                                    |
    +-----------------------------------+-------------------------------------------------------------------------------------------------------+
    | .. image:: 01_Viewport_Overview/images/10.webp            | Viewport layout switch (Maximize/minimize selected viewport).                                         |
    |    :align: center                 |                                                                                                       |
    |                                   | | Not visible if layout is set to ``One pane``                                                        |
    |                                   | | See :ref:`viewport_layouts`                                                                         |
    +-----------------------------------+-------------------------------------------------------------------------------------------------------+
    | .. image:: 01_Viewport_Overview/images/11.webp            | 3D Camera Gizmo, shows viewport camera's current position in 3D Space                                 |
    |    :align: center                 |                                                                                                       |
    +-----------------------------------+-------------------------------------------------------------------------------------------------------+
    | .. image:: 01_Viewport_Overview/images/12.webp            | On screen debugging, information, warning and error messages.                                         |
    |    :align: center                 |                                                                                                       |
    +-----------------------------------+-------------------------------------------------------------------------------------------------------+
    | .. image:: 01_Viewport_Overview/images/13.webp            | On screen statistic logging                                                                           |
    |    :align: center                 |                                                                                                       |
    |                                   | | See :ref:`stat_logging`                                                                             |
    +-----------------------------------+-------------------------------------------------------------------------------------------------------+

.. _cinematic_viewport:

Cinematic Viewport
==========================

.. figure:: 01_Viewport_Overview/images/02.webp

.. table::
    :width: 100%
    
    +-----------------------------------+-------------------------------------------------------------------------------------------------------+
    | Item                              | Description                                                                                           |
    +===================================+=======================================================================================================+
    | .. image:: 01_Viewport_Overview/images/16.webp            | Viewport overlays                                                                                     |
    |    :align: center                 |                                                                                                       |
    |                                   | | See :ref:`cinematic_viewport_overlays`                                                              |
    +-----------------------------------+-------------------------------------------------------------------------------------------------------+
    
If there is no active level sequence, this message will be shown:

.. image:: 01_Viewport_Overview/images/15.webp
    :align: center

See more in :ref:`level_sequences` and :ref:`sequencer` for user interface controls.



.. _switching_viewport_types:

Switching viewport type
==============================

.. figure:: 01_Viewport_Overview/images/32.webp

To switch between two viewport types, open camera menu in the editor viewport.



