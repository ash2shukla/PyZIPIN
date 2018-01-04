# PyZIPIN : Python module for ZIP codes of India #

decode: Convert ZIP to Information(District, State etc.).
encode: Convert District to ZIP.

return types are in JSON strings. use after loading with json module's loads


	import PyZIPIN as PZ
	from json import loads

	PZ.decode("209801")

	# '{"officename": "Itauli B.O", "pincode": "209801", "officetype": "B.O", "Deliverystatus": "Delivery", "divisionname": "Kanpur
	# Moffusil", "regionname": "Kanpur", "circlename": "Uttar Pradesh", "taluk": "Unnao", "districtname": "Unnao", "statename":
	# "UTTAR PRADESH"}'

	PZ.encode("Unnao")

	# '{"pincode": "209831", "officename": "Atesuwa B.O"}'

	print(loads(PZ.encode('Unnao'))['pincode'])

	# 209831


One ZIP may belong to more than one offices so to list all the results matching pass additional argument all_results = True to both of the functions.

	PZ.encode("Unnao",all_results=True)

	# '[{"pincode": "209831", "officename": "Atesuwa B.O"}, {"pincode": "209863", "officename": "Dodiya Khera B.O"},
	# .... {"pincode": "209801", "officename": "Unnao H.O"}]'
