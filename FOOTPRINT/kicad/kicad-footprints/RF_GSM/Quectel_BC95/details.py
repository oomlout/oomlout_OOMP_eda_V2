
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_GSM"
    oIndex = "Quectel_BC95"
    hexID = "FZKGSMQUECTELBC95"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Quectel_BC95', 'description': 'GSM NB-IoT module, 19.9x23.6x2.2mm, https://www.quectel.com/UploadImage/Downlad/Quectel_BC95_Hardware_Design_V1.3.pdf', 'tags': 'GSM NB-IoT module BC95', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_GSM.3dshapes/Quectel_BC95.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('RF_GSM : Quectel_BC95')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

