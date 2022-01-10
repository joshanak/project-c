#!/usr/bin/env python
'''
    Parse a MAVLink protocol XML file and generate a Java implementation
    
    Copyright Andrew Tridgell 2011
    Released under GNU GPL version 3 or later
    '''

import sys, textwrap, os, time
from . import mavparse, mavtemplate

t = mavtemplate.MAVTemplate()

def generate_enums(basename, xml):
    '''generate main header per XML file'''
    directory = os.path.join(basename, '''enums''')
    mavparse.mkdir_p(directory)
    for en in xml.enum:
        f = open(os.path.join(directory, en.name+".java"), mode='w')
        t.write(f, '''
/* AUTO-GENERATED FILE.  DO NOT MODIFY.
 *
 * This class was automatically generated by the
 * java mavlink generator tool. It should not be modified by hand.
 */

package com.MAVLink.enums;

/** 
* ${description}
*/
public class ${name} {
${{entry:   public static final int ${name} = ${value}; /* ${description} |${{param:${description}| }} */
}}
}
            ''', en)
        f.close()



def generate_CRC(directory, xml):
    # and message CRCs array
    xml.message_crcs_array = ''
    for msgid in range(256):
        crc = xml.message_crcs.get(msgid, 0)
        xml.message_crcs_array += '%u, ' % crc
    xml.message_crcs_array = xml.message_crcs_array[:-2]
    
    f = open(os.path.join(directory, "CRC.java"), mode='w')
    t.write(f,'''
/* AUTO-GENERATED FILE.  DO NOT MODIFY.
 *
 * This class was automatically generated by the
 * java mavlink generator tool. It should not be modified by hand.
 */

package com.MAVLink.${basename};

/**
* X.25 CRC calculation for MAVlink messages. The checksum must be initialized,
* updated with witch field of the message, and then finished with the message
* id.
*
*/
public class CRC {
    private static final int[] MAVLINK_MESSAGE_CRCS = {${message_crcs_array}};
    private static final int CRC_INIT_VALUE = 0xffff;
    private int crcValue;

    /**
    * Accumulate the X.25 CRC by adding one char at a time.
    *
    * The checksum function adds the hash of one char at a time to the 16 bit
    * checksum (uint16_t).
    *
    * @param data
    *            new char to hash
    **/
    public  void update_checksum(int data) {
        data = data & 0xff; //cast because we want an unsigned type
        int tmp = data ^ (crcValue & 0xff);
        tmp ^= (tmp << 4) & 0xff;
        crcValue = ((crcValue >> 8) & 0xff) ^ (tmp << 8) ^ (tmp << 3) ^ ((tmp >> 4) & 0xf);
    }

    /**
    * Finish the CRC calculation of a message, by running the CRC with the
    * Magic Byte. This Magic byte has been defined in MAVlink v1.0.
    *
    * @param msgid
    *            The message id number
    */
    public void finish_checksum(int msgid) {
        update_checksum(MAVLINK_MESSAGE_CRCS[msgid]);
    }

    /**
    * Initialize the buffer for the X.25 CRC
    *
    */
    public void start_checksum() {
        crcValue = CRC_INIT_VALUE;
    }

    public int getMSB() {
        return ((crcValue >> 8) & 0xff);
    }

    public int getLSB() {
        return (crcValue & 0xff);
    }

    public CRC() {
        start_checksum();
    }

}
        ''',xml)
    
    f.close()


def generate_message_h(directory, m):
    '''generate per-message header for a XML file'''
    f = open(os.path.join(directory, 'msg_%s.java' % m.name_lower), mode='w')

    path=directory.split('/')
    t.write(f, '''
/* AUTO-GENERATED FILE.  DO NOT MODIFY.
 *
 * This class was automatically generated by the
 * java mavlink generator tool. It should not be modified by hand.
 */

// MESSAGE ${name} PACKING
package com.MAVLink.%s;
import com.MAVLink.MAVLinkPacket;
import com.MAVLink.Messages.MAVLinkMessage;
import com.MAVLink.Messages.MAVLinkPayload;
        
/**
* ${description}
*/
public class msg_${name_lower} extends MAVLinkMessage{

    public static final int MAVLINK_MSG_ID_${name} = ${id};
    public static final int MAVLINK_MSG_LENGTH = ${wire_length};
    private static final long serialVersionUID = MAVLINK_MSG_ID_${name};


    ${{ordered_fields:  
    /**
    * ${description}
    */
    public ${type} ${name}${array_suffix};
    }}

    /**
    * Generates the payload for a mavlink message for a message of this type
    * @return
    */
    public MAVLinkPacket pack(){
        MAVLinkPacket packet = new MAVLinkPacket(MAVLINK_MSG_LENGTH);
        packet.sysid = 255;
        packet.compid = 190;
        packet.msgid = MAVLINK_MSG_ID_${name};
        ${{ordered_fields:      
        ${packField}
        }}
        return packet;
    }

    /**
    * Decode a ${name_lower} message into this class fields
    *
    * @param payload The message to decode
    */
    public void unpack(MAVLinkPayload payload) {
        payload.resetIndex();
        ${{ordered_fields:      
        ${unpackField}
        }}
    }

    /**
    * Constructor for a new message, just initializes the msgid
    */
    public msg_${name_lower}(){
        msgid = MAVLINK_MSG_ID_${name};
    }

    /**
    * Constructor for a new message, initializes the message with the payload
    * from a mavlink packet
    *
    */
    public msg_${name_lower}(MAVLinkPacket mavLinkPacket){
        this.sysid = mavLinkPacket.sysid;
        this.compid = mavLinkPacket.compid;
        this.msgid = MAVLINK_MSG_ID_${name};
        unpack(mavLinkPacket.payload);        
    }

    ${{ordered_fields: ${getText} }}
    /**
    * Returns a string with the MSG name and data
    */
    public String toString(){
        return "MAVLINK_MSG_ID_${name} -"+${{ordered_fields:" ${name}:"+${name}+}}"";
    }
}
        ''' % path[len(path)-1], m)
    f.close()


def generate_MAVLinkMessage(directory, xml_list):
    f = open(os.path.join(directory, "MAVLinkPacket.java"), mode='w')
    t.write(f, '''
/* AUTO-GENERATED FILE.  DO NOT MODIFY.
 *
 * This class was automatically generated by the
 * java mavlink generator tool. It should not be modified by hand.
 */
        
package com.MAVLink;

import java.io.Serializable;
import com.MAVLink.Messages.MAVLinkPayload;
import com.MAVLink.Messages.MAVLinkMessage;
import com.MAVLink.${basename}.CRC;
import com.MAVLink.common.*;
import com.MAVLink.${basename}.*;

/**
* Common interface for all MAVLink Messages
* Packet Anatomy
* This is the anatomy of one packet. It is inspired by the CAN and SAE AS-4 standards.

* Byte Index  Content              Value       Explanation
* 0            Packet start sign  v1.0: 0xFE   Indicates the start of a new packet.  (v0.9: 0x55)
* 1            Payload length      0 - 255     Indicates length of the following payload.
* 2            Packet sequence     0 - 255     Each component counts up his send sequence. Allows to detect packet loss
* 3            System ID           1 - 255     ID of the SENDING system. Allows to differentiate different MAVs on the same network.
* 4            Component ID        0 - 255     ID of the SENDING component. Allows to differentiate different components of the same system, e.g. the IMU and the autopilot.
* 5            Message ID          0 - 255     ID of the message - the id defines what the payload means and how it should be correctly decoded.
* 6 to (n+6)   Payload             0 - 255     Data of the message, depends on the message id.
* (n+7)to(n+8) Checksum (low byte, high byte)  ITU X.25/SAE AS-4 hash, excluding packet start sign, so bytes 1..(n+6) Note: The checksum also includes MAVLINK_CRC_EXTRA (Number computed from message fields. Protects the packet from decoding a different version of the same packet but with different variables).

* The checksum is the same as used in ITU X.25 and SAE AS-4 standards (CRC-16-CCITT), documented in SAE AS5669A. Please see the MAVLink source code for a documented C-implementation of it. LINK TO CHECKSUM
* The minimum packet length is 8 bytes for acknowledgement packets without payload
* The maximum packet length is 263 bytes for full payload
*
*/
public class MAVLinkPacket implements Serializable {
    private static final long serialVersionUID = 2095947771227815314L;

    public static final int MAVLINK_STX = 254;

    /**
    * Message length. NOT counting STX, LENGTH, SEQ, SYSID, COMPID, MSGID, CRC1 and CRC2
    */
    public final int len;

    /**
    * Message sequence
    */
    public int seq;

    /**
    * ID of the SENDING system. Allows to differentiate different MAVs on the
    * same network.
    */
    public int sysid;

    /**
    * ID of the SENDING component. Allows to differentiate different components
    * of the same system, e.g. the IMU and the autopilot.
    */
    public int compid;

    /**
    * ID of the message - the id defines what the payload means and how it
    * should be correctly decoded.
    */
    public int msgid;

    /**
    * Data of the message, depends on the message id.
    */
    public MAVLinkPayload payload;

    /**
    * ITU X.25/SAE AS-4 hash, excluding packet start sign, so bytes 1..(n+6)
    * Note: The checksum also includes MAVLINK_CRC_EXTRA (Number computed from
    * message fields. Protects the packet from decoding a different version of
    * the same packet but with different variables).
    */
    public CRC crc;

    public MAVLinkPacket(int payloadLength){
        len = payloadLength;
        payload = new MAVLinkPayload(payloadLength);
    }

    /**
    * Check if the size of the Payload is equal to the "len" byte
    */
    public boolean payloadIsFilled() {
        return payload.size() >= len;
    }

    /**
    * Update CRC for this packet.
    */
    public void generateCRC(){
        if(crc == null){
            crc = new CRC();
        }
        else{
            crc.start_checksum();
        }
        
        crc.update_checksum(len);
        crc.update_checksum(seq);
        crc.update_checksum(sysid);
        crc.update_checksum(compid);
        crc.update_checksum(msgid);

        payload.resetIndex();

        final int payloadSize = payload.size();
        for (int i = 0; i < payloadSize; i++) {
            crc.update_checksum(payload.getByte());
        }
        crc.finish_checksum(msgid);
    }

    /**
    * Encode this packet for transmission.
    *
    * @return Array with bytes to be transmitted
    */
    public byte[] encodePacket() {
        byte[] buffer = new byte[6 + len + 2];
        
        int i = 0;
        buffer[i++] = (byte) MAVLINK_STX;
        buffer[i++] = (byte) len;
        buffer[i++] = (byte) seq;
        buffer[i++] = (byte) sysid;
        buffer[i++] = (byte) compid;
        buffer[i++] = (byte) msgid;

        final int payloadSize = payload.size();
        for (int j = 0; j < payloadSize; j++) {
            buffer[i++] = payload.payload.get(j);
        }

        generateCRC();
        buffer[i++] = (byte) (crc.getLSB());
        buffer[i++] = (byte) (crc.getMSB());
        return buffer;
    }

    /**
    * Unpack the data in this packet and return a MAVLink message
    *
    * @return MAVLink message decoded from this packet
    */
    public MAVLinkMessage unpack() {
        switch (msgid) {
        ''', xml_list[0])
    for xml in xml_list:
        t.write(f, '''
            ${{message:     
            case msg_${name_lower}.MAVLINK_MSG_ID_${name}:
                return  new msg_${name_lower}(this);
            }}
            ''',xml)
    f.write('''
            default:
                return null;
        }
    }

}
        
        ''')
    
    f.close()

def copy_fixed_headers(directory, xml):
    '''copy the fixed protocol headers to the target directory'''
    import shutil
    hlist = [ 'Parser.java', 'Messages/MAVLinkMessage.java', 'Messages/MAVLinkPayload.java', 'Messages/MAVLinkStats.java' ]
    basepath = os.path.dirname(os.path.realpath(__file__))
    srcpath = os.path.join(basepath, 'java/lib')
    print("Copying fixed headers")
    for h in hlist:
        src = os.path.realpath(os.path.join(srcpath, h))
        dest = os.path.realpath(os.path.join(directory, h))
        if src == dest:
            continue
        destdir = os.path.realpath(os.path.join(directory, 'Messages'))
        try:
            os.makedirs(destdir)
        except:
            print("Not re-creating Messages directory")
        shutil.copy(src, dest)

class mav_include(object):
    def __init__(self, base):
        self.base = base


def mavfmt(field, typeInfo=False):
    '''work out the struct format for a type'''
    map = {
        'float'    : ('float', 'Float'),
        'double'   : ('double', 'Double'),
        'char'     : ('byte', 'Byte'),
        'int8_t'   : ('byte', 'Byte'),
        'uint8_t'  : ('short', 'UnsignedByte'),
        'uint8_t_mavlink_version'  : ('short', 'UnsignedByte'),
        'int16_t'  : ('short', 'Short'),
        'uint16_t' : ('int', 'UnsignedShort'),
        'int32_t'  : ('int', 'Int'),
        'uint32_t' : ('long', 'UnsignedInt'),
        'int64_t'  : ('long', 'Long'),
        'uint64_t' : ('long', 'UnsignedLong'),
    }
    
    if typeInfo:
        return map[field.type][1]
    else:
        return map[field.type][0]

def generate_one(basename, xml):
    '''generate headers for one XML file'''
    
    directory = os.path.join(basename, xml.basename)
    
    print("Generating Java implementation in directory %s" % directory)
    mavparse.mkdir_p(directory)
    
    if xml.little_endian:
        xml.mavlink_endian = "MAVLINK_LITTLE_ENDIAN"
    else:
        xml.mavlink_endian = "MAVLINK_BIG_ENDIAN"
    
    if xml.crc_extra:
        xml.crc_extra_define = "1"
    else:
        xml.crc_extra_define = "0"
    
    if xml.sort_fields:
        xml.aligned_fields_define = "1"
    else:
        xml.aligned_fields_define = "0"
    
    # work out the included headers
    xml.include_list = []
    for i in xml.include:
        base = i[:-4]
        xml.include_list.append(mav_include(base))
    
    # form message lengths array
    xml.message_lengths_array = ''
    for mlen in xml.message_lengths:
        xml.message_lengths_array += '%u, ' % mlen
    xml.message_lengths_array = xml.message_lengths_array[:-2]
    
    
    
    # form message info array
    xml.message_info_array = ''
    for name in xml.message_names:
        if name is not None:
            xml.message_info_array += 'MAVLINK_MESSAGE_INFO_%s, ' % name
        else:
            # Several C compilers don't accept {NULL} for
            # multi-dimensional arrays and structs
            # feed the compiler a "filled" empty message
            xml.message_info_array += '{"EMPTY",0,{{"","",MAVLINK_TYPE_CHAR,0,0,0}}}, '
    xml.message_info_array = xml.message_info_array[:-2]
    
    # add some extra field attributes for convenience with arrays
    for m in xml.message:
        m.msg_name = m.name
        if xml.crc_extra:
            m.crc_extra_arg = ", %s" % m.crc_extra
        else:
            m.crc_extra_arg = ""
        for f in m.fields:
            if f.print_format is None:
                f.c_print_format = 'NULL'
            else:
                f.c_print_format = '"%s"' % f.print_format
            f.getText = ''
            if f.array_length != 0:
                f.array_suffix = '[] = new %s[%u]' % (mavfmt(f),f.array_length)
                f.array_prefix = '*'
                f.array_tag = '_array'
                f.array_arg = ', %u' % f.array_length
                f.array_return_arg = '%s, %u, ' % (f.name, f.array_length)
                f.array_const = 'const '
                f.decode_left = ''
                f.decode_right = 'm.%s' % (f.name)
                
                f.unpackField = ''' 
        for (int i = 0; i < this.%s.length; i++) {
            this.%s[i] = payload.get%s();
        }
                ''' % (f.name, f.name, mavfmt(f, True) )
                f.packField = '''
        for (int i = 0; i < %s.length; i++) {
            packet.payload.put%s(%s[i]);
        }
                    ''' % (f.name, mavfmt(f, True),f.name)
                f.return_type = 'uint16_t'
                f.get_arg = ', %s *%s' % (f.type, f.name)
                if f.type == 'char':
                    f.c_test_value = '"%s"' % f.test_value
                    f.getText = '''
    /**
    * Sets the buffer of this message with a string, adds the necessary padding
    */
    public void set%s(String str) {
        int len = Math.min(str.length(), %d);
        for (int i=0; i<len; i++) {
            %s[i] = (byte) str.charAt(i);
        }

        for (int i=len; i<%d; i++) {            // padding for the rest of the buffer
            %s[i] = 0;
        }
    }

    /**
    * Gets the message, formated as a string
    */
    public String get%s() {
        String result = "";
        for (int i = 0; i < %d; i++) {
            if (%s[i] != 0)
                result = result + (char) %s[i];
            else
                break;
        }
        return result;

    }
                        ''' % (f.name.title(),f.array_length,f.name,f.array_length,f.name,f.name.title(),f.array_length,f.name,f.name)
                else:
                    test_strings = []
                    for v in f.test_value:
                        test_strings.append(str(v))
                    f.c_test_value = '{ %s }' % ', '.join(test_strings)
            else:
                f.array_suffix = ''
                f.array_prefix = ''
                f.array_tag = ''
                f.array_arg = ''
                f.array_return_arg = ''
                f.array_const = ''
                f.decode_left =  '%s' % (f.name)
                f.decode_right = ''
                f.unpackField = 'this.%s = payload.get%s();' % (f.name, mavfmt(f, True))
                f.packField = 'packet.payload.put%s(%s);' % (mavfmt(f, True),f.name)                   
                
                
                f.get_arg = ''
                f.return_type = f.type
                if f.type == 'char':
                    f.c_test_value = "'%s'" % f.test_value
                elif f.type == 'uint64_t':
                    f.c_test_value = "%sULL" % f.test_value                    
                elif f.type == 'int64_t':
                    f.c_test_value = "%sLL" % f.test_value                    
                else:
                    f.c_test_value = f.test_value
    
    # cope with uint8_t_mavlink_version
    for m in xml.message:
        m.arg_fields = []
        m.array_fields = []
        m.scalar_fields = []
        for f in m.ordered_fields:
            if f.array_length != 0:
                m.array_fields.append(f)
            else:
                m.scalar_fields.append(f)
        for f in m.fields:
            if not f.omit_arg:
                m.arg_fields.append(f)
                f.putname = f.name
            else:
                f.putname = f.const_value
    
    # fix types to java
    for m in xml.message:
        for f in m.ordered_fields:
            f.type = mavfmt(f)
    
    generate_CRC(directory, xml)
    
    for m in xml.message:
        generate_message_h(directory, m)


def generate(basename, xml_list):
    '''generate complete MAVLink Java implemenation'''
    for xml in xml_list:
        generate_one(basename, xml)
        generate_enums(basename, xml)
        generate_MAVLinkMessage(basename, xml_list)
    copy_fixed_headers(basename, xml_list[0])
