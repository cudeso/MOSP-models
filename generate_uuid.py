#!/usr/bin/env python

import uuid
import json
import sys

jf = sys.argv[1]
with open(jf) as json_file:
	data = json.load(json_file)
	for p in data['measures']:
		old_uuid = p['uuid']
		if not old_uuid:
			new_uuid = str(uuid.uuid4())
			p['uuid'] = new_uuid


#print(data)
with open(jf, 'w') as json_file:
	json.dump(data, json_file, indent=2)
