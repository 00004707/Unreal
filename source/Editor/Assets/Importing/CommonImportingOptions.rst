.. _Importing Assets Common Options:

========================================
Common Importing Assets options
========================================



.. _Mesh Import Create Content Folder Hierarchy:

Create Content Folder Hierarchy
------------------------

.. figure:: images/04.webp
    :align: center

If assets are grouped or parented, this feature will place those assets in separate folders with same name as group/parent name.

Shared/Linked assets will be placed inside of folder containing first asset in hierarchy that uses it.


.. admonition:: See also
    :class: seealso

    Assets used in this example: 
    
    * `ISLAND by Stéphane Agullo is licensed under Creative Commons Attribution <https://sketchfab.com/3d-models/island-80036f71b0014f0fbae6732d2465b64d>`_





.. _Mesh Import Import as Dynamic:

Import as Dynamic
------------------------
Sets :ref:`actor mobility <Actor Mobility>` of all imported actors to dynamic, instead of static.



.. _Mesh Import Hierarchy Type:

Hierarchy type
------------------------
1. Create one Blueprint Asset

    Imported assets will be added to a single blueprint that will be placed in current level. Groups will be converted into scene components.

.. |ht_img0| figure:: images/06.webp
    :align: center

* Create one Actor with components

    Imported assets will be added to single actor in level, **without a blueprint**. 
    
    Actor containing assets will not be shown in asset browser. Assets themselves, will be shown.

* Create Level actors

    Imported assets will be added to level as separate actors. Actors will be automatically attached to parents, if applicable. See :ref:`Attach Actor`




.. _Mesh Import Force Front XAxis:

Force Front XAxis
-------------------------------

If your assets are front towards X axis instead of Y- select this option.

.. note ::

    While exporting from blender, it looks like it should be aligned towards X- not X axis while this is enabled.



.. _Mesh Import Bake Pivot in Vertex:

Bake Pivot in Vertex
-------------------------------

Sets custom pivot point position of imported mesh as the pivot point in Unreal Engine


.. admonition:: Note
    :class: hint

    Blender bakes custom mesh pivot point while exporting FBX files.


.. _Mesh Import Import Static Mesh LOD:

Import Static Mesh LOD
----------------------------

Imports custom static mesh LODs. See :ref:`Creating Static Mesh LOD`

Disabled imports only LOD0


.. _Mesh Import Import Skeletal Mesh LOD:

Import Skeletal Mesh LOD
----------------------------

Imports custom skeletal mesh LODs. See :ref:`Creating Skeletal Mesh LOD`

Disabled imports only LOD0


.. _Mesh Import Invert Normal Maps:

Invert Normal Maps
----------------------

If your materials contain OpenGL type Normal Maps, use this option to automatically convert them to DirectX format.
See :ref:`Normal Maps`



.. _Mesh Import Generate Missing Collision:

Generate Missing Collision
------------------------------

If any asset inside of FBX file does not have custom collsion, this feature will generate it.

.. admonition:: Note
    :class: note

    This does not override custom collision. See also: :ref:`Creating Custom Asset Collision`

.. _Mesh Import Vertex Color Import Option:

Vertex Color Import Option
----------------------------

* **Replace** - Imports Vertex Colors stored in the FBX file.
* **Ignore** - Does not import vertex colors set in FBX file
* **Override** - Sets vertex color to all verticles to color specified in :ref:`Mesh Import Vertex Override Color`


.. _Mesh Import Vertex Override Color:

Vertex Override Color
----------------------------

If :ref:`Vertex Color Import Option` is set to override, this defines what Vertex Color to set to all verticles


.. _Mesh Import Remove Degenerates:

Remove Degenerates
----------------------------

This feature removes all degenerate triangles. (triangles that are squashed and there is no face visible)


.. figure:: images/09.webp
    :align: center




.. _Mesh Import Build Reversed Index Buffer:

Build Reversed Index Buffer
----------------------------

Optimization technique that is used for meshes with negative scale. 

.. admonition:: Tip
    :class: tip

    If the mesh will always have positive scale, this can be turned off.

By ticking this option on, these buffers will be created:

* mesh indices reversed index buffer
* reversed depth-only index buffer

.. _Mesh Import Generate Lightmap UVs:

Generate Lightmap UVs
----------------------------

Generates an UVMap used for :ref:`lightmaps <lightmaps>`. 

.. admonition:: note
    :class: note
    
    New UVMap will have highest UVMap index.

See :ref:`Creating Lightmap UVs`


.. _Mesh Import One Convex Hull per UCX:

One Convex Hull per UCX
----------------------------

If a single custom collision object consists of multiple floating meshes, this option merges them into a single convex hull.

.. image:: images/10.webp
    :width: 45%

.. image:: images/11.webp
    :width: 45%


Leaving this option unticked, Unreal Engine will split it into multiple collision meshes, the same way as if it would be separated in :ref:`DCC Software <dcc software>` that the mesh is created in.

.. figure:: images/12.webp
    :align: center
    :width: 50%

.. admonition:: note
    :class: note

    Multiple custom collision objects created in :ref:`DCC Software <dcc software>` (eg. UCX_Mesh_01 and UCX_Mesh_02) will not be combined into one.


.. _Mesh Import Import Normal Method:

Import Normal Method
---------------------------

* **Compute Normals** - Ignores normals stored in FBX file and generates new data.
* **Import Normals** - Imports normal data from FBX file but generates tangents and binormals data
* **Import Normals and Tangents** - Imports both normals, tangents and binormals from FBX file.



.. _Mesh Import Normal Generation Method:

Normal Generation Method
---------------------------

If :ref:`Mesh Import Import Normal Method` is not set to ``Import Normals and Tangents``, generates new normal data using selected alghoritm.

.. admonition:: Tip
    :class: tip

    The Mikk TSpace requires a correctly mapped UVMap, otherwise :command:`"Object has Degenerate Tangent bases which will results in incorrect shading"` error will pop-up while importing. 

    This may lead to inaccurate lightining.

    The solution is to either use the :guilabel:`Built In` alghoritm, or to properly UV map your asset.

.. admonition:: See Also
    :class: seealso

    `Official Mikk TSpace website <http://www.mikktspace.com/>`_

    `Mikk TSpace Github <https://github.com/mmikk/MikkTSpace>`_






.. _Mesh Import Offset Translation:

Offset Translation
----------------------

Imported using content browser
`````````````````````````````````

Adds or subtracts position of static mesh


Imported into the level
`````````````````````````````````

Modifies world position of ``Scene`` actor, that imported assets from source file will be set to be a child of.


.. note::

    Meshes will be imported as normal, without those changes in their blueprints.

    .. figure:: images/24.webp
        :align: center


.. _Mesh Import Offset Rotation:

Offset Rotation
----------------------

Imported using content browser
`````````````````````````````````

Adds or subtracts rotation of the static mesh

Imported into the level
`````````````````````````````````

Add or subtract world rotation of ``Scene`` actor that imported assets from source file will be set to be a child of.

.. note::

    Meshes will be imported as normal, without those changes in their blueprints.

    .. figure:: images/24.webp
        :align: center


.. _Mesh Import Offset Uniform Scale:

Offset Uniform Scale
----------------------

Imported using content browser
`````````````````````````````````
Scales the static mesh

Imported into the level
`````````````````````````````````

Set world scale multiplier of ``Scene`` actor that imported assets from source file will be set to be a child of.

.. note::

    Meshes will be imported as normal, without those changes in their blueprints.

    .. figure:: images/24.webp
        :align: center


.. _Mesh Import Force All Mesh as Type:

Force All Mesh as Type
----------------------

Forces all meshes from file to be converted into static or skeletal mesh assets.


.. _Mesh Import Import Lods:

Import Lods
----------------------

Toggles importing :ref:`LODs <Creating LODs>` of static and skeletal meshes.


.. _Mesh Import Vertex Color Import Option:

Vertex Color Import Option
--------------------------------------------

* **Replace** - Imports Vertex Colors for new meshes or replaces them when reimporting
* **Ignore** - Does not import Vertex Colors or does not replace them when Reimporting
* **Override** - Sets new Vertex Color to all verticles with values set in :ref:`Mesh Import Vertex Override Color`


.. _Mesh Import Import Vertex Override Color:

Vertex Override Color
--------------------------------------------

Sets new Vertex Color to all verticles using provided value.



.. _Mesh Import Import Recompute Normals:

Recompute Normals
----------------------

Forces to recompute mesh normals instead of importing normals stored in source file.

.. _Mesh Import Recompute Tangents:

Recompute Tangents
----------------------

Forces to recompute normals instead of importing normals stored in source file.

.. _Mesh Import Use Mikk TSpace:

Use Mikk TSpace
----------------------

Uses :guilabel:`Mikk TSpace` alghoritm to recompute normals, instead of :guilabel:`Built In` alghoritm.

See :ref:`Mesh Import Normal Generation Method` for more info about differences in those alghoritms

.. _Mesh Import Compute Weighted Normals:

Compute Weighted Normals
--------------------------------------------

[TODO]

.. _Mesh Import Use High Precision Tangent Basis:

Use High Precision Tangent Basis
--------------------------------------------

[TODO]

.. _Mesh Import Use Full Precision UVs:

Use Full Precision UVs
--------------------------------------------

.. _Mesh Import Use Backwards Compatible F16Trunc UVs:

Use Backwards Compatible F16Trunc UVs
--------------------------------------------


.. _Mesh Import Import Meshes In Bone Hierarchy:

Meshes In Bone Hierarchy
----------------------

.. _Mesh Import Use T0As Ref Pose:

Use T0As Ref Pose
----------------------


.. _Mesh Import Import Animations:

Import Animations
----------------------

.. _Mesh Import Import Bone Tracks:

Import Bone Tracks
----------------------

.. _Mesh Import Animation Length:

Animation Length
----------------------

.. _Mesh Import Frame Import Range:

Frame Import Range
----------------------

.. _Mesh Import Use 30Hz to Bake Bone Animation:

Use 30Hz to Bake Bone Animation
--------------------------------------------

.. _Mesh Import Custom Bone Animation Sample Rate:

Custom Bone Animation Sample Rate
--------------------------------------------

.. _Mesh Import Snap To Closest Frame Boundary:

Snap To Closest Frame Boundary
------------------------------------------------------------------

.. _Mesh Import Import Attributes as Curves or Animation Attributes:

Import Attributes as Curves or Animation Attributes
------------------------------------------------------------------

.. _Mesh Import Set Material Curve Type:

Set Material Curve Type
--------------------------------------------

.. _Mesh Import Material Curve Suffixes:

Material Curve Suffixes
--------------------------------------------

.. _Mesh Import Remove Redundant Keys:

Remove Redundant Keys
----------------------

.. _Mesh Import Do not import curves with only 0 values:

Do not import curves with only 0 values
--------------------------------------------

.. _Mesh Import Delete Existing Animation Attributes:

Delete Existing Animation Attributes
--------------------------------------------

.. _Mesh Import Delete Existing Animation Curves:

Delete Existing Animation Curves
------------------------------------------------------------------

.. _Mesh Import Delete Existing Morph Target Curves:

Delete Existing Morph Target Curves
--------------------------------------------


.. _Mesh Import Import Materials:

Import Materials
----------------------

.. _Mesh Import Material Import:

Material Import
--------------------------------------------

.. _Mesh Import Parent Material:

Parent Material
----------------------





.. _Mesh Import Import Skeletal Meshes:

Import Skeletal Meshes
--------------------------------------------

.. _Mesh Import Import Content Type:

Import Content Type
--------------------------------------------

.. _Mesh Import Import Morph Targets:

Import Morph Targets
----------------------

.. _Mesh Import Update Skeleton Reference Pose:

Update Skeleton Reference Pose
--------------------------------------------

.. _Mesh Import Create Physics Asset:

Create Physics Asset
--------------------------------------------

.. _Mesh Import Threshold Position:

Threshold Position
----------------------

.. _Mesh Import Threshold Tangent Normal:

Threshold Tangent Normal
--------------------------------------------

.. _Mesh Import Threshold UV:

Threshold UV
--------------------------------------------

.. _Mesh Import Morph Threshold Position:

Morph Threshold Position
--------------------------------------------


.. _Mesh Import Import Static Meshes:

Import Static Meshes
--------------------------------------------

.. _Mesh Import Import Collision According To Mesh Name:

Import Collision According To Mesh Name
--------------------------------------------

.. _Mesh Import One Conves Hull Per UCX:

One Conves Hull Per UCX
--------------------------------------------

.. _Mesh Import Build Nanite:

Build Nanite
----------------------

.. _Mesh Import Build Reversed Index Buffer:

Build Reversed Index Buffer
--------------------------------------------

.. _Mesh Import Generate Lightmap UVs:

Generate Lightmap UVs
----------------------

.. _Mesh Import Two Sided Disatnce Field Generation:

Two Sided Disatnce Field Generation
--------------------------------------------

.. _Mesh Import Enable Physical Material Mask:

Enable Physical Material Mask
--------------------------------------------

.. _Mesh Import Min Lightmap Resolution:

Min Lightmap Resolution
--------------------------------------------

.. _Mesh Import Source Lightmap Index:

Source Lightmap Index
--------------------------------------------

.. _Mesh Import Destination Lightmap Index:

Destination Lightmap Index
--------------------------------------------

.. _Mesh Import Build Scale:

Build Scale
--------------------------------------------

.. _Mesh Import Distance Field Resolution Scale:

Distance Field Resolution Scale
--------------------------------------------

.. _Mesh Import Distance Field Replacement Mesh:

Distance Field Replacement Mesh
--------------------------------------------

.. _Mesh Import Max Lumen Mesh Cards:

Max Lumen Mesh Cards
----------------------


.. _Mesh Import Import Textures:

Import Textures
----------------------

.. _Mesh Import Detect Normal Map Texture:

Detect Normal Map Texture
--------------------------------------------

.. _Mesh Import Flip Normal Map Green Channel:

Flip Normal Map Green Channel
--------------------------------------------

.. _Mesh Import Import UDIMs:

Import UDIMs
----------------------

.. _Mesh Import File Extensions To Import as Long Lat Cubemap:

File Extensions To Import as Long Lat Cubemap
------------------------------------------------------------------

.. _Mesh Import Prefer Compressed Source Data:

Prefer Compressed Source Data
--------------------------------------------

.. _Mesh Import Allow Non Power of Two:

Allow Non Power of Two
--------------------------------------------







Creating Sockets in ...
========================

SOCKET_MeshName_00

do not apply scale, it's value is imported into unreal.
1.0 is ~ 2meter scale socket

