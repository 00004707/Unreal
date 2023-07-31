# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'unreal-docs'
copyright = '2023, 00004707'
author = '00004707'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.todo', 
              'sphinx.ext.githubpages', 
              'sphinx_copybutton', 
              'sphinxext.opengraph', 
              'sphinx.ext.intersphinx',
              'sphinx_favicon',
              "notfound.extension",
              'sphinx_last_updated_by_git']
              #'hoverxref.extension']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ['_static']
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#0051C4",
        "color-brand-content": "#0051C4",
        "color-admonition-background": "orange",
        "sidebar_hide_name": True,
        "navigation_with_keys": True,
    },

    "dark_css_variables": {
        "color-brand-primary": "orange",
        "color-brand-content": "#FF7F00",
        "sidebar_hide_name": True,
        "navigation_with_keys": True,
    },
    "navigation_with_keys": True,
    "sidebar_hide_name": False,
    "light_logo": "unreal_black.png",
    "dark_logo": "unreal_white.png",

}
html_title = "0004707 Unreal Docs"
html_sidebars = {
    "**": [
        "sidebar/scroll-start.html",
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/navigation.html",
        "sidebar/ethical-ads.html",
        "sidebar/scroll-end.html",
    ]
}

# faaaviiconss
favicons = [
   {
      "sizes": "16x16",
      "href": "favicon-16x16.png",
   },
   {
      "sizes": "32x32",
      "href": "favicon-32x32.png",
   },
   {
      "sizes": "192x192",
      "href": "android-chrome-192x192.png",
   },
   {
      "sizes": "512x512",
      "href": "android-chrome-512x512.png",
   },
   {
      "rel": "apple-touch-icon",
      "sizes": "180x180",
      "href": "apple-touch-icon.png",
   },
]

notfound_pagename = "404"
# todo 
#notfound_template = "_extra\\404.rst"
notfound_urls_prefix = "/Unreal/"

hoverxref_auto_ref = True
hoverxref_role_types = {
    'hoverxref': 'tooltip',
    'ref': 'tooltip',  # for hoverxref_auto_ref config
}