
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_SMD"
    oIndex = "Relay_2P2T_10x6mm_TE_IMxxG"
    hexID = "FZKRELAYSMRELAY2P2T1X6TEIMXXG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_2P2T_10x6mm_TE_IMxxG', 'description': 'Signal Relay, 10x6mm, 2 Form C, Gull Wings, https://www.te.com/commerce/DocumentDelivery/DDEController?Action=showdoc&DocId=Data+Sheet%7F108-98001%7FZ.1%7Fpdf%7FEnglish%7FENG_DS_108-98001_Z.1.pdf', 'tags': 'TE IM-Series Relay DPDT Form C', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_SMD.3dshapes/Relay_2P2T_10x6mm_TE_IMxxG.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Relay_SMD : Relay_2P2T_10x6mm_TE_IMxxG')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

