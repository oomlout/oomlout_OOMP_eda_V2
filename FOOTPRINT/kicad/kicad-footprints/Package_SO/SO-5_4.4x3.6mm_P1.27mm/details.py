
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SO-5_4.4x3.6mm_P1.27mm"
    hexID = "FZKSOSO544X36P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SO-5_4.4x3.6mm_P1.27mm', 'description': '5-Lead Plastic Small Outline (SO), see https://docs.broadcom.com/cs/Satellite?blobcol=urldata&blobheader=application%2Fpdf&blobheadername1=Content-Disposition&blobheadername2=Content-Type&blobheadername3=MDT-Type&blobheadervalue1=attachment%3Bfilename%3DIPD-Selection-Guide_AV00-0254EN_030617.pdf&blobheadervalue2=application%2Fx-download&blobheadervalue3=abinary%253B%2Bcharset%253DUTF-8&blobkey=id&blobnocache=true&blobtable=MungoBlobs&blobwhere=1430884105675&ssbinary=true', 'tags': 'SO SOIC 1.27', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SO-5_4.4x3.6mm_P1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : SO-5_4.4x3.6mm_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

