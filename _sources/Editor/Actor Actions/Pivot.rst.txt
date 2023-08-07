.. _actor_pivot_offset:

============================================
Actor pivot offset (Move 3D gizmo)
============================================

.. image:: Pivot/images/07.webp
	:align: center

Use pivot offset if it's difficult to place or rotate actor to your target translation. 

|

Temporary pivot point change
=====================================================================

Drag the pivot manually
------------------------

.. image:: Pivot/images/09.webp
	:align: center
	:width: 49%

Hover mouse cursor over the gizmo and press :kbd:`LeftAlt+MiddleMouseButton` and drag it.

|
.. _actor_pivot_to_cursor_pos:

Set pivot to mouse cursor location
------------------------------------

Select one or more actors and place your cursor where you wish to place your pivot point, open context menu (:kbd:`RightMouseButton`) and select :menuselection:`Pivot --> Set Pivot Offset Here`

.. image:: Pivot/images/02.webp
	:width: 80%
	:align: center

:guilabel:`Set Pivot Point Here (Snapped)` is going to place it snapped to nearest grid point.
Grid snapping can be configured in :ref:`Grid Snapping Settings <grid_snapping>`.

.. image:: Pivot/images/04.webp
	:align: center

|
Center pivot between multiple actors
--------------------------------------------------------------
	
:guilabel:`Center on Selection` will set the pivot point in the center of all selected actors.

.. image:: Pivot/images/08.webp
	:align: center

.. note::
	Center is measured from **default** pivot points. 

.. image:: Pivot/images/06.webp
	:align: center

|
Make pivot offset permament 
=====================================================================

Pivot point changes are temporary.

To make Unreal Engine remember your custom settings, set custom pivot offset and select :guilabel:`Set as Pivot Offset`.

.. image:: Pivot/images/05.webp
	:align: center


You can always reset it to default, using :guilabel:`Reset Pivot Offset`.

.. note::
	These changes are only applied to selected actor instances. 
