# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
### (Don't forget to remove me)
# This is a basic skeleton for your plugin's __init__.py. You probably want to adjust the class name of your plugin
# as well as the plugin mixins it's subclassing from. This is really just a basic skeleton to get you started,
# defining your plugin as a template plugin, settings and asset plugin. Feel free to add or remove mixins
# as necessary.
#
# Take a look at the documentation on what other plugin mixins are available.
import octoprint.plugin
import octoprint.printer

class miskPlugin(octoprint.plugin.SettingsPlugin,
				 octoprint.plugin.AssetPlugin,
				 octoprint.plugin.TemplatePlugin,
				 octoprint.plugin.SimpleApiPlugin,
				 octoprint.plugin.StartupPlugin,
				 octoprint.plugin.EventHandlerPlugin):

    def on_after_startup(self):
        self._logger.info("miskPlugin")

    ##~~ AssetPlugin mixin
    def get_assets(self):
		# Define your plugin's asset files to automatically include in the
		# core UI here.
        return dict(
		js=["js/misk.js"]
		)


__plugin_name__ = "miskPlugin"
__plugin_pythoncompat__ = ">=3,<4"
__plugin_implementation__ = miskPlugin()
