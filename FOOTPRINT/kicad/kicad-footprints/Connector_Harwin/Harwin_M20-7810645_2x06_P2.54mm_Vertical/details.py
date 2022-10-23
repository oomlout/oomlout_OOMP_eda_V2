
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Harwin"
    oIndex = "Harwin_M20-7810645_2x06_P2.54mm_Vertical"
    hexID = "FZKCNHARWINHARWINM27816452X6P254VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Harwin_M20-7810645_2x06_P2.54mm_Vertical', 'description': 'Harwin Female Vertical Surface Mount Double Row 2.54mm (0.1 inch) Pitch PCB Connector, M20-7810645, 6 Pins per row (https://cdn.harwin.com/pdfs/M20-781.pdf), generated with kicad-footprint-generator', 'tags': 'connector Harwin M20 side entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Harwin.3dshapes/Harwin_M20-7810645_2x06_P2.54mm_Vertical.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Harwin : Harwin_M20-7810645_2x06_P2.54mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

