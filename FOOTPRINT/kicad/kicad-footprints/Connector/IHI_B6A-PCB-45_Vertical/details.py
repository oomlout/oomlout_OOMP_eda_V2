
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector"
    oIndex = "IHI_B6A-PCB-45_Vertical"
    hexID = "FZKCNIHIB6APCB45VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'IHI_B6A-PCB-45_Vertical', 'description': 'https://lugsdirect.com/PDF_Webprint/B6A-PCB-45-XX(-X).pdf', 'tags': 'connector IHI B6A-PCB-45', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector.3dshapes/IHI_B6A-PCB-45_Vertical.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector : IHI_B6A-PCB-45_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

