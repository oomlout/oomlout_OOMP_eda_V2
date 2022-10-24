
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "UCBGA-36_2.5x2.5mm_Layout6x6_P0.4mm"
    hexID = "FZKBGAUCBGA3625X25LAYOUT6X6P4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'UCBGA-36_2.5x2.5mm_Layout6x6_P0.4mm', 'description': 'UCBGA-36, 6x6 raster, 2.5x2.5mm package, pitch 0.4mm; https://www.latticesemi.com/view_document?document_id=213', 'tags': 'BGA 36 0.4', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/UCBGA-36_2.5x2.5mm_Layout6x6_P0.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : UCBGA-36_2.5x2.5mm_Layout6x6_P0.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

