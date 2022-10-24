
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Potentiometer_SMD"
    oIndex = "Potentiometer_Bourns_PRS11S_Vertical"
    hexID = "FZKPOTENTIOMETERSMPOTENTIOMETERBOURNSPRS11SVERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Potentiometer_Bourns_PRS11S_Vertical', 'description': 'Potentiometer, vertical, Bourns PRS11S, http://www.bourns.com/docs/Product-Datasheets/PRS11S.pdf', 'tags': 'Potentiometer vertical Bourns PRS11S', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Potentiometer_SMD.3dshapes/Potentiometer_Bourns_PRS11S_Vertical.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Potentiometer_SMD : Potentiometer_Bourns_PRS11S_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

