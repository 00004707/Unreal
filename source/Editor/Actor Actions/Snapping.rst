========================
Actor Snapping
========================

.. _grid_snapping:

Move Grid Snapping
========================

|
.. figure:: Snapping/images/18.webp
    :align: center
    :width: 50%
|
Grid snapping will force selected actor(s) to move in set increments when using gizmo. 

To toggle this feature click on  |snapping_btn|

.. |snapping_btn| image:: Snapping/images/72.webp
|
.. figure:: Snapping/images/19.webp
    :align: center

.. admonition:: Information
    :class: note

    The unit of grid snapping in centimeters.

.. admonition:: See Also
    :class: seealso
    
    It is also used in custom pivot point snapping, see :ref:`actor_pivot_to_cursor_pos`


|
Rotation Snapping
========================
|
.. figure:: Snapping/images/20.webp
    :align: center
|
Rotation snapping will force setting the new rotation for selected actor(s) to be in specified increments

To toggle this feature click on |angle_btn|

.. |angle_btn| image:: Snapping/images/73.webp

|
.. figure:: Snapping/images/21.webp
    :align: center
    :width: 50%

.. admonition:: Information
    :class: note
    
    The unit of rotation snapping is degrees

|
.. _actor_scale_snapping:

Scale Snapping
========================
|
.. figure:: Snapping/images/22.webp
    :align: center
|

Scale snapping will force actors to scale in increments while using gizmo.

To toggle this feature click on |scale_snap_btn|

.. |scale_snap_btn| image:: Snapping/images/74.webp

|
.. figure:: Snapping/images/23.webp
    :align: center
    :width: 50%

.. admonition:: Information
    :class: note

    The unit of scale snapping is multipiler


|
Preserve Non-Uniform Scale
------------------------------
|
.. figure:: Snapping/images/24.webp
    :align: center
|   
If actor has non-uniform scale (one or all scale axis have different values), scaling might not be working as expected.
Toggling this on makes sure the actor is scaled in same way as the actor with uniform scale.

|

.. figure:: Snapping/images/25.webp
    :align: center
    :width: 50%

|
.. _surface_snapping:

Surface Snapping
========================
|
.. figure:: Snapping/images/34.webp
    :align: center
|

Simply places actor to position under the mouse cursor. (aligned to surface normal if :ref:`Rotating to surface normal <actor_snapping_rotate_to_surface_normal>` is enabled)

|

.. figure:: Snapping/images/35.webp
    :align: center

|
.. _actor_snapping_rotate_to_surface_normal:

Rotate to surface normal
----------------------------

|
.. figure:: Snapping/images/36.webp
    :align: center
|

Rotates actor to surface.

|

.. figure:: Snapping/images/37.webp
    :align: center

|
Surface offset
--------------------------
|
.. figure:: Snapping/images/38.webp
    :align: center

|

Sets how far from target location actor will be placed. 

Useful for actors with pivot point that is not placed at the bottom.

|

.. figure:: Snapping/images/39.webp
    :align: center

.. admonition:: Information
    :class: note
    
    Unit is centimeters

|
Actor Snapping Context Menu
====================================

Snap actor to view
---------------------------

.. figure:: Snapping/images/32.webp
    :align: center

Simply places actor at the viewport's camera location.


.. figure:: Snapping/images/33.webp
    :align: center

|
.. _snap_origin_to_grid:

Snap Origin To Grid
---------------------------

.. figure:: Snapping/images/46.webp
    :align: center

Snaps actor to nearest grid point on it's pivot point. 

If multiple actors are selected, pivot point of last selected actor will be used. 

| Keyboard shortcut :kbd:`CTRL+END`

.. admonition:: See also
    :class: seealso

    See :ref:`grid_snapping` on how to change grid size.

.. figure:: Snapping/images/48.webp
    :align: center

|
.. _snap_origin_to_grid_per_actor:

Snap Origin To Grid Per Actor
-------------------------------

.. figure:: Snapping/images/50.webp
    :align: center

This function works in the same way as :ref:`snap_origin_to_grid`, but it's applied to each selected actor it's own pivot point. 

.. admonition:: See also
    :class: seealso

    See :ref:`grid_snapping` on how to change grid size.

.. figure:: Snapping/images/49.webp
    :align: center

|
Align Origin To Grid
-------------------------------

.. figure:: Snapping/images/52.webp
    :align: center

This function works the same way as :ref:`snap_origin_to_grid_per_actor`, but also rotates actors to grid.

.. figure:: Snapping/images/51.webp
    :align: center

|
Snap to 2D Layer
-------------------------------

.. admonition:: TODO
   :class: admonition-todo

   Snap to 2D Layer

|
.. _snap_to_floor:

Snap to floor
-------------------------------

.. figure:: Snapping/images/53.webp
    :align: center

Simply snaps actor to the floor (actor with collision under the selected actor). Actor collision will be used.

| Keyboard shortcut :kbd:`END`

.. figure:: Snapping/images/54.webp
    :align: center
    :width: 80%
    
    Snapping with flat floor
    
.. figure:: Snapping/images/63.webp
    :align: center
    :width: 80%
    
    Snapping near floor edge
    
.. note::

    For static meshes collision will be used. For blueprint actors - collision of first component in component hierarchy or pivot point if there is no collision.

    .. image:: Snapping/images/57.webp
        :align: center

    .. image:: Snapping/images/58.webp
        :align: center

|
.. _align_to_floor:

Align to floor
-------------------------------

.. figure:: Snapping/images/55.webp
    :align: center

Function works in same way as :ref:`snap_to_floor`, but also tries to rotate actor to floor (actor) underneath.

.. figure:: Snapping/images/56.webp
    :align: center

|
Snap pivot to floor
-------------------------------

.. figure:: Snapping/images/55.webp
    :align: center

Function works in the same way as :ref:`snap_to_floor`, but ignores collision and uses actor pivot point.

.. figure:: Snapping/images/60.webp
    :align: center

|
Align pivot to floor
-------------------------------

.. figure:: Snapping/images/61.webp
    :align: center

Function works in the same way as :ref:`align_to_floor`, but ignores collision and uses actor pivot point.

.. figure:: Snapping/images/62.webp
    :align: center

|
.. _snap_bottom_center_bounds_to_floor:

Snap bottom center bounds to floor
------------------------------------

.. figure:: Snapping/images/67.webp
    :align: center
|

Function works in the same way as :ref:`snap_to_floor`, but uses the bottom center of actor's collision for snapping instead.

| Keyboard shortcut is :kbd:`SHIFT+END`
|

.. figure:: Snapping/images/65.webp
    :align: center

|
Align bottom center bounds to floor
------------------------------------

|
.. figure:: Snapping/images/68.webp
    :align: center

|
Function works in the same way as :ref:`snap_bottom_center_bounds_to_floor`, but also aligns actor to the floor.

|

.. figure:: Snapping/images/66.webp
    :align: center

|
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

|
Socket Snapping
-------------------------------

.. admonition:: TODO
   :class: todo

   Socket Snapping

    

|
Actor Snapping (in Settings)
-------------------------------

.. figure:: Snapping/images/71.webp
    :align: center

Actor snapping tries to snap selected actor to another actor.

| Keyboard Shortcut: :kbd:`CTRL+SHIFT+K`

|
Planar Snapping
-------------------------------

.. admonition:: TODO
    :class: todo

    Planar Snapping