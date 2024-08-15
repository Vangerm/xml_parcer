import xml.etree.ElementTree as ET
import csv


def indent(elem, level=0):
    '''создает красивый xml c отступами'''
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def app_cis():
    flag_first_chek = True
    with open('1.csv', encoding='utf-8') as f:
        lines = csv.reader(f)
        for line in lines:
            new_item = ET.Element('cis')
            if flag_first_chek:
                new_item.text = line[0].strip()[1:]
                flag_first_chek = False
            else:
                new_item.text = line[0].strip()
            root[0][1].insert(1, new_item)
    return None


if __name__ == '__main__':
    tree = ET.parse('Формирование_наборов.xml')
    root = tree.getroot()

    app_cis()

    indent(root)
    tree.write('output.xml', encoding="utf-8", xml_declaration=True)
