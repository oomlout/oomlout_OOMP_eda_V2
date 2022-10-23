
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Harwin"
    oIndex = "Harwin_LTek-Male_03_P2.00mm_Vertical"
    hexID = "FZKCNHARWINHARWINLTEKMALE3P2VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Harwin_LTek-Male_03_P2.00mm_Vertical', 'description': 'Harwin LTek Connector, 3 pins, single row male, vertical entry', 'tags': 'connector harwin ltek M80', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Harwin.3dshapes/Harwin_LTek-Male_03_P2.00mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_Harwin : Harwin_LTek-Male_03_P2.00mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

