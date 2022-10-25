
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Wago"
    oIndex = "Wago_734-140_1x10_P3.50mm_Vertical"
    hexID = "FZKCNWAGOWAGO734141X1P35VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Wago_734-140_1x10_P3.50mm_Vertical', 'description': 'Molex 734 Male header (for PCBs); Straight solder pin 1 x 1 mm, 734-140 , 10 Pins (http://www.farnell.com/datasheets/2157639.pdf), generated with kicad-footprint-generator', 'tags': 'connector Wago  side entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Wago.3dshapes/Wago_734-140_1x10_P3.50mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Wago : Wago_734-140_1x10_P3.50mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

