
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Crystal_SMD_EuroQuartz_MT-4Pin_3.2x2.5mm"
    hexID = "FZKXXSMEUROQUARTZMT4PIN32X25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Crystal_SMD_EuroQuartz_MT-4Pin_3.2x2.5mm', 'description': 'SMD Crystal EuroQuartz MT series http://cdn-reichelt.de/documents/datenblatt/B400/MT.pdf, 3.2x2.5mm^2 package', 'tags': 'SMD SMT crystal', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_SMD_EuroQuartz_MT-4Pin_3.2x2.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Crystal : Crystal_SMD_EuroQuartz_MT-4Pin_3.2x2.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

