
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_GSM"
    oIndex = "Quectel_M95"
    hexID = "FZKGSMQUECTELM95"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Quectel_M95', 'description': 'Quad-Band GSM/GPRS module, 19.9x23.6x2.65mm, https://www.quectel.com/UploadImage/Downlad/M95_Hardware_Design_V1.3.pdf', 'tags': 'GSM Module M95', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_GSM.3dshapes/Quectel_M95.wrl', 'pins': {'type': 'smd', 'shape': 'oval'}})
    newPart['name'].append('RF_GSM : Quectel_M95')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

