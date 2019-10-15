import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import os


ignore_empty = plugins.toolkit.get_validator('ignore_empty')

class TerriajsPreviewPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IResourceView, inherit=True)
    plugins.implements(plugins.ITemplateHelpers, inherit=True)

    TerriaJS_Formats = ['wms', 'wfs', 'kml', 'kmz', 'gjson', 'geojson', 'czml']

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'terriajs_preview')

    def info(self):
        return {
            'name': 'terriajs_view',
            'title': 'TerriaJS Beta',
            'always_available': True,
            'default_title': 'TerriaJS Beta View',
            'icon': 'globe',
            'schema': {'extent': [ignore_empty, unicode], 'show_extent': [ignore_empty, unicode]},
            'iframed': False
        }

    def can_view(self, data_dict):
        resource = data_dict['resource']
        format_lower = resource['format'].lower()
        if format_lower == '':
            format_lower = os.path.splitext(resource['url'])[1][1:].lower()
        #        print format_lower
        if format_lower in self.TerriaJS_Formats:
            return True
        return False

    def setup_template_variables(self, context, data_dict):
        return {
            'resource_view': data_dict['resource_view'],
            'resource': data_dict['resource'],
            'package': data_dict['package'],
        }

    def view_template(self, context, data_dict):
        return 'terriajs.html'

    def form_template(self, context, data_dict):
        return 'terriajs_form.html'

    # ITemplateHelpers
    def get_helpers(self):
        return {
            'extent_str_to_coords': self.extent_str_to_coords
        }

    def extent_str_to_coords(self, extent):
        '''
        Takes a string representing the two points of the extent, strips square brackets and returns the coordinates
        as a dict
        :param extent: string, e.g. [143.819362,-37.8244315,144.984938,-36.75134]
        :return:
        '''
        if extent.startswith('[') and extent.endswith(']'):
            extent = extent.replace('[', '').replace(']', '').split(',')

            #return extent.split(',')
            return {
                'point_1': {
                    'lon': extent[0],
                    'lat': extent[1]
                },
                'point_2': {
                    'lon': extent[2],
                    'lat': extent[3]
                },
            }
