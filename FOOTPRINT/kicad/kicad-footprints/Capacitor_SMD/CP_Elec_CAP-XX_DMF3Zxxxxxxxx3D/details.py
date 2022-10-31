
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_SMD"
    oIndex = "CP_Elec_CAP-XX_DMF3Zxxxxxxxx3D"
    hexID = "FZKCAPACITORSMCPELECCAPXXDMF3ZXXXXXXXX3D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'CP_Elec_CAP-XX_DMF3Zxxxxxxxx3D', 'description': '5.5V, 470mF supercapacitor, 45mohm, -40ºC to +70ºC, https://www.cap-xx.com/wp-content/uploads/datasheets/CAP-XX-DMF470mF-Datasheet.pdf', 'tags': 'supercap', 'attributeType': None, 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_SMD.3dshapes/CP_Elec_CAP-XX_DMF3Zxxxxxxxx3D.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Capacitor_SMD : CP_Elec_CAP-XX_DMF3Zxxxxxxxx3D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

