# gclid timestamp decoder

decoding timestamp from Google gclid using Protocol Buffers.

## overview

message formats are defined in `.proto` files. each field in the message has a unique numbered tag (immutable once message type is in use).

running the compiler on a `.proto` generates code in our chosen language (e.g. Python). with regards to Python:

> a module is generated with a static descriptor of each message type, which is then used with a metaclass to create the necessary Python data accesss class at runtime.

compiling the `.proto` using an example file we already pre-defined:

    protoc -I=$REPO_DIR --python_out=$DST_DIR $REPO_DIR/example.proto

this generates example_pb2.py in the specified destination.

## additional presteps for base64 decode

removing trailing bytes doesn't work, we will end up getting

    google.protobuf.message.DecodeError: Truncated message.

instead, we resort to padding with `=` so we get the gclid to a multiple of 4 before decoding.

## requires

- [Protocol Buffers 2.6](https://github.com/google/protobuf/releases/tag/v2.6.0)

## install

    pip install gclid-timestamp-decoder

## usage

    >>> from gclid_timestamp_decoder.decode import get_timestamp_from_gclid
    >>> get_timestamp_from_gclid("CKSDxc_qhLkCFQyk4AodO24Arg")
    '2013-08-17 23:50:17'


## references

- [Protocol Buffers][2]

- [Protocol Buffers Language Guide][3]

- [Protocol Buffer Basics: Python][4]

- [How to decode the gclid parameter in Google Adwords][1]

## author

Contact [kenny@machinesung.com](mailto:kenny@machinesung.com)

[1]: http://blog.deedpolloffice.com/articles/decoding-gclid-parameter
[2]: https://developers.google.com/protocol-buffers/docs/overview
[3]: https://developers.google.com/protocol-buffers/docs/proto
[4]: https://developers.google.com/protocol-buffers/docs/pythontutorial
