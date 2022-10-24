
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_SMD"
    oIndex = "LED_Dialight_591"
    hexID = "FZKLSMLDIALIGHT591"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_Dialight_591', 'description': 'LED SMD 3mm Right Angle series (http://www.dialightsignalsandcomponents.com/Assets/Drawings/2D_Drawings_DrawingDetailedSpec/C17354.pdf)', 'tags': 'LED Dialight 591', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_Dialight_591.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('LED_SMD : LED_Dialight_591')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

