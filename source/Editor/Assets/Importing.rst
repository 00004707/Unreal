.. _Importing Assets:


.. toctree::
    :hidden:
    :glob:

    Importing/*


==========================
Importing Assets
==========================

Importing assets can be done in multiple ways in Unreal Engine.

.. _Importing Assets Import To Asset Browser:

Importing into asset browser
============================

.. _Importing Assets Import Into Level:

Import Into Level
=======================

.. figure:: Importing/images/01.webp
    :align: center

To import whole scenes and place them directly into the level, use ``Import Into Level``

.. admonition:: Warning
    :class: caution

    Only ``FBX``, ``GLTF``, ``GLB`` and ``MTLX`` formats are supported by this function.

.. admonition:: Warning
    :class: caution

    Using this method will create a single .uasset file in project directory, instead of many separate ones.

After selecting source file all other windows won't be interactible. To create a new folder, right click on parent folder.

.. figure:: Importing/images/02.webp
    :align: center

Depending on source file format, appropriate importing window will show up.



