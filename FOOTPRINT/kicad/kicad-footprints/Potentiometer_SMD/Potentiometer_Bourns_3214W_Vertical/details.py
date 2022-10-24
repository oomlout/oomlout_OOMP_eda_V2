
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Potentiometer_SMD"
    oIndex = "Potentiometer_Bourns_3214W_Vertical"
    hexID = "FZKPOTENTIOMETERSMPOTENTIOMETERBOURNS3214WVERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Potentiometer_Bourns_3214W_Vertical', 'description': 'Potentiometer, vertical, Bourns 3214W, https://www.bourns.com/docs/Product-Datasheets/3214.pdf', 'tags': 'Potentiometer vertical Bourns 3214W', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Potentiometer_SMD.3dshapes/Potentiometer_Bourns_3214W_Vertical.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Potentiometer_SMD : Potentiometer_Bourns_3214W_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

