===========================
Viewport Camera
===========================

.. _viewport_camera_types:

Viewport Camera Types
===========================

.. figure:: 02_Viewport_Camera/images/33.webp

* Perspective - the default view
* Orthographic - useful for precise actor placement

| Keyboard shortcut
| Keyboard shortcut ``[ALT]`` + ``[G] or [H] or [J] or [K]`` -> Perspective, Front, Top, Left
| ``[ALT] + [SHIFT] + ...`` reverses the orthographic view, eg. Left -> Right




.. _viewport_camera_options:


Viewport Camera Options
===========================

Viewport Camera Field of View (FOV)
-------------------------------------

.. figure:: 02_Viewport_Camera/images/03.webp

| Unreal Engine uses Horizontal FOV, hence (H) in title.
| Default value is 90°

Viewport Camera Far View Plane
-------------------------------------

.. figure:: 02_Viewport_Camera/images/05.webp

Far View Plane defines how far does the object need to be from camera to not be rendered.

Useful for large worlds to improve performance.

| Setting value to 0 sets it to Infinite


Viewport Camera Bookmarks
===========================

.. figure:: 02_Viewport_Camera/images/06.webp

Bookmarks save viewport camera location

| Bookmarks are saved into current level.
| Bookmarks are moving the camera in ALL viewport windows.

| Go to bookmark: Any number key from ``[0]`` to ``[9]``
| Set new bookmark: ``[CTRL]`` + Any number key from ``[0]`` to ``[9]``

.. figure:: 02_Viewport_Camera/images/07.webp

    You can manage bookmarks in ``Viewport Options`` menu.


``Compact Bookmarks`` simply removes empty slot gaps between saved bookmarks.

.. figure:: 02_Viewport_Camera/images/09.webp

Focus camera
===========================

Focus viewport camera on selected actor(s)
--------------------------------------------

Select at least one actor and press ``F``

.. figure:: 02_Viewport_Camera/images/01.webp


Change Camera Speed
===========================

.. figure:: 02_Viewport_Camera/images/02.webp

Use ``Change Camera Speed`` menu in editor viewport. 

| ``Camera Speed Scalar`` multiplies that value, allowing for more precise or faster camera movement.


Realtime Toggle
===========================

.. figure:: 02_Viewport_Camera/images/36.webp

.. image:: 02_Viewport_Camera/images/34.webp
    :width: 45%

.. image:: 02_Viewport_Camera/images/35.webp
    :width: 45%

Disabling realtime pauses all animations, physics and particle systems.

| While realtime is off, some windows will report it to the user and viewport toolbar will have extra toggle to turn it on.
| Keyboard shortcut is ``[CTRL] + [R]``

.. note::
    
    While using Simulate or Play, viewport is only updated while viewport camera is moving.

