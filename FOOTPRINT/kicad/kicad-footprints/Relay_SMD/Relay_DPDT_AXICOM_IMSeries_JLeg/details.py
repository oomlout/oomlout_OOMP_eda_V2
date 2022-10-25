
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_SMD"
    oIndex = "Relay_DPDT_AXICOM_IMSeries_JLeg"
    hexID = "FZKRELAYSMRELAYDPDTAXICOMIMSERIESJLEG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_DPDT_AXICOM_IMSeries_JLeg', 'description': 'http://www.te.com/commerce/DocumentDelivery/DDEController?Action=showdoc&DocId=Specification+Or+Standard%7F108-98001%7FW5%7Fpdf%7FEnglish%7FENG_SS_108-98001_W5.pdf', 'tags': 'AXICOM IM-Series Relay J JLeg', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_SMD.3dshapes/Relay_DPDT_AXICOM_IMSeries_JLeg.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Relay_SMD : Relay_DPDT_AXICOM_IMSeries_JLeg')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

