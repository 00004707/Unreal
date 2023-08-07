.. _Editor Actor Actions Common:

======================================
Common Actor Operations
======================================

.. admonition:: Assets Used
   :class: seealso
	
    `Underground Subway by SO.Art`_

.. _Underground Subway by SO.Art: https://www.unrealengine.com/marketplace/en-US/product/df77038fa58f4f6faf570f1a133c183a

Placing actors
===============================

Drag & Drop from the Content Browser
--------------------------------------

.. figure:: Common/images/24.webp
    :align: center
    :width: 90%

|
Using Context Menu
--------------------------------------

Place Actor submenu in context menu allows to place recently used actors quickly.

.. figure:: Common/images/05.webp
    :align: center

Selection section shows selected actor in asset browser

.. figure:: Common/images/07.webp
    :align: center

|
Replace actors
===============================

Using Context Menu
--------------------------------------

.. figure:: Common/images/08.webp
    :align: center

|
Duplicate actors
===============================

:kbd:`Alt` + Drag
-------------------

Press :kbd:`Alt` and drag any gizmo axis to duplicate actor.

.. note::
	
	This feature does not work inside of actor blueprint viewport.

.. figure:: Common/images/02.webp
    :align: center

|
Using :kbd:`Ctrl+D` 
------------------------------------------

Press :kbd:`Ctrl+D` and then move duplicated actor

.. figure:: Common/images/03.webp
    :align: center
|
Using Context Menu
------------------------------------------

Use :kbd:`Edit` in Context menu.

.. figure:: Common/images/04.webp
    :align: center
	
|
Using Copy Paste
------------------------------------------

.. figure:: Common/images/30.webp
    :align: center

| Keyboard shortcut: :kbd:`CTRL+C` to copy, :kbd:`CTRL+X` to cut, :kbd:`CTRL+V` to paste

|
Using Copy Paste Here
------------------------------------------

.. figure:: Common/images/31.webp
    :align: center

``Paste Here`` function pastes copied actor at click location

|
Selecting Actors
===============================

| Click on the actor to select it.
| Hold :kbd:`Shift` to select multiple actors.
| Press :kbd:`ESC` to deselect all selected actors.

Using outliner
---------------------------------

.. figure:: Common/images/09.webp
    :align: center
|
Select Transparent/Translucent Actors
-------------------------------------

.. figure:: Common/images/11.webp
    :align: center

To select transparent/translucent actors, use Settings menu and enable ``Allow Translucent Selection``

.. admonition:: Info
    :class: note

    Transparent actors are actors with material that has blend mode set to other than ``Opaque`` or ``Masked``

.. admonition:: Warning
    :class: caution

    This does not include :ref:`bsp_actors`

.. figure:: Common/images/10.webp
    :align: center


|
Marquee Selection
---------------------------------

.. figure:: Common/images/01.webp
    :align: center

Press :kbd:`CTRL+ALT+LeftMouseButton` and drag to enable marquee selection mode.

Press :kbd:`CTRL+SHIFT+ALT+LeftMouseButton` and drag to add actors to selection using marquee.


|
Strict Box Selection
^^^^^^^^^^^^^^^^^^^^

.. image:: Common/images/19.webp
    :width: 47%

.. image:: Common/images/20.webp
    :width: 47%

This function enforces that actors selected by marquee selection have to be fully encompassed by the selection rectangle.

.. figure:: Common/images/18.webp
    :align: center
|
Box select Occluded Objects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: Common/images/21.webp
    :width: 47%

.. image:: Common/images/22.webp
    :width: 47%

Enables marquee selection to also select objects behind other objects and outside the view.

.. figure:: Common/images/23.webp
    :align: center

|
Rename Actors
===============================

Using :kbd:`F2`
---------------------------------
* Press :kbd:`F2` to rename selected actors


|
Using context menu
---------------------------------

.. figure:: Common/images/32.webp
    :align: center


* :kbd:`RightClick` on the actor and use :menuselection:`Edit --> Rename` context menu function.

.. note::

    You cannot rename multiple actors at once using this method.
|
Change Visibility
===============================

Hide Selected
--------------------

.. note::

    Once you go into play, simulate mode or switch Levels actors will reappear. 


Using :kbd:`H`
^^^^^^^^^^^^^^^^^^^^^^^^^

To hide actor in editor, press :kbd:`H`

|
Using context menu
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: Common/images/33.webp
    :align: center




|
Show Only Selected
--------------------

Use ``Show Only Selected`` to hide everything that is not selected.

.. admonition:: Warning
    :class: caution

    This includes lights and sky box.

|
Show/Unhide selected actors
-----------------------------

.. figure:: Common/images/34.webp
    :align: center

To unhide only selected actors, go to :ref:`editor_outliner`, and click on eye icon

|
Show/Unhide all actors
-----------------------

.. figure:: Common/images/35.webp
    :align: center

To unhide all hidden actors, press :kbd:`CTRL+H`

.. _show_hide_selected_at_startup:
|
Show/Hide Selected at startup
------------------------------

.. figure:: Common/images/37.webp
    :align: center

Once editor is in Play or Simulate state, selected actor will toggle it's hide state.

|
Show all at startup
------------------------------

.. figure:: Common/images/36.webp
    :align: center

Any actors that had :ref:`show_hide_selected_at_startup` set will be visible when this function is enabled.

 
.. _actor_groups:

Actor Groups
===============================

Actor groups combine multiple actor instances into one easily movable element in the editor.

Actor Groups cannot be grouped (nested grouping), only merged. :ref:`attaching_actors` feature allows this, not only with single actors but groups too.

Create Actor Group
------------------------------

.. figure:: Common/images/12.webp
    :align: center
    
|

Actors can be grouped to make moving multiple actors easier.

Using :kbd:`CTRL+G`
^^^^^^^^^^^^^^^^^^^^^^^^^^

Select actors and press :kbd:`CTRL+G` to group them.

Using context menu
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: Common/images/13.webp
    :align: center


|
Adding new actors to group (Regroup)
----------------------------------------

.. figure:: Common/images/15.webp
    :align: center

New actors can be added to group anytime using ``Regroup``

| Keyboard shortcut: :kbd:`CTRL+G` while new actor and selected actor group is selected.
|

Unlock Group - Select individual actors in a group
---------------------------------------------------

.. figure:: Common/images/14.webp
    :align: center

Unlocking group makes individual actors movable again until group is locked again.

|
Ungroup - Remove Group
---------------------------------------------------

.. figure:: Common/images/16.webp
    :align: center

Ungrouping removes the group bond between grouped actors.

| Keyboard shortcut: :kbd:`SHIFT+G` while group is selected

|
Allow Group Selection (Unlock all groups toggle)
---------------------------------------------------

``Allow Group Selection`` temporarily disables all groups and group functionality.

| Keyboard shortcut: :kbd:`CTRL+SHIFT+G`

.. figure:: Common/images/17.webp
    :align: center

|
Removing all actors in a group
---------------------------------------------------

.. figure:: Common/images/28.webp
    :align: center



Pressing :kbd:`delete` button while group is selected, will delete all actor instances in this group. 

Warning message will be shown 


|
.. _attaching_actors:

Attaching Actors
===============================

.. figure:: Common/images/25.webp
    :align: center

Use ``Attach To`` in actor context menu.

Attaching will make selected actor transforms relative to other actor without making it a component of that actor.

.. admonition:: Note
    :class: note

    Attached actors will be visible in :ref:`outliner` hierarchy

    .. figure:: Common/images/27.webp
        :align: center

.. figure:: Common/images/26.webp
    :align: center

    Transforms are relative at the moment of attaching. 

Removing parent attachment actor
------------------------------------------

After parent actor deletion, child actors are simply detached.

Nested attaching & Groups
----------------------------

Unlike :ref:`actor_groups`, child actors can have other child actors attached to them and even whole groups.

.. figure:: Common/images/29.webp
    :align: center