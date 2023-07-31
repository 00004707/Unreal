==========================
Importing Assets
==========================



TEST FOR LINKED ASSETS!!!!

Import Into Level
=======================

.. figure:: Importing/images/01.*
    :align: center

To import whole scenes in more controlled way use ``Import Into Level``

.. note::

    Only ``FBX``, ``GLTF``, ``GLB`` and ``MTLX`` formats are supported by this function.

.. note::

    Using this method will create a single .uasset file in project directory, instead of many separate ones.

After selecting source file all other windows won't be interactible. To create a new folder, right click on parent folder.

.. figure:: Importing/images/02.*
    :align: center

Depending on source file format, different windows will open.

FBX
-----------------------

A new window will pop up with tabs representing categorized options for importing.

Using this method will also create :ref:`FbxSceneImportData` asset.

.. note::

    If you feel anxious about accidentally closing those tabs, fear not, as |xmark| button does not work.

.. |xmark| image:: Importing/images/05.*


.. note::

    As of version 5.1, importing static meshes with custom collision will also create collision actors in the level, for some reason.
    Collision is imported properly though.


Scene
``````````````

.. figure:: Importing/images/03.*
    :align: center

Outline of the scene in source file will be listed on the left side. Outline contains every asset and group contained in source file.

To exclude assets or groups from importing, **untick them in their category. Unticking in scene tab won't change anything.** 

.. figure:: Importing/images/07.*
    :align: center

    Use expand/collapse buttons to quickly show all assets


.. note::

    Files imported from blender will not be grouped as blender uses ``Collections`` instead. [ARE YOU SURE????????????????????????????]
    
    To create fake groups in blender, parent assets to an empty and name it as you wish. Empties do not have to share same collection as assets.

    While importing :ref:`FbxSceneImportData` asset will be created, which only purpose is to allow reimporting or adding new assets from single source file.

Import Options
''''''''''''''''''

* :ref:`Create Content Folder Hierarchy`
* :ref:`Import as Dynamic`
* :ref:`Hierarchy Type`
* :ref:`Force Front XAxis`

Meshes
''''''''''''''''''

* :ref:`Bake Pivot in Vertex`
* :ref:`Import Static Mesh LOD`
* :ref:`Import Skeletal Mesh LOD`

Texture
''''''''''''''''''

* :ref:`LevelImport Invert Normal Maps`

.. _ImportToLevel FBXImport Static Meshes:

Static Meshes
``````````````

.. figure:: Importing/images/08.*
    :align: center

Unticking elements in this tab will exclude them from importing. You can also select multiple meshes and press ``[Right Mouse Button]`` to add or remove them from importing.

.. _ImportToLevel FBXImport Static Meshes Setting Sets:

**Setting Sets**
''''''''''''''''''

If you want to some meshes use different settings, use |fbx_sm_createoverride| and name your new settings set.

After adding new setting set, press ``[Right Mouse Button]`` on selected static meshes and pick new settings set from the context menu.

``[Left Mouse Button] + [Ctrl]`` to select multiple meshes.

.. figure:: Importing/images/19.*
    :align: center


* To select all static meshes using custom settings set, press |fbx_sm_selectassetusing|.
* To remove custom settings set press |fbx_sm_settingsetdelete|
* To preview or modify settings set, but not apply it to the mesh use |fbx_sm_settingsetlist|
* Assets with custom settings set will be marked as |fbx_sm_settingseticon|

.. |fbx_sm_createoverride| image:: Importing/images/15.*

.. |fbx_sm_selectassetusing| image:: Importing/images/16.*

.. |fbx_sm_settingsetdelete| image:: Importing/images/17.*

.. |fbx_sm_settingsetlist| image:: Importing/images/18.*

.. |fbx_sm_settingseticon| image:: Importing/images/20.*

**Reimporting**

If window was opened to reimport the file, new and deleted files from source FBX file will be marked with |meshplus| or |meshminus|

Files removed from FBX file will be also removed from Unreal Engine project. In order to not remove them, simply untick them.

.. |meshminus| image:: Importing/images/13.*

.. |meshplus| image:: Importing/images/14.*




* :ref:`ImportToLevel Generate Missing Collision`
* :ref:`ImportToLevel Vertex Color Import Option`
* :ref:`ImportToLevel Vertex Override Color`
* :ref:`ImportToLevel Remove Degenerates`
* :ref:`ImportToLevel Build Reversed Index Buffer`
* :ref:`ImportToLevel Generate Lightmap UVs`
* :ref:`ImportToLevel One Convex Hull per UCX`
* :ref:`ImportToLevel Import Normal Method`
* :ref:`ImportToLevel Normal Generation Method`

Skeletal Meshes
`````````````````

.. figure:: Importing/images/21.*
    :align: center

Just like :ref:`ImportToLevel FBXImport Static Meshes`, skeletal meshes also support :ref:`ImportToLevel FBXImport Static Meshes Setting Sets`


Skeletal Mesh
''''''''''''''''''

* :ref:`ImportToLevel Update Skeleton Reference Pose`
* :ref:`ImportToLevel Create Physics Asset`
* :ref:`ImportToLevel Preserve Smoothing Groups`
* :ref:`ImportToLevel Import Meshes in Bone Hierarchy`
* :ref:`ImportToLevel Import Morph Targets`
* :ref:`ImportToLevel Morph Target Thresholds`

Animation
''''''''''''''''''

* :ref:`ImportToLevel Import Animations`
* :ref:`ImportToLevel Animation Length`
* :ref:`ImportToLevel Frame Import Range`
* :ref:`ImportToLevel Use Default Sample Rate`
* :ref:`ImportToLevel Snap to Closest Frame Boundary`
* :ref:`ImportToLevel Import Attributes as Curves or Animation`
* :ref:`ImportToLevel Deelte Existing Animation Curves`
* :ref:`ImportToLevel Delete Existing Animation Attributes`
* :ref:`ImportToLevel Preserve Local Transform`
* :ref:`ImportToLevel Delete Existing Morph Target Curves`

Materials
`````````````````````

.. figure:: Importing/images/22.*
    :align: center

Unticking any material in this tab will exclude it from importing (or deleting if material was deleted from FBX file after previous import to Unreal Engine)

Material path override
''''''''''''''''''''''''

Materials can be imported into different directory. 

All of imported materaials will be placed in one directory. Subdirectories won't be created even when :ref:`Create Content Folder Hierarchy` is ticked in :ref:`ImportToLevel FBXImport Static Meshes` tab




glT/glTF
-----------------------

.. figure:: Importing/images/25.*
    :align: center

All types of glTF files are supported

* .glT
* .glTF
* .glTF with separate texture files

Untick |gltf auto apply settings to all| if you want to set different settings to different imported files.


.. |gltf auto apply settings to all| image:: /images/23.*

Common
''''''''''''''''''''''''''''''''''''

* :ref:`gltf Import Offset Translation`
* :ref:`gltf Import Offset Rotation`
* :ref:`gltf Import Offset Uniform Scale`


Common Meshes
''''''''''''''''''''''''''''''''''''

* :ref:`gltf Import Force All Mesh as Type`
* :ref:`gltf Import Import Lods`
* :ref:`gltf Import Vertex Color Import Option`
* :ref:`gltf Import Vertex Override Color`
* :ref:`gltf Import Recompute Normals`
* :ref:`gltf Import Recompute Tangents`
* :ref:`gltf Import Use Mikk TSpace`
* :ref:`gltf Import Compute Weighted Normals`
* :ref:`gltf Import Use High Precision Tangent Basis`
* :ref:`gltf Import Use Full Precision UVs`
* :ref:`gltf Import Use Backwards Compatible F16Trunc UVs`
* :ref:`gltf Import Remove Degenerates`

Common Skeletal Meshes And Animations
''''''''''''''''''''''''''''''''''''''

* :ref:`gltf Import Import Meshes In Bone Hierarchy`
* :ref:`gltf Import Use T0As Ref Pose`

Static Meshes
'''''''''''''''''''''''''''''''''''''''

* :ref:`gltf Import Import Static Meshes`
* :ref:`gltf Import Import Collision According To Mesh Name`
* :ref:`gltf Import One Conves Hull Per UCX`
* :ref:`gltf Import Build Nanite`
* :ref:`gltf Import Build Reversed Index Buffer`
* :ref:`gltf Import Generate Lightmap UVs`
* :ref:`gltf Import Two Sided Disatnce Field Generation`
* :ref:`gltf Import Enable Physical Material Mask`
* :ref:`gltf Import Min Lightmap Resolution`
* :ref:`gltf Import Source Lightmap Index`
* :ref:`gltf Import Destination Lightmap Index`
* :ref:`gltf Import Build Scale`
* :ref:`gltf Import Distance Field Resolution Scale`
* :ref:`gltf Import Distance Field Replacement Mesh`
* :ref:`gltf Import Max Lumen Mesh Cards`

Skeletal Meshes
''''''''''''''''''''''''''''''''''''

* :ref:`gltf Import Import Skeletal Meshes`
* :ref:`gltf Import Import Content Type`
* :ref:`gltf Import Import Morph Targets`
* :ref:`gltf Import Update Skeleton Reference Pose`
* :ref:`gltf Import Create Physics Asset`
* :ref:`gltf Import Threshold Position`
* :ref:`gltf Import Threshold Tangent Normal`
* :ref:`gltf Import Threshold UV`
* :ref:`gltf Import Morph Threshold Position`



Animations
''''''''''''''''''''''''''''''''''''

* :ref:`gltf Import Import Animations`
* :ref:`gltf Import Import Bone Tracks`
* :ref:`gltf Import Animation Length`
* :ref:`gltf Import Frame Import Range`
* :ref:`gltf Import Use 30Hz to Bake Bone Animation`
* :ref:`gltf Import Custom Bone Animation Sample Rate`
* :ref:`gltf Import Snap To Closest Frame Boundary`
* :ref:`gltf Import Import Attributes as Curves or Animation Attributes`
* :ref:`gltf Import Set Material Curve Type`
* :ref:`gltf Import Material Curve Suffixes`
* :ref:`gltf Import Remove Redundant Keys`
* :ref:`gltf Import Do not import curves with only 0 values`
* :ref:`gltf Import Delete Existing Animation Attributes`
* :ref:`gltf Import Delete Existing Animation Curves`
* :ref:`gltf Import Delete Existing Morph Target Curves`

Materials
''''''''''''''''''''''''''''''''''''

* :ref:`gltf Import Import Materials`
* :ref:`gltf Import Material Import`
* :ref:`gltf Import Parent Material`

Textures
''''''''''''''''''''''''''''''''''''

* :ref:`gltf Import Import Textures`
* :ref:`gltf Import Detect Normal Map Texture`
* :ref:`gltf Import Flip Normal Map Green Channel`
* :ref:`gltf Import Import UDIMs`
* :ref:`gltf Import File Extensions To Import as Long Lat Cubemap`
* :ref:`gltf Import Prefer Compressed Source Data`
* :ref:`gltf Import Allow Non Power of Two`





.. _Create Content Folder Hierarchy:

Create Content Folder Hierarchy
'''''''''''''''''''''''''''''''''

.. figure:: Importing/images/04.*
    :align: center

If assets are grouped or parented, this feature will place those assets in separate folders with same name as group/parent name.

Shared/Linked assets will be placed inside of folder containing first asset in hierarchy that uses it.


.. note ::
    Assets used in this example: 
    
    * `ISLAND by Stéphane Agullo is licensed under Creative Commons Attribution <https://sketchfab.com/3d-models/island-80036f71b0014f0fbae6732d2465b64d>`_





.. _Import as Dynamic:

Import as Dynamic
'''''''''''''''''''''''''''''''''
Simply sets mobility of all imported actors to dynamic, instead of static.



.. _Hierarchy Type:

Hierarchy type
'''''''''''''''''''''''''''''''''
* Create one Blueprint Asset

    Imported assets will be added to a single blueprint that will be placed in current level. Groups will be converted into scene components.

.. |ht_img0| figure:: Importing/images/06.*
    :align: center

* Create one Actor with components

    Imported assets will be added to single actor in level, **without a blueprint**. 
    
    Actor containing assets will not be shown in asset browser. Assets themselves, will be shown.

* Create Level actors

    Imported assets will be added to level as separate actors. Actors will be automatically attached to parents, if applicable. See :ref:`Attach Actor`




.. _Force Front XAxis:

Force Front XAxis
-------------------------------

If your assets are front towards X axis instead of Y- select this option.

.. note ::

    While exporting from blender, it looks like it should be aligned towards X- not X axis while this is enabled.



.. _Bake Pivot in Vertex:

Bake Pivot in Vertex
-------------------------------

Makes pivot point saved in source file being


.. note::

    Does not apply for Blender users as Blender already does that while exporting FBX file.


.. _Import Static Mesh LOD:

Import Static Mesh LOD
----------------------------

Self explanatory. See :ref:`Creating Static Mesh LOD`

Disabled = Only import LOD0


.. _Import Skeletal Mesh LOD:

Import Skeletal Mesh LOD
----------------------------

Self explanatory. See :ref:`Creating Skeletal Mesh LOD`

Disabled = Only import LOD0


.. _LevelImport Invert Normal Maps:

Invert Normal Maps
----------------------

If your materials contain OpenGL type Normal Maps, use this option to automatically convert them to DirectX format.
See :ref:`Normal Maps`



.. _ImportToLevel Generate Missing Collision:

Generate Missing Collision
------------------------------

If any asset inside of FBX file do not have custom collsion, this feature will generate it.

This does not override custom collision. See :ref:`Creating Custom Asset Collision`



.. _ImportToLevel Vertex Color Import Option:

Vertex Color Import Option
----------------------------

* **Replace** - Simply imports Vertex Colors set in FBX file.
* **Ignore** - Does not import vertex colors set in FBX file
* **Override** - Sets vertex color to all verticles to color specified in :ref:`ImportToLevel Vertex Override Color`


.. _ImportToLevel Vertex Override Color:


Vertex Override Color
----------------------------

If :ref:`Vertex Color Import Option` is set to override, this defines what Vertex Color to set to all verticles


.. _ImportToLevel Remove Degenerates:

Remove Degenerates
----------------------------

This feature removes all degenerate triangles. (triangles that are so much squashed that they became a line)


.. figure:: Importing/images/09.*
    :align: center




.. _ImportToLevel Build Reversed Index Buffer:

Build Reversed Index Buffer
----------------------------

[TODO] ? Reversed index buffer, used to prevent changing culling state between drawcalls.
? disable Reverse index buffer if you are never inverting your mesh by scaling negatively.

.. _ImportToLevel Generate Lightmap UVs:

Generate Lightmap UVs
----------------------------

Generates an UVMap for Lightmap (baked lightning). New UVMap will have index of [last UVMap index in source file]+1.

See :ref:`Creating Lightmap UVs`


.. _ImportToLevel One Convex Hull per UCX:

One Convex Hull per UCX
----------------------------

If a single custom collision object consists of multiple floating meshes, this option merges them into a single convex hull.

.. image:: Importing/images/10.*
    :width: 45%

.. image:: Importing/images/11.*
    :width: 45%



Leaving this option unticked, Unreal Engine will split it into multiple collision meshes, the same way as if it would be separated in blender/maya/... as UCX_Mesh_01 and UCX_Mesh_02

.. figure:: Importing/images/12.*
    :align: center
    :width: 50%

| It does **not** merge other collision objects into one 
| (eg. UCX_Mesh_01 and UCX_Mesh_02 manually created in Blender/Maya/... will not be merged into one)



.. _ImportToLevel Import Normal Method:

Import Normal Method
---------------------------

* **Compute Normals** - Ignores normals stored in FBX file and generates new data.
* **Import Normals** - Imports normal data from FBX file but generates tangents and binormals data
* **Import Normals and Tangents** - Imports both normals, tangents and binormals from FBX file.



.. _ImportToLevel Normal Generation Method:

Normal Generation Method
---------------------------

If :ref:`ImportToLevel Import Normal Method` is not set to ``Import Normals and Tangents``, generates new normal data using selected alghoritm.

[TODO]



.. _FbxSceneImportData :

FbxSceneImportData 
---------------------------

FbxSceneImportData asset purpose is to provide functionality of reimporting, adding and removing assets from single FBX file.


.. note::
    
    If :ref:`Create Content Folder Hierarchy` was checked, new folders might not show up in asset browser on reimporting.
    
    Creating these folders manually, using :ref:`Save All` or restarting editor will fix the issue.

.. note::

    If :ref:`Create Content Folder Hierarchy` was checked, assets might temporarily be visible in asset browser as if this option was unchecked. Refreshing asset browser will fix the issue.






.. _gltf Import Offset Translation:

Offset Translation
----------------------

Add or subtract world position of ``Scene`` actor that imported assets from source file will be set to be a child of.


.. note::

    Meshes will be imported as normal, without those changes in their blueprints.

    .. figure:: Importing/images/24.*
        :align: center


.. _gltf Import Offset Rotation:

Offset Rotation
----------------------

Add or subtract world rotation of ``Scene`` actor that imported assets from source file will be set to be a child of.

.. note::

    Meshes will be imported as normal, without those changes in their blueprints.

    .. figure:: Importing/images/24.*
        :align: center


.. _gltf Import Offset Uniform Scale:

Offset Uniform Scale
----------------------

Set world scale multiplier of ``Scene`` actor that imported assets from source file will be set to be a child of.

.. note::

    Meshes will be imported as normal, without those changes in their blueprints.

    .. figure:: Importing/images/24.*
        :align: center


.. _gltf Import Force All Mesh as Type:

Force All Mesh as Type
----------------------

Forces all meshes from file to be converted into static or skeletal mesh assets.


.. _gltf Import Import Lods:

Import Lods
----------------------

Whether to import :ref:`LODs <Creating LODs>` of static and skeletal meshes.


.. _gltf Import Vertex Color Import Option:

Vertex Color Import Option
--------------------------------------------

* **Replace** - Imports Vertex Colors for new meshes or replaces them when reimporting
* **Ignore** - Does not import Vertex Colors or does not replace them when Reimporting
* **Override** - Sets new Vertex Color to all verticles with values set in :ref:`gltf Import Vertex Override Color`


.. _gltf Import Vertex Override Color:

Vertex Override Color
--------------------------------------------

Sets new Vertex Color to all verticles using provided value.



.. _gltf Import Recompute Normals:

Recompute Normals
----------------------

.. _gltf Import Recompute Tangents:

Recompute Tangents
----------------------

.. _gltf Import Use Mikk TSpace:

Use Mikk TSpace
----------------------

.. _gltf Import Compute Weighted Normals:

Compute Weighted Normals
--------------------------------------------

.. _gltf Import Use High Precision Tangent Basis:

Use High Precision Tangent Basis
--------------------------------------------

.. _gltf Import Use Full Precision UVs:

Use Full Precision UVs
--------------------------------------------

.. _gltf Import Use Backwards Compatible F16Trunc UVs:

Use Backwards Compatible F16Trunc UVs
--------------------------------------------

.. _gltf Import Remove Degenerates:

Remove Degenerates
--------------------------------------------





.. _gltf Import Import Meshes In Bone Hierarchy:

Meshes In Bone Hierarchy
----------------------

.. _gltf Import Use T0As Ref Pose:

Use T0As Ref Pose
----------------------


.. _gltf Import Import Animations:

Import Animations
----------------------

.. _gltf Import Import Bone Tracks:

Import Bone Tracks
----------------------

.. _gltf Import Animation Length:

Animation Length
----------------------

.. _gltf Import Frame Import Range:

Frame Import Range
----------------------

.. _gltf Import Use 30Hz to Bake Bone Animation:

Use 30Hz to Bake Bone Animation
--------------------------------------------

.. _gltf Import Custom Bone Animation Sample Rate:

Custom Bone Animation Sample Rate
--------------------------------------------

.. _gltf Import Snap To Closest Frame Boundary:

Snap To Closest Frame Boundary
------------------------------------------------------------------

.. _gltf Import Import Attributes as Curves or Animation Attributes:

Import Attributes as Curves or Animation Attributes
------------------------------------------------------------------

.. _gltf Import Set Material Curve Type:

Set Material Curve Type
--------------------------------------------

.. _gltf Import Material Curve Suffixes:

Material Curve Suffixes
--------------------------------------------

.. _gltf Import Remove Redundant Keys:

Remove Redundant Keys
----------------------

.. _gltf Import Do not import curves with only 0 values:

Do not import curves with only 0 values
--------------------------------------------

.. _gltf Import Delete Existing Animation Attributes:

Delete Existing Animation Attributes
--------------------------------------------

.. _gltf Import Delete Existing Animation Curves:

Delete Existing Animation Curves
------------------------------------------------------------------

.. _gltf Import Delete Existing Morph Target Curves:

Delete Existing Morph Target Curves
--------------------------------------------


.. _gltf Import Import Materials:

Import Materials
----------------------

.. _gltf Import Material Import:

Material Import
--------------------------------------------

.. _gltf Import Parent Material:

Parent Material
----------------------





.. _gltf Import Import Skeletal Meshes:

Import Skeletal Meshes
--------------------------------------------

.. _gltf Import Import Content Type:

Import Content Type
--------------------------------------------

.. _gltf Import Import Morph Targets:

Import Morph Targets
----------------------

.. _gltf Import Update Skeleton Reference Pose:

Update Skeleton Reference Pose
--------------------------------------------

.. _gltf Import Create Physics Asset:

Create Physics Asset
--------------------------------------------

.. _gltf Import Threshold Position:

Threshold Position
----------------------

.. _gltf Import Threshold Tangent Normal:

Threshold Tangent Normal
--------------------------------------------

.. _gltf Import Threshold UV:

Threshold UV
--------------------------------------------

.. _gltf Import Morph Threshold Position:

Morph Threshold Position
--------------------------------------------


.. _gltf Import Import Static Meshes:

Import Static Meshes
--------------------------------------------

.. _gltf Import Import Collision According To Mesh Name:

Import Collision According To Mesh Name
--------------------------------------------

.. _gltf Import One Conves Hull Per UCX:

One Conves Hull Per UCX
--------------------------------------------

.. _gltf Import Build Nanite:

Build Nanite
----------------------

.. _gltf Import Build Reversed Index Buffer:

Build Reversed Index Buffer
--------------------------------------------

.. _gltf Import Generate Lightmap UVs:

Generate Lightmap UVs
----------------------

.. _gltf Import Two Sided Disatnce Field Generation:

Two Sided Disatnce Field Generation
--------------------------------------------

.. _gltf Import Enable Physical Material Mask:

Enable Physical Material Mask
--------------------------------------------

.. _gltf Import Min Lightmap Resolution:

Min Lightmap Resolution
--------------------------------------------

.. _gltf Import Source Lightmap Index:

Source Lightmap Index
--------------------------------------------

.. _gltf Import Destination Lightmap Index:

Destination Lightmap Index
--------------------------------------------

.. _gltf Import Build Scale:

Build Scale
--------------------------------------------

.. _gltf Import Distance Field Resolution Scale:

Distance Field Resolution Scale
--------------------------------------------

.. _gltf Import Distance Field Replacement Mesh:

Distance Field Replacement Mesh
--------------------------------------------

.. _gltf Import Max Lumen Mesh Cards:

Max Lumen Mesh Cards
----------------------


.. _gltf Import Import Textures:

Import Textures
----------------------

.. _gltf Import Detect Normal Map Texture:

Detect Normal Map Texture
--------------------------------------------

.. _gltf Import Flip Normal Map Green Channel:

Flip Normal Map Green Channel
--------------------------------------------

.. _gltf Import Import UDIMs:

Import UDIMs
----------------------

.. _gltf Import File Extensions To Import as Long Lat Cubemap:

File Extensions To Import as Long Lat Cubemap
------------------------------------------------------------------

.. _gltf Import Prefer Compressed Source Data:

Prefer Compressed Source Data
--------------------------------------------

.. _gltf Import Allow Non Power of Two:

Allow Non Power of Two
--------------------------------------------







Creating Sockets in ...
========================

SOCKET_MeshName_00

do not apply scale, it's value is imported into unreal.
1.0 is ~ 2meter scale socket