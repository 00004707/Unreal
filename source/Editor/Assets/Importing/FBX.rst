.. _Importing Assets FBX:

========================================
Importing Assets using FBX Files
========================================

|
FBX (via :ref:`Import Into Level<Importing Assets Import Into Level>`)
--------------------------------------------------------------------------------------------


Using :ref:`Import Into Level <Importing Assets Import Into Level>` method will also create :ref:`FbxSceneImportData` asset.

.. admonition:: Tip
    :class: tip
    
    |xmark| button on tabs does not work.

.. |xmark| image:: images/05.webp


.. note::

    As of version 5.1, importing static meshes with custom collision will also create collision actors in the level for some reason.
    Collision is imported properly.

.. tab-set::
    ..tab-item:: Label1
        Markdown 1





|
Scene Tab
``````````````

.. figure:: images/03.webp
    :align: center

Outline of the scene in source file will be listed on the left side. Outline contains every asset and group contained in source file.

To exclude assets or groups from importing, **untick them in their category. Unticking in scene tab won't change anything**

.. figure:: images/07.webp
    :align: center

    Use expand/collapse buttons to quickly show all assets


.. note::

    Files imported from blender will not be grouped as blender uses ``Collections`` instead.
    
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

|
.. _ImportToLevel FBXImport Static Meshes:

Static Meshes Tab
`````````````````````

.. figure:: images/08.webp
    :align: center

Unticking elements in this tab will exclude them from importing. You can also select multiple meshes and press ``Right Mouse Button`` to add or remove them from importing.

**Reimporting**

If window was opened to reimport the file, new and deleted files from source FBX file will be marked with |meshplus| or |meshminus|

Files removed from FBX file will be also removed from Unreal Engine project. In order to not remove them, simply untick them.

Skeletal meshes tab supports :ref:`ImportToLevel FBXImport Setting Sets`

.. |meshminus| image:: images/13.webp

.. |meshplus| image:: images/14.webp


* :ref:`ImportToLevel Generate Missing Collision`
* :ref:`ImportToLevel Vertex Color Import Option`
* :ref:`ImportToLevel Vertex Override Color`
* :ref:`ImportToLevel Remove Degenerates`
* :ref:`ImportToLevel Build Reversed Index Buffer`
* :ref:`ImportToLevel Generate Lightmap UVs`
* :ref:`ImportToLevel One Convex Hull per UCX`
* :ref:`ImportToLevel Import Normal Method`
* :ref:`ImportToLevel Normal Generation Method`

|
Skeletal Meshes Tab
```````````````````````

.. figure:: images/21.webp
    :align: center

Skeletal meshes tab supports :ref:`ImportToLevel FBXImport Setting Sets`


* :ref:`ImportToLevel Update Skeleton Reference Pose`
* :ref:`ImportToLevel Create Physics Asset`
* :ref:`ImportToLevel Preserve Smoothing Groups`
* :ref:`ImportToLevel Import Meshes in Bone Hierarchy`
* :ref:`ImportToLevel Import Morph Targets`
* :ref:`ImportToLevel Morph Target Thresholds`

Animation Tab
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

Materials Tab
`````````````````````

.. figure:: images/22.webp
    :align: center

Unticking any material in this tab will exclude it from importing (or deleting if material was deleted from FBX file after previous import to Unreal Engine)

Material path override
''''''''''''''''''''''''

Materials can be imported into different directory. 

All of imported materaials will be placed in one directory. Subdirectories won't be created even when :ref:`Create Content Folder Hierarchy` is ticked in :ref:`ImportToLevel FBXImport Static Meshes`


.. _ImportToLevel FBXImport Setting Sets:

**Setting Sets**
`````````````````````

If multiple of static or skeletal meshes share same import settings, you can use Settings Sets to configure importing faster.

Use |fbx_sm_createoverride| and name your new settings set.

After adding a new setting set, press :kbd:`RightMouseButton` on selected static/skeletal meshes and pick new settings set from the context menu.

:kbd:`LeftMouseButton+Ctrl` to select multiple meshes.

.. figure:: images/19.webp
    :align: center


* To select all static meshes using custom settings set, press |fbx_sm_selectassetusing|.
* To remove custom settings set press |fbx_sm_settingsetdelete|
* To preview or modify settings set, but not apply it to the mesh use |fbx_sm_settingsetlist|
* Assets with custom settings set will be marked as |fbx_sm_settingseticon|

.. |fbx_sm_createoverride| image:: images/15.webp

.. |fbx_sm_selectassetusing| image:: images/16.webp

.. |fbx_sm_settingsetdelete| image:: images/17.webp

.. |fbx_sm_settingsetlist| image:: images/18.webp

.. |fbx_sm_settingseticon| image:: images/20.webp