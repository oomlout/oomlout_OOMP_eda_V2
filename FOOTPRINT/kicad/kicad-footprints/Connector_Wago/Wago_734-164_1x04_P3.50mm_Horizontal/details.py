
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Wago"
    oIndex = "Wago_734-164_1x04_P3.50mm_Horizontal"
    hexID = "FZKCNWAGOWAGO7341641X4P35HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Wago_734-164_1x04_P3.50mm_Horizontal', 'description': 'Molex 734 Male header (for PCBs); Angled solder pin 1 x 1 mm, 734-164 , 4 Pins (http://www.farnell.com/datasheets/2157639.pdf), generated with kicad-footprint-generator', 'tags': 'connector Wago  top entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Wago.3dshapes/Wago_734-164_1x04_P3.50mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Wago : Wago_734-164_1x04_P3.50mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

