# -*- coding: utf8 -*-

# Copyright 2008 Jaap Karssenberg <pardus@cpan.org>

'''FIXME'''

import types

def get_plugin(pluginname):
	'''FIXME'''
	# __import__ has some quirks, see the reference manual
	pluginname = pluginname.lower()
	mod = __import__('zim.plugins.'+pluginname)
	mod = getattr(mod, 'plugins')
	mod = getattr(mod, pluginname)
	for name in dir(mod):
		obj = getattr(mod, name)
		if ( isinstance(obj, (type, types.ClassType)) # is a class
		and issubclass(obj, PluginClass) # is derived from PluginClass
		and not obj == PluginClass ): # but is not PluginClass itself
			return obj


class PluginClass(object):

	info = {}

	def __init__(self, ui):
		self.ui = ui
		# TODO: assert self.info['name'] ['author'] etc.

	def disconnect(self):
		'''FIXME'''
		self.ui.remove_actions(self)
