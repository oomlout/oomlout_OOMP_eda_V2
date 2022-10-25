
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_THT"
    oIndex = "Diode_Bridge_DIP-4_W7.62mm_P5.08mm"
    hexID = "FZKDDIODEBRIDGEDIP4W762P58"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Diode_Bridge_DIP-4_W7.62mm_P5.08mm', 'description': '4-lead dip package for diode bridges, row spacing 7.62 mm (300 mils), see http://cdn-reichelt.de/documents/datenblatt/A400/HDBL101G_20SERIES-TSC.pdf', 'tags': 'DIL DIP PDIP 5.08mm 7.62mm 300mil', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/Diode_Bridge_DIP-4_W7.62mm_P5.08mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Diode_THT : Diode_Bridge_DIP-4_W7.62mm_P5.08mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

