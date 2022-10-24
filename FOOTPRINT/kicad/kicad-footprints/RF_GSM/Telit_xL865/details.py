
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_GSM"
    oIndex = "Telit_xL865"
    hexID = "FZKGSMTELITXL865"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Telit_xL865', 'description': 'Telit xL865 familly footprint, http://www.telit.com/fileadmin/user_upload/products/Downloads/3G/Telit_UL865_Hardware_User_Guide_r8.pdf ', 'tags': 'xL865 gsm umts', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_GSM.3dshapes/Telit_xL865.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('RF_GSM : Telit_xL865')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

