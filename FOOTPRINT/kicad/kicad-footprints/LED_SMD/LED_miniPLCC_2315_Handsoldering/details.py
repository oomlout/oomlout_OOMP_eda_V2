
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_SMD"
    oIndex = "LED_miniPLCC_2315_Handsoldering"
    hexID = "FZKLSMLMPLCC2315HANDSOLDERING"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_miniPLCC_2315_Handsoldering', 'description': 'https://docs.broadcom.com/cs/Satellite?blobcol=urldata&blobheader=application%2Fpdf&blobheadername1=Content-Disposition&blobheadername2=Content-Type&blobheadername3=MDT-Type&blobheadervalue1=attachment%3Bfilename%3DAV02-2205EN_DS_ASMT-TxBM_2014-05-09.pdf&blobheadervalue2=application%2Fx-download&blobheadervalue3=abinary%253B%2Bcharset%253DUTF-8&blobkey=id&blobnocache=true&blobtable=MungoBlobs&blobwhere=1430858274704&ssbinary=true', 'tags': 'LED', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_miniPLCC_2315.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('LED_SMD : LED_miniPLCC_2315_Handsoldering')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

