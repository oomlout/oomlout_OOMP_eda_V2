
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Harwin"
    oIndex = "Harwin_M20-89020xx_1x20_P2.54mm_Horizontal"
    hexID = "FZKCNHARWINHARWINM2892XX1X2P254HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Harwin_M20-89020xx_1x20_P2.54mm_Horizontal', 'description': 'Harwin Male Horizontal Surface Mount Single Row 2.54mm (0.1 inch) Pitch PCB Connector, M20-89020xx, 20 Pins per row (https://cdn.harwin.com/pdfs/M20-890.pdf), generated with kicad-footprint-generator', 'tags': 'connector Harwin M20-890 horizontal', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Harwin.3dshapes/Harwin_M20-89020xx_1x20_P2.54mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_Harwin : Harwin_M20-89020xx_1x20_P2.54mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

