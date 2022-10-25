
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Module"
    oIndex = "Digi_XBee_SMT"
    hexID = "FZKRFMODIGIXBEES"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Digi_XBee_SMT', 'description': 'http://www.digi.com/resources/documentation/digidocs/pdfs/90002126.pdf http://ftp1.digi.com/support/documentation/90001020_F.pdf', 'tags': 'Digi XBee SMT RF', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Module.3dshapes/Digi_XBee_SMT.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('RF_Module : Digi_XBee_SMT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

