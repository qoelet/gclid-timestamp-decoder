import base64
import datetime
import gclid_pb2

def decode(gclid):
    decoded_gclid = base64.urlsafe_b64decode(gclid + '=' * (4 - len(gclid) % 4))
    g = gclid_pb2.Gclid()
    g.ParseFromString(decoded_gclid)
    return g

def convert_to_dt(g):
    return datetime.datetime.fromtimestamp(g.timestamp / 1000000).strftime('%Y-%m-%d %H:%M:%S')

def get_timestamp_from_gclid(gclid):
    return convert_to_dt(decode(gclid))
