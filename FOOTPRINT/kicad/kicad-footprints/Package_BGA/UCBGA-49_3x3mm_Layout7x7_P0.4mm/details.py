
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "UCBGA-49_3x3mm_Layout7x7_P0.4mm"
    hexID = "FZKBGAUCBGA493X3LAYOUT7X7P4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'UCBGA-49_3x3mm_Layout7x7_P0.4mm', 'description': 'UCBGA-49, 7x7 raster, 3x3mm package, pitch 0.4mm; https://www.latticesemi.com/view_document?document_id=213', 'tags': 'BGA 49 0.4', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/UCBGA-49_3x3mm_Layout7x7_P0.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : UCBGA-49_3x3mm_Layout7x7_P0.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

