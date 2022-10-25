
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_GSM"
    oIndex = "Quectel_BC66"
    hexID = "FZKGSMQUECTELBC66"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Quectel_BC66', 'description': 'GSM NB-IoT module, 15.8x17.7x2mm, https://www.quectel.com/UploadImage/Downlad/Quectel_BC66_Hardware_Design_V1.1.pdf', 'tags': 'GSM NB-IoT Module BC66 M66', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_GSM.3dshapes/Quectel_BC66.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('RF_GSM : Quectel_BC66')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

