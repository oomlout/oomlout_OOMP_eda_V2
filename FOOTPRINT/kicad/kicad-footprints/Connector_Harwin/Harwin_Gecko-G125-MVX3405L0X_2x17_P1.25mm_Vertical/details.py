
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Harwin"
    oIndex = "Harwin_Gecko-G125-MVX3405L0X_2x17_P1.25mm_Vertical"
    hexID = "FZKCNHARWINHARWINGECKOG125MVX345LX2X17P125VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Harwin_Gecko-G125-MVX3405L0X_2x17_P1.25mm_Vertical', 'description': 'Harwin Gecko Connector, 34 pins, dual row male, vertical entry, no latches, PN:G125-MVX3405L0X', 'tags': 'connector harwin gecko', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Harwin.3dshapes/Harwin_Gecko-G125-MVX3405L0X_2x17_P1.25mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_Harwin : Harwin_Gecko-G125-MVX3405L0X_2x17_P1.25mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

