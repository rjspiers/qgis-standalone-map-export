from qgis.core import *

print 'Hello from QGIS'

import sys
# from qgis.core import (
	# QgsProject, QgsComposition, QgsApplication, QgsProviderRegistry)
from qgis.gui import QgsMapCanvas, QgsLayerTreeMapCanvasBridge
from PyQt4.QtCore import QFileInfo, QObject
from PyQt4.QtXml import QDomDocument


gui_flag = True
app = QgsApplication(sys.argv, gui_flag)

# Make sure QGIS_PREFIX_PATH is set in your env if needed!
app.initQgis()

# project.qgs
project_path = 'single_pdf.qgs' # absolute filepath example: 'C:/folder/subfolder/project.qgs'

# template.qpt
template_path = 'single_pdf_a4_landscape.qpt'

def make_pdf(xmin, ymin, xmax, ymax, filter_expression):
	canvas = QgsMapCanvas()
	# Load our project
	QgsProject.instance().read(QFileInfo(project_path))
	
	# Set canvas extent
	canvas.setExtent(QgsRectangle(xmin, ymin, xmax, ymax))
	
	# Load layers here if they are not already in the project
	for layer in QgsMapLayerRegistry.instance().mapLayers().values():
		if layer.name() == 'data':
			lyr = layer
			break
	lyr.setSubsetString(filter_expression)
	
	# bridge used in standalone script: http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/loadproject.html
	bridge = QgsLayerTreeMapCanvasBridge(
		QgsProject.instance().layerTreeRoot(), canvas)
	bridge.setCanvasLayers()

	# Check data providers load ok
	print('Provider List')
	print(QgsProviderRegistry.instance().providerList())
	
	# Print layer validity - I've had some trouble with some wms layers
	for layer in QgsMapLayerRegistry.instance().mapLayers().values():
		print(layer.name())
		print(layer.isValid())
	
	template_file = file(template_path)
	template_content = template_file.read()
	template_file.close()
	document = QDomDocument()
	document.setContent(template_content)
	composition = QgsComposition(canvas.mapSettings())
	# You can use this to replace any string like this [key]
	# in the template with a new value. e.g. to replace
	# [date] pass a map like this {'date': '1 Jan 2012'}
	substitution_map = {
		'title': 'the title of my map'}
	composition.loadFromTemplate(document, substitution_map)
	# You must set the id in the template
	map_item = composition.getComposerItemById('Main Map')
	map_item.setMapCanvas(canvas)
	map_item.zoomToExtent(canvas.extent())
	# You must set the id in the template
	legend_item = composition.getComposerItemById('Legend')
	legend_item.updateLegend()
	composition.refreshItems()
	composition.exportAsPDF('export.pdf')
	QgsProject.instance().clear()


filter_expression = '"name" IN ("Burpham Ward", "Send Ward", "Merrow Ward", "Holy Trinity Ward")'

make_pdf(500000, 150000, 505000, 155000, filter_expression) # this requires: (xmin, ymin, xmax, ymax, filter_expression), set filter_expression = '' if not needed
