# ckanext-terriajs-preview

_This is a work in progress and should not be used in production_

This extension requires an instance of _TerriaJS_ to be running locally on http://localhost:3001

You can follow the instructions here to set that up:

https://docs.terria.io/guide/getting-started/

## Installation

1. Clone this repo into `/usr/lib/ckan/default/src` (or equivalent dir for extensions)

1. Activate Python virtual environment:

        . /usr/lib/ckan/default/bin/activate
        
        cd /usr/lib/ckan/default/src/ckanext-terriajs-preview

1. Run setup:

        python setup.py develop

## Configuration

Add `terriajs_preview` to CKAN `.ini` file, e.g.

    ckan.plugins = ... terriajs_preview

## TODO

- Make TerriaJS configurable (add CKAN `.ini` file setting)
- Document creation of TerriaJS map preview in CKAN UI
