.. _Editor Static Mesh Menu:

==============================
Static Mesh Menu
==============================

.. figure:: StaticMeshEditorWindow/images/01.webp
    :align: center


viewport ground plame mesh is 40x40x1m

.. figure:: StaticMeshEditorWindow/images/22.webp
    :align: center

Each static mesh edge is selectable. Selected edge will be highlighted in yellow

.. note::

    Mesh is triangulated before importing into Unreal Engine. Some faces (quads) have a diagonal edge. 




Toolbar
====================

.. figure:: StaticMeshEditorWindow/images/02.webp
    :align: center

.. table::

    +------------------------------------------------+-----------------------------------------------------------------------------------------------+
    | Element                                        | Description                                                                                   |
    +================================================+===============================================================================================+
    | .. figure:: StaticMeshEditorWindow/images/03.webp                        | Save changes set in static mesh asset                            |
    |     :align: center                             |                                                                                               |
    +------------------------------------------------+-----------------------------------------------------------------------------------------------+
    | .. figure:: StaticMeshEditorWindow/images/04.webp                        | | Finds asset in last open asset browser                                                      |
    |     :align: center                             | | Keyboard Shortcut: ``[CTRL] + [B]``                                                         |
    +------------------------------------------------+-----------------------------------------------------------------------------------------------+
    | .. figure:: StaticMeshEditorWindow/images/05.webp                        | Reimports static mesh from source file.                                                       |
    |     :align: center                             | If source file does not exist or was moved, file browser will pop up.                         |
    |                                                |                                                                                               |
    +------------------------------------------------+-----------------------------------------------------------------------------------------------+
    | .. figure:: StaticMeshEditorWindow/images/06.webp                        | Reimports static mesh from source file, and also custom LODs stored in source file            |
    |     :align: center                             |                                                                                               |
    +------------------------------------------------+-----------------------------------------------------------------------------------------------+
    | .. figure:: StaticMeshEditorWindow/images/07.webp                        | :ref:`Static Mesh Collision Options`                                                          |
    |     :align: center                             |                                                                                               |
    +------------------------------------------------+-----------------------------------------------------------------------------------------------+
    | .. figure:: StaticMeshEditorWindow/images/08.webp                        | :ref:`Static Mesh UV preview and options`                                                     |
    |     :align: center                             |                                                                                               |
    +------------------------------------------------+-----------------------------------------------------------------------------------------------+

Edit Simplified Collision

Add Sphere Simplified Collision - Creates a sphere collision than encompasses the mesh
Add Capsule Simplified Collision - Creates a capsule collision that encompasses the mesh
Add Box Simplified Collision - Creates a box collision that encompasses the mesh

Add DOP Collision

10-DOP-X  - Creates a box with beveled edges on X axis (10 faces in total)
18DOP - Creat6es a box with all edges beveled (18 faces in total)
26DOP - Creates a box with all edges and corners beveled (26 faces in total)

Convert Box to Convex - Converts all Box Simplified collisions to Convex Simplified collisions. Cannot be undone.

Remove Collision - Removes all simplified collision from the mesh.

Edit options for collisions are only available if simplified collision was selected in the viewport.

Copy Collision From Selected Static Mesh - Copies collision from static mesh that is selected in content browser

Find Source - If asset was imported from FBX/OBJ/... file, this feature opens up location of the source file in Explorer/Finder/...

Auto Convex Collision

Opens :ref:`Convex Decomposition` Editor tab


.. _Convex Decomposition:

Convex Decomposition
==========================

This menu allows quick automatic generation of simple collision convex hulls.

Hull Count - Maximum count of Convex Collision Hulls
Max Hull Verts - Maximum count of verticles for each generated convex collision hulls.

.. figure:: StaticMeshEditorWindow/images/09.webp
    :align: center


Hull Precision - Count of voxels to determine placement of verticles creating each collision hull

.. note::
    Depending on complexity of the mesh and input settings, this operation can take a while


Toolbar UV menu
======================

.. figure:: StaticMeshEditorWindow/images/10.webp
    :align: center

UV Menu allows previewing or removing UV Maps from static mesh.

.. note::
    If :ref:`Generate Lightmap UVs` was selected while importing static mesh, there will be an extra generated UV Map for lightmap, usually with last index.

Selecting one of UV Map channels enables preview in left lower corner of the viewport

.. figure:: StaticMeshEditorWindow/images/11.webp
    :align: center

To remove UV Map press ``Remove Selected``

.. note::

    If static mesh has a single UVMap, it cannot be removed.

    UV Maps generated for lightmap cannot be removed via this menu. Change :ref:`Destination lightmap index` to remove it.


Extra Viewport Elements
========================

dataprepviewportsetting
[TODO]

Duplicate ``Player Collision`` and ``Visibility Collision`` view modes

.. figure:: StaticMeshEditorWindow/images/12.webp
    :align: center

View Menu in Toolbar
---------------------

Sockets
```````````````````
.. figure:: StaticMeshEditorWindow/images/13.webp
    :align: center

Draws a octahedron at each socket position

| Keyboard Shortcut ``[ALT] + [S]``

Verticles
```````````````````
.. figure:: StaticMeshEditorWindow/images/14.webp
    :align: center

Draws cubes on each verticle position.

| Keyboard Shortcut ``[ALT] + [V]``

.. note::

    Do not enable on high density meshes! It will slow down and might crash the editor.


Vert Colors
```````````````````
.. figure:: StaticMeshEditorWindow/images/15.webp
    :align: center

Shows Vertex Colors created in `DCC Software`_. See :ref:`Importing Vertex Colors`

[TODO]
.. _DCC: Digital Content Creation Software eg. Blender, Maya, 3DSMax...

Normals
```````````````````
.. figure:: StaticMeshEditorWindow/images/16.webp
    :align: center

Shows vertex normals. 

| Keyboard Shortcut ``[ALT] + [N]``


Tangents
```````````````````

.. figure:: StaticMeshEditorWindow/images/17.webp
    :align: center

Shows vertex tangents. `What is tangent? <https://gamedev.stackexchange.com/questions/51399/what-are-normal-tangent-and-binormal-vectors-and-how-are-they-used>`

| Keyboard Shortcut ``[ALT] + [T]``


Binormals
```````````````````

.. figure:: StaticMeshEditorWindow/images/18.webp
    :align: center

Shows vertex Binormals. Ortohogonal (perpendicular) vector to normal and tangent.

`More about binormals <https://gamedev.stackexchange.com/questions/51399/what-are-normal-tangent-and-binormal-vectors-and-how-are-they-used>`

| Keyboard Shortcut ``[ALT] + [B]``


Pivot
```````````````````
.. figure:: StaticMeshEditorWindow/images/19.webp
    :align: center

Shows mesh pivot point.

| Keyboard Shortcut ``[ALT] + [P]``


Grid
```````````````````
.. figure:: StaticMeshEditorWindow/images/20.webp
    :align: center

Shows ground grid. It's size can be configured in :ref:`Snapping Menu`


Bounds
```````````````````

.. figure:: StaticMeshEditorWindow/images/21.webp
    :align: center

Shows the bounding box (red) and bounding sphere (yellow) around the mesh.

.. note:: 
    
    This also includes the preview ground mesh in the viewport.



Simple Collision
```````````````````

.. figure:: StaticMeshEditorWindow/images/23.webp
    :align: center

Shows static mesh simple collision and allows editing it in the viewport. See :ref:`Creating Simple Collision`



Complex Collision
```````````````````
.. figure:: StaticMeshEditorWindow/images/24.webp
    :align: center

Shows complex collision. See :ref:`Complex Collision`

.. note::
    Complex collision cannot be translated, as it is based on on mesh itself.


Physical Material Masks
```````````````````````
.. figure:: StaticMeshEditorWindow/images/25.webp
    :align: center

If your mesh has a material with Physical Material Mask set, this will show the mask on the mesh. 

See :ref:`Setting up Physical Material Masks`


LOD Menu in the toolbar
------------------------

.. figure:: StaticMeshEditorWindow/images/26.webp
    :align: center

* **LOD Auto** - Switches LOD levels automatically, based on rendered size of the mesh on the screen
* **LOD X** - Forces preview of X LOD level in this viewport



Details Panel
=============================

Details panel contains all information and configuration of the static mesh. Many entries are the same as shown in :ref:`Import Settings`.

Material Slots
-------------------

.. figure:: StaticMeshEditorWindow/images/29.webp
    :align: center


Shows all materials assigned to this static mesh.

New slots can be added using |materialslotadd| button.

[TODO] What is the use for them?

Slots can be named, in |materialsslotname|

[TODO] What is the use for the slot name?

* |MaterialsSlotSetFromContentBrowser| will replace the material in this slot with material selected in :ref:`Content Browser`
* |MaterialsSlotFindMaterialInContentBrowser| will find assigned material in :ref:`Content Browser`.
* |MaterialsSlotListMaterialTextures| shows the list of used textures in material assigned in this material slot. Clicking on any entry will find the texture in :ref:`Content Browser`

.. |materialslotadd| image:: StaticMeshEditorWindow/images/30.webp
.. |materialsslotname| image:: StaticMeshEditorWindow/images/31.webp
.. |MaterialsSlotSetFromContentBrowser| image:: StaticMeshEditorWindow/images/32.webp
.. |MaterialsSlotFindMaterialInContentBrowser| image:: StaticMeshEditorWindow/images/33.webp
.. |MaterialsSlotListMaterialTextures| image:: StaticMeshEditorWindow/images/34.webp

Using |MaterialSlotHighlight| will highlight the mesh part that uses this material.

.. figure:: StaticMeshEditorWindow/images/27.webp
    :align: center

Using |MaterialSlotIsolate| will hide any static mesh faces using other materials.

.. figure:: StaticMeshEditorWindow/images/28.webp
    :align: center

.. |MaterialSlotHighlight| image:: StaticMeshEditorWindow/images/35.webp
.. |MaterialSlotIsolate| image:: StaticMeshEditorWindow/images/36.webp


destination lightmap index, if you set it higher than last lastindex+1 it will temporarilty create empty uvmaps and set it to lastindex+1 anyway

remove degenerates option is force enabled with nanite enabled


""doggo_hp_Alberto_hp_old has degenerate tangent bases which will result in incorrect shading.  MikkTSpace relies on tangent bases and may result in mesh corruption, consider disabling this option. ""

