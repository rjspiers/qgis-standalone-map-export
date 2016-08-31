# qgis-standalone-map-export

## How to use
### Setup and test for windows
- unzip this repo
- Edit [standalone_generate_pdf.bat](standalone_generate_pdf.bat) to set the `OSGEO4W_ROOT` to your install of QGIS. Edit path to your install of `python.exe` too (line 21).
- Open cmd window in the unzipped folder and run `standalone_generate_pdf.bat`. If everything goes ok you should see feedback in the console and a file `export.pdf` will be created in the folder. If you didn't get the 'Hello from QGIS' message then there is  a problem with the bat file config. See [export_expected_result.pdf](export_expected_result.pdf) for an example output.

### Customise the python script
Edit this for your situation: [standalone_generate_pdf.py](standalone_generate_pdf.py)
#### File paths:
```python
project_path = 'single_pdf.qgs'
template_path = 'single_pdf_a4_landscape.qpt'
composition.exportAsPDF('export.pdf')
```

#### Filter:
change the filter_expression:
```python
filter_expression = '"name" IN ("Burpham Ward", "Send Ward", "Merrow Ward", "Holy Trinity Ward")'
```
change the layer name `'data'` which the filter is applied to:
```python
	for layer in QgsMapLayerRegistry.instance().mapLayers().values():
		if layer.name() == 'data':
			lyr = layer
			break
	lyr.setSubsetString(filter_expression)
```

#### Location:
Specify coords to set the map canvas to:
```python
make_pdf(500000, 150000, 505000, 155000, filter_expression)
```

#### Title:
Change the title:
```python
	substitution_map = {
		'title': 'the title of my map'}
```
## What happens
The script will print the pdf using the qpt template based on whatever layers are loaded in the `'single_pdf.qgs'` file.

## Links
Most of the script is from Tim Sutton's example [here](http://kartoza.com/how-to-create-a-qgis-pdf-report-with-a-few-lines-of-python/): 
