import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))