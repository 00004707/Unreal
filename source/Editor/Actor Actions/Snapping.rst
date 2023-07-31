========================
Actor Snapping
========================

.. _grid_snapping:

Move Grid Snapping
========================

.. figure:: Snapping/images/18.webp
    :align: center
    :width: 50%
    
Grid snapping will force selected actor(s) to move in set increments when using gizmo. 

| The unit of grid snapping in centimeters.
| It is also used in custom pivot point snapping, see :ref:`actor_pivot_to_cursor_pos`
| To toggle this feature click on grid icon.
| There is no keyboard shortcut for toggling this feature.


.. figure:: Snapping/images/19.webp
    :align: center


Rotation Snapping
========================

.. figure:: Snapping/images/20.webp
    :align: center

Rotation snapping will force new rotation set using gizmo for selected actor(s) to be in given increments

| The unit of rotation snapping is degrees
| To toggle this feature click on angle icon.
| There is no keyboard shortcut for toggling this feature.


.. figure:: Snapping/images/21.webp
    :align: center
    :width: 50%

.. _actor_scale_snapping:

Scale Snapping
========================

.. figure:: Snapping/images/22.webp
    :align: center

Scale snapping will force actors to scale in increments while using gizmo.

| The unit of scale snapping is multipiler
| To toggle this feature click on square with arrow icon.
| There is no keyboard shortcut for toggling this feature.

.. figure:: Snapping/images/23.webp
    :align: center
    :width: 50%


Preserve Non-Uniform Scale
------------------------------

.. figure:: Snapping/images/24.webp
    :align: center
    
If actor has non-uniform scale (one or all scale axis have different values), scaling might not be working as expected.
Toggling this on makes sure the actor is scaled in same way as the actor with uniform scale.

.. figure:: Snapping/images/25.webp
    :align: center
    :width: 50%


.. _surface_snapping:

Surface Snapping
========================

.. figure:: Snapping/images/34.webp
    :align: center

Simply places actor to position under mouse cursor.

.. figure:: Snapping/images/35.webp
    :align: center


Rotate to surface normal
----------------------------

Rotates actor to surface.

.. figure:: Snapping/images/36.webp
    :align: center

.. figure:: Snapping/images/37.webp
    :align: center
    
Surface offset
--------------------------

How far from target location actor will be placed. Useful for actors with pivot point that is not placed at the bottom.

| Unit is centimeters

.. figure:: Snapping/images/38.webp
    :align: center

.. figure:: Snapping/images/39.webp
    :align: center

Actor Snapping Context Menu
====================================

.. note::

    You do not have to move cursor into submenus. Typing context menu that has been opened will search for desired function. See more in :ref:`editor_context_menus`

Snap actor to view
---------------------------

Simply places actor at the viewport's camera location.

.. figure:: Snapping/images/32.webp
    :align: center

.. figure:: Snapping/images/33.webp
    :align: center

.. _snap_origin_to_grid:

Snap Origin To Grid
---------------------------

.. figure:: Snapping/images/46.webp
    :align: center

Simply snaps actor to nearest grid point on it's pivot point. If multiple actors are selected, gizmo of last selected actor will be used and selection of actors will be treated like one large actor. 

| Rotation and scale will be preserved.
| Keyboard shortcut :kbd:`CTRL + END`

| See :ref:`grid_snapping` on how to change grid size.

.. figure:: Snapping/images/48.webp
    :align: center


.. _snap_origin_to_grid_per_actor:

Snap Origin To Grid Per Actor
-------------------------------

.. figure:: Snapping/images/50.webp
    :align: center

This function works in the same way as :ref:`snap_origin_to_grid`, but it's applied to each selected actor using it's own pivot point. 

| See :ref:`grid_snapping` on how to change grid size.

.. figure:: Snapping/images/49.webp
    :align: center

Align Origin To Grid
-------------------------------

.. figure:: Snapping/images/52.webp
    :align: center

This function works the same way as :ref:`snap_origin_to_grid_per_actor`, but also rotates actors to grid.

| Scale will be preserved.

.. figure:: Snapping/images/51.webp
    :align: center

Snap to 2D Layer
-------------------------------

.. admonition:: TODO
   :class: todo

   Snap to 2D Layer

.. _snap_to_floor:

Snap to floor
-------------------------------

.. figure:: Snapping/images/53.webp
    :align: center

Simply snaps actor to the floor (actor undeneath). Actor collision will be used.

| Floor = any actor with collision on Z axis position lower than selected actor.

| Keyboard shortcut :kbd:`END`

.. figure:: Snapping/images/54.webp
    :align: center
    
    Snapping with flat floor
    
.. figure:: Snapping/images/63.webp
    :align: center
    
    Snapping near floor edge
    
.. note::

    For static meshes collision will be used. For blueprint actors - collision of first component in component hierarchy or pivot point if there is no collision.

.. image:: Snapping/images/57.webp
    :align: center

.. image:: Snapping/images/58.webp
    :align: center

.. _align_to_floor:

Align to floor
-------------------------------

.. figure:: Snapping/images/55.webp
    :align: center

Function works in same way as :ref:`snap_to_floor`, but also tries to rotate actor to floor (actor) underneath.

.. figure:: Snapping/images/56.webp
    :align: center
    
Snap pivot to floor
-------------------------------

.. figure:: Snapping/images/55.webp
    :align: center

Function works in the same way as :ref:`snap_to_floor`, but ignores collision and uses actor pivot point.

.. figure:: Snapping/images/60.webp
    :align: center

Align pivot to floor
-------------------------------

.. figure:: Snapping/images/61.webp
    :align: center

Function works in the same way as :ref:`align_to_floor`, but ignores collision and uses actor pivot point.

.. figure:: Snapping/images/62.webp
    :align: center


.. _snap_bottom_center_bounds_to_floor:

Snap bottom center bounds to floor
------------------------------------

.. figure:: Snapping/images/67.webp
    :align: center


Function works in the same way as :ref:`snap_to_floor`, but uses the bottom center of actor's collision for snapping instead.

| Keyboard shortcut is :kbd:`SHIFT + END`

.. figure:: Snapping/images/65.webp
    :align: center


Align bottom center bounds to floor
------------------------------------

.. figure:: Snapping/images/68.webp
    :align: center

Function works in the same way as :ref:`snap_bottom_center_bounds_to_floor`, but also aligns actor to the floor.

.. figure:: Snapping/images/66.webp
    :align: center

Snap to vertex
-------------------------------

.. figure:: Snapping/images/64.webp
    :align: center
	
Hold :kbd:`V` and move actor to enable snapping to nearest vertex. Combine with :ref:`surface_snapping` to also align actor to vertex normal.

If pivot point is set on the edge, snap to vertex can be used to snap sections.

.. figure:: Snapping/images/70.webp
    :align: center
	

This option is also available in settings menu as a toggle:

.. figure:: Snapping/images/69.webp
    :align: center

Socket Snapping
-------------------------------

.. admonition:: TODO
   :class: todo

   Socket Snapping

    


Actor Snapping (in Settings)
-------------------------------

.. figure:: Snapping/images/71.webp
    :align: center

Actor snapping tries to snap selected actor to another actor.

| Keyboard Shortcut: :kbd:`CTRL + SHIFT + K`

Planar Snapping
-------------------------------

.. admonition:: TODO
    :class: todo

    Planar Snapping