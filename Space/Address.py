###############################################################################
# Deals with addresses
###############################################################################
import re

def shorten_rd(address):
    '''Completes the road type. I.e. Rd becomes Road, st becomes Street as per Google etc.'''
    address = address.title()
    address = re.sub(r" Street(?=$| [NE(So|S$)(We|W$)])", ' St', address)
    address = re.sub(r" Road(?=$| [NE(So|S$)(We|W$)])", ' Rd', address)
    address = re.sub(r"(?<!The) Avenue(?=$| [NE(So|S$)(We|W$)])", ' Ave', address)
    address = re.sub(r" Close(?=$| [NE(So|S$)(We|W$)])", ' Cl', address)
    address = re.sub(r" Court(?=$| [NE(So|S$)(We|W$)])", ' Ct', address)
    address = re.sub(r"(?<!The) Crescent(?=$| [NE(So|S$)(We|W$)])", ' Cres', address)
    address = re.sub(r" Boulevarde?(?=$| [NE(So|S$)(We|W$)])", ' Bvd', address)
    address = re.sub(r" Drive(?=$| [NE(So|S$)(We|W$)])", ' Dr', address)
    address = re.sub(r" Lane(?=$| [NE(So|S$)(We|W$)])", ' Ln', address)
    address = re.sub(r" Place(?=$| [NE(So|S$)(We|W$)])", ' Pl', address)
    address = re.sub(r" Square(?=$| [NE(So|S$)(We|W$)])", ' Sq', address)
    address = re.sub(r"(?<!The) Parade(?=$| [NE(So|S$)(We|W$)])", ' Pde', address)
    address = re.sub(r" Circuit(?=$| [NE(So|S$)(We|W$)])", ' Cct', address)
    address = re.sub(r" Highway(?=$| [NE(So|S$)(We|W$)])", ' Hwy', address)
    return address

def lengthen_rd(address):
    address = address.title()
    address = re.sub(r" St(?=$| [NE(So|S$)(We|W$)])", " Street", address)
    address = re.sub(r" Rd(?=$| [NE(So|S$)(We|W$)])", " Road", address)
    address = re.sub(r" Ave(?=$| [NE(So|S$)(We|W$)])", " Avenue", address)
    address = re.sub(r" Cl(?=$| [NE(So|S$)(We|W$)])", " Close", address)
    address = re.sub(r" Ct(?=$| [NE(So|S$)(We|W$)])", " Court", address)
    address = re.sub(r" Cres(?=$| [NE(So|S$)(We|W$)])", " Crescent", address)
    address = re.sub(r" Blvd(?=$| [NE(So|S$)(We|W$)])", " Boulevard", address)
    address = re.sub(r" Bvd(?=$| [NE(So|S$)(We|W$)])", " Boulevard", address)
    address = re.sub(r" Dr(?=$| [NE(So|S$)(We|W$)])", " Drive", address)
    address = re.sub(r" Ln(?=$| [NE(So|S$)(We|W$)])", " Lane", address)
    address = re.sub(r" La(?=$| [NE(So|S$)(We|W$)])", " Lane", address)
    address = re.sub(r" Pl(?=$| [NE(So|S$)(We|W$)])", " Place", address)
    address = re.sub(r" Sq(?=$| [NE(So|S$)(We|W$)])", " Square", address)
    address = re.sub(r" Pde(?=$| [NE(So|S$)(We|W$)])", " Parade", address)
    address = re.sub(r" Cct(?=$| [NE(So|S$)(We|W$)])", " Circuit", address)
    address = re.sub(r" Hwy(?=$| [NE(So|S$)(We|W$)])", " Highway", address)
    return address

class StandardAddr:
    def __init__(self, address, printing=False):
        self.raw_address = address
        '''Checks for unit numbers and street addresses and puts them in the standard format'''
        if printing:
            print("################################")
            print("### Address: |" + address + "|")
        unit_nums = re.findall(r"(?<=Unit )\w?\d+\w?|(?<=U)\d+\w?|\w?\d+\w?(?=\s*/)", address)
        unit_num = unit_nums[0].strip() if len(unit_nums)==1 else ""
        if printing:
            print("Unit Number: |" + unit_num + "|")
        proc_addr = re.sub(r"Unit \w?\d+\w?/?|U\d+\w?/?|\w?\d+\w?\s*/", "", address)
        proc_addr = re.sub(r"^[,\- ]+|[,\- ]+$", "", proc_addr)
        if printing:
            print("Unitless address: |" + proc_addr + "|")
        type_opts = r"Terrace|Way|Walk|St|Rd|Ave|Cl|Ct|Cres|Blvd|Bvd|Dr|Ln|Pl|Sq|Pde|Cct|Hwy"
        road_attrs_pattern = r"(?P<rd_no>\w?\d+(\-\d+)?\w?\s+)(?P<rd_nm>[a-zA-z \-]+)\s+(?P<rd_tp>" \
                                + type_opts + ")"
        road_attrs = re.search(road_attrs_pattern, proc_addr)
        try:
            road_num = road_attrs.group('rd_no').strip()
        except AttributeError:
            road_num = ""
        if printing:
            print("Road number: |" + road_num + "|")
        try:
            road_name = road_attrs.group('rd_nm').strip()
        except AttributeError:
            road_name = ""
        if printing:
            print("Road name: |" + road_name + "|")
        try:
            road_type = road_attrs.group('rd_tp').strip()
        except AttributeError:
            road_type = ""
        if printing:
            print("Road type: |" + road_type + "|")
        road_section_search = re.search(road_attrs_pattern, proc_addr)
        left_over_arr = re.split(road_section_search[0], proc_addr) if road_section_search != None else [proc_addr]
        if printing:
            print("Left Over Array: |" + str(left_over_arr) + "|")
        end_left_over = lengthen_rd(re.sub(r"^[,\- ]+|[,\- ]+$", "", left_over_arr[-1])) if len(left_over_arr) > 1 else ""
        start_left_over = re.sub(r"^[,\- ]+|[,\- ]+$", "", left_over_arr[0])
        post_script_pattern = "^(CN|Central|E|East|EX|Extension|LR|Lower|N|North|NE|North\s+East|NW|North\s+West|S|South|SE|South\s+East|SW|South\s+West|UP|Upper|W|West)[$,]"
        address_post_script_match = re.findall(post_script_pattern, end_left_over)
        address_post_script = "" if len(address_post_script_match) == 0 else address_post_script_match[0].strip()
        if printing:
            print("Address post-script: |" + address_post_script + "|")
        end_left_over = re.sub(post_script_pattern, "", end_left_over).strip()
        if printing:
            print("Start Leftover: |" + start_left_over + "|")
            print("End Leftover: |" + end_left_over + "|")
        left_over = start_left_over + ("" if end_left_over == "" else (", " if start_left_over != "" else "") + end_left_over)
        if printing:
            print("Leftover: |" + left_over + "|")
        unit_seg = (unit_num + "/" if unit_num!="" else "") if road_num != "" else ("Unit " + unit_num if unit_num!="" else "")
        road_seg = ((road_num + " " if road_num!="" else "") + road_name + " " + road_type).strip()
        post_road_seg = " " + address_post_script if address_post_script != "" else ""
        proc_addr = (unit_seg + road_seg) + post_road_seg
        full_proc_addr = proc_addr + ("" if left_over == "" else "; " + left_over)
        if printing:
            print("### Processed Address: |" + proc_addr + "|")
        self.unit_number = unit_num
        self.road_number = road_num
        self.road_name = road_name
        self.road_type = road_type + post_road_seg
        
        self.surplus_address_information = left_over
        self.address_is_valid = road_num != ''
        self.processed_address = proc_addr

print('x')
print('Give me a shell!!!')
