
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "UCBGA-81_4x4mm_Layout9x9_P0.4mm"
    hexID = "FZKBGAUCBGA814X4LAYOUT9X9P4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'UCBGA-81_4x4mm_Layout9x9_P0.4mm', 'description': 'UCBGA-81, 9x9 raster, 4x4mm package, pitch 0.4mm; https://www.latticesemi.com/view_document?document_id=213', 'tags': 'BGA 81 0.4', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/UCBGA-81_4x4mm_Layout9x9_P0.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : UCBGA-81_4x4mm_Layout9x9_P0.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

