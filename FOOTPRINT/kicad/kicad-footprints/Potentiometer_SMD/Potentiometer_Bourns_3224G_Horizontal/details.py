
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Potentiometer_SMD"
    oIndex = "Potentiometer_Bourns_3224G_Horizontal"
    hexID = "FZKPOTENTIOMETERSMPOTENTIOMETERBOURNS3224GHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Potentiometer_Bourns_3224G_Horizontal', 'description': 'Potentiometer, horizontal, Bourns 3224G, https://www.bourns.com/docs/Product-Datasheets/3224.pdf', 'tags': 'Potentiometer horizontal Bourns 3224G', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Potentiometer_SMD.3dshapes/Potentiometer_Bourns_3224G_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Potentiometer_SMD : Potentiometer_Bourns_3224G_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

