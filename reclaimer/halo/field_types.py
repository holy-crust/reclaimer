from struct import unpack

from supyr_struct.apps.constants import *
from supyr_struct.field_types import *
from supyr_struct.blocks import *
from .field_type_methods import *


'''These are varients of the standard FieldTypes that have been
slightly modified based on how Halo needs to utilize them.'''
StringVarLen = FieldType(base=StrLatin1, name="HaloRefStr",
                         encoder=encode_tag_ref_str, sizecalc=tag_ref_sizecalc)
FlUTF16StrData = FieldType(base=StrUtf16, name="UTF16StrData",
                           enc=StrUtf16.little.enc, decoder=decode_raw_string,
                           sizecalc=utf_sizecalc)
FlStrUTF16 = FieldType(base=StrUtf16, name="StrUTF16",
                       enc=StrUtf16.little.enc, decoder=decode_string,
                       sizecalc=delim_utf_sizecalc)

#forces little endian integers and float
FlUInt16 = FieldType(
    base=UInt16.little, name="FlUInt16", enc=UInt16.little.enc)
FlUInt32 = FieldType(
    base=UInt32.little, name="FlUInt32", enc=UInt32.little.enc)

FlUEnum16 = FieldType(
    base=UEnum16.little, name="FlUEnum16", enc=UEnum16.little.enc)
FlUEnum32 = FieldType(
    base=UEnum32.little, name="FlUEnum32", enc=UEnum32.little.enc)

FlBool16 = FieldType(
    base=Bool16.little, name="FlBool16", enc=Bool16.little.enc)
FlBool32 = FieldType(
    base=Bool32.little, name="FlBool32", enc=Bool32.little.enc)

FlSInt16 = FieldType(
    base=SInt16.little, name="FlSInt16", enc=SInt16.little.enc)
FlSInt32 = FieldType(
    base=SInt32.little, name="FlSInt32", enc=SInt32.little.enc)

FlSEnum16 = FieldType(
    base=SEnum16.little, name="FlSEnum16", enc=SEnum16.little.enc)
FlSEnum32 = FieldType(
    base=SEnum32.little, name="FlSEnum32", enc=SEnum32.little.enc)

FlFloat = FieldType(base=Float.little, name="FlFloat", enc=Float.little.enc)

'''These FieldTypes exist to easily identify where in a tag
that raw data refs, reflexives, and tag references exist.'''
RawdataRef  = FieldType(base=QStruct, name="RawdataRef")
Reflexive   = FieldType(base=QStruct, name="Reflexive")
TagIndexRef = FieldType(base=Struct, name="TagIndexRef")

#The tag_index is the array that stores all the tag string paths and
#meta datas in a map file. This FieldType exists so the Map_Magic
#can be easily supplied through the keyword argument "Map_Magic"
TagIndex = FieldType(base=Array, name="TagIndex",
                     parser=tag_index_parser, serializer=tag_index_serializer)

Rawdata = FieldType(base=BytearrayRaw, name="Rawdata", parser=rawdata_parser)

StrLatin1Enum = FieldType(base=StrRawLatin1, name="StrLatin1Enum",
                          is_block=True, is_data=True, data_cls=str,
                          sizecalc=sizecalc_wrapper(len_sizecalc),
                          decoder=decoder_wrapper(decode_string),
                          encoder=encoder_wrapper(encode_string),
                          node_cls=EnumBlock, sanitizer=enum_sanitizer)
