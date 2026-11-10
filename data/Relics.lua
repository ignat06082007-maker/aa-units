return {
	relic_dagger = {
		id = "relic_dagger", 
		name = "Steel Shiv", 
		rarity = "Epic", 
		crafting_recipe = {
			ingots_steel = 10
		}, 
		crafting_cost = 4000, 
		_craft_type = "Relics", 
		usage_from_inventory = true, 
		usage = {
			type = "apply_relic"
		}, 
		relic_data = {
			_core_random_buffs_to_roll = 1, 
			_core_damage_type_buffs_random = { {
					damage_type = "physical", 
					mul = {
						min = 0.01, 
						max = 0.04
					}, 
					weight = 1
				}, {
					damage_type = "physical", 
					add_upg = {
						min = 0.5, 
						max = 2
					}, 
					weight = 2
				}, {
					damage_type = "physical", 
					pen = {
						min = 20, 
						max = 40
					}, 
					weight = 2
				} }
		}, 
		item_group = "Relics", 
		unique = true
	}, 
	relic_book = {
		id = "relic_book", 
		name = "Amplifying Codex", 
		rarity = "Epic", 
		crafting_recipe = {
			book_material = 20
		}, 
		crafting_cost = 5000, 
		_craft_type = "Relics", 
		usage_from_inventory = true, 
		usage = {
			type = "apply_relic"
		}, 
		relic_data = {
			_core_random_buffs_to_roll = 1, 
			_core_damage_type_buffs_random = { {
					damage_type = "magic", 
					mul = {
						min = 0.01, 
						max = 0.04
					}, 
					weight = 1
				}, {
					damage_type = "magic", 
					add_upg = {
						min = 0.5, 
						max = 2
					}, 
					weight = 2
				}, {
					damage_type = "magic", 
					pen = {
						min = 20, 
						max = 40
					}, 
					weight = 2
				} }
		}, 
		item_group = "Relics", 
		unique = true
	}, 
	asta_clover = {
		id = "asta_clover", 
		name = "5-Leaf Clover", 
		rarity = "Mythic", 
		flavor = "<font color=\"#921296\"><i>And in the fifth leaf... there lies the devil.</i></font>", 
		usage_from_inventory = true, 
		usage = {
			type = "apply_relic"
		}, 
		crafting_recipe = {
			demon_horns = 25, 
			demon_skull = 25, 
			demon_tail = 25, 
			book_material = 25, 
			ingots_steel = 18, 
			scroll_material = 80
		}, 
		crafting_cost = 10000, 
		_craft_type = "Relics", 
		relic_data = {
			_core_damage_type_buffs_static = { {
					damage_type = "physical", 
					mul = {
						min = 0.02, 
						max = 0.05
					}
				} }, 
			_core_random_buffs_to_roll = 1, 
			_core_damage_type_buffs_random = { {
					damage_type = "dark_damage", 
					mul = {
						min = 0.02, 
						max = 0.08
					}, 
					weight = 1
				}, {
					damage_type = "dark_damage", 
					add_upg = {
						min = 1, 
						max = 3
					}, 
					weight = 1
				}, {
					damage_type = "physical", 
					pen = {
						min = 30, 
						max = 50
					}, 
					weight = 1
				} }, 
			_unique_relic_effects = { {
					id = "asta_clover", 
					static_params = {
						dmg_buff = {
							min = 0.1, 
							max = 0.15
						}
					}
				} }
		}, 
		item_group = "Relics", 
		unique = true
	}, 
	yuno_clover = {
		id = "yuno_clover", 
		name = "Clover Of The Wind", 
		rarity = "Mythic", 
		flavor = "<font color=\"#921296\"><i>\"Like I'd let you catch up to me!\"</i></font>", 
		usage_from_inventory = true, 
		usage = {
			type = "apply_relic"
		}, 
		crafting_recipe = {
			fairy_wings_material = 25, 
			circlet_material = 25, 
			book_material = 25, 
			yuno_blade = 25, 
			ingots_steel = 18, 
			leaf_generic = 80
		}, 
		crafting_cost = 10000, 
		_craft_type = "Relics", 
		relic_data = {
			_core_damage_type_buffs_static = { {
					damage_type = "magic", 
					mul = {
						min = 0.02, 
						max = 0.05
					}
				} }, 
			_core_random_buffs_to_roll = 1, 
			_core_damage_type_buffs_random = { {
					damage_type = "air_damage", 
					mul = {
						min = 0.02, 
						max = 0.08
					}, 
					weight = 1
				}, {
					damage_type = "air_damage", 
					add_upg = {
						min = 1, 
						max = 3
					}, 
					weight = 1
				}, {
					damage_type = "magic", 
					pen = {
						min = 30, 
						max = 50
					}, 
					weight = 1
				} }, 
			_unique_relic_effects = { {
					id = "yuno_clover", 
					static_params = {
						dmg_buff = {
							min = 0.1, 
							max = 0.15
						}
					}
				} }
		}, 
		item_group = "Relics", 
		unique = true
	}, 
	noelle_crown = {
		id = "noelle_crown", 
		name = "Mermaid Crown", 
		rarity = "Mythic", 
		flavor = "<font color=\"#921296\"><i>\"I'm not weak anymore!\"</i></font>", 
		usage_from_inventory = true, 
		usage = {
			type = "apply_relic"
		}, 
		crafting_recipe = {
			demon_horns = 25, 
			demon_skull = 25, 
			circlet_material = 25, 
			book_material = 25, 
			ingots_steel = 18, 
			leaf_generic = 80
		}, 
		crafting_cost = 10000, 
		_craft_type = "Relics", 
		relic_data = {
			_core_damage_type_buffs_static = { {
					damage_type = "magic", 
					mul = {
						min = 0.02, 
						max = 0.05
					}
				} }, 
			_core_random_buffs_to_roll = 1, 
			_core_damage_type_buffs_random = { {
					damage_type = "water_damage", 
					mul = {
						min = 0.02, 
						max = 0.08
					}, 
					weight = 1
				}, {
					damage_type = "water_damage", 
					add_upg = {
						min = 1, 
						max = 3
					}, 
					weight = 1
				}, {
					damage_type = "magic", 
					pen = {
						min = 30, 
						max = 50
					}, 
					weight = 1
				} }, 
			_unique_relic_effects = { {
					id = "noelle_crown", 
					static_params = {
						magic_res_decr = {
							min = 1, 
							max = 4
						}
					}
				} }
		}, 
		item_group = "Relics", 
		unique = true
	}
};