body_dir = {'blueprint': {'icons': [{'signal': {'type': 'item', 'name': 'small-lamp'}, 'index': 1}], 'entities': [], 'item': 'blueprint', 'version': 73019555840}}

led_dir={'entity_number': 1, 'name': 'small-lamp', 'position': {'x': -1, 'y': 0}, 
            'control_behavior': {'circuit_condition': {'first_signal': {'type': 'virtual', 'name': 'signal-0'}, 'constant': 1, 'comparator': '='}}, 'connections': {'1': {'green': [{'entity_id': 2}, {'entity_id': 4}]}}}

pow_dir={ "entity_number": 1,
          "name": "medium-electric-pole",
          "position": {
                    "x": -4,
                    "y": -4
                }
            }


cmp_dir= {
                "entity_number": 3,
                "name": "decider-combinator",
                "position": {
                    "x": 1,
                    "y": -1.5
                },
                "control_behavior": {
                    "decider_conditions": {
                        "first_signal": {
                            "type": "virtual",
                            "name": "signal-red"
                        },
                        "constant": 1,
                        "comparator": "=",
                        "output_signal": {
                            "type": "virtual",
                            "name": "signal-everything"
                        },
                        "copy_count_from_input": True
                    }
                },
                "connections": {
                    "1": {
                        "red": [
                            {
                                "entity_id": 2,
                                "circuit_id": 1
                            }
                        ],
                        "green": [
                            {
                                "entity_id": 6
                            }
                        ]
                    },
                    "2": {
                        "green": [
                            {
                                "entity_id": 2,
                                "circuit_id": 2
                            }
                        ]
                    }
                }
            }



cost_dir = {
                "entity_number": 5,
                "name": "constant-combinator",
                "position": {
                    "x": 1,
                    "y": 0
                },
                "direction": 2,
                "control_behavior": {
                    "filters": [
                        {
                            "signal": {
                                "type": "virtual",
                                "name": "signal-0"
                            },
                            "count": 1,
                            "index": 1
                        }, {
                            "signal": {
                                "type": "virtual",
                                "name": "signal-0"
                            },
                            "count": 1,
                            "index": 2
                        }, {
                            "signal": {
                                "type": "virtual",
                                "name": "signal-0"
                            },
                            "count": 1,
                            "index": 3
                        }, {
                            "signal": {
                                "type": "virtual",
                                "name": "signal-0"
                            },
                            "count": 1,
                            "index": 4
                        }
                    ]
                },
                "connections": {
                    "1": {
                        "green": [
                            {
                                "entity_id": 4
                            }, {
                                "entity_id": 7
                            }
                        ]
                    }
                }
            }





cal_dir ={
                "entity_number": 11,
                "name": "arithmetic-combinator",
                "position": {
                    "x": -4.5,
                    "y": 1
                },
                "direction": 2,
                "control_behavior": {
                    "arithmetic_conditions": {
                        "first_signal": {
                            "type": "virtual",
                            "name": "signal-each"
                        },
                        "second_constant": 31,
                        "operation": ">>",
                        "output_signal": {
                            "type": "virtual",
                            "name": "signal-each"
                        }
                    }
                },
                "connections": {
                    "1": {
                        "green": [
                            {
                                "entity_id": 4,
                                "circuit_id": 2
                            }
                        ]
                    },
                    "2": {
                        "green": [
                            {
                                "entity_id": 4,
                                "circuit_id": 1
                            }
                        ]
                    }
                }
            }




sig_list=[['virtual', 'signal-1'], ['virtual', 'signal-2'], ['virtual', 'signal-3'], ['virtual', 'signal-4'], ['virtual', 'signal-5'], ['virtual', 'signal-6'], ['virtual', 'signal-7'], ['virtual', 'signal-8'], ['virtual', 'signal-9'], ['virtual', 'signal-0'], ['virtual', 'signal-A'], ['virtual', 'signal-B'], ['virtual', 'signal-C'], ['virtual', 'signal-D'], ['virtual', 'signal-E'], ['virtual', 'signal-F'], ['virtual', 'signal-G'], ['virtual', 'signal-H'], ['virtual', 'signal-I'], ['virtual', 'signal-J'], ['virtual', 'signal-K'], ['virtual', 'signal-L'], ['virtual', 'signal-M'], ['virtual', 'signal-N'], ['virtual', 'signal-O'], ['virtual', 'signal-P'], ['virtual', 'signal-Q'], ['virtual', 'signal-R'], ['virtual', 'signal-S'], ['virtual', 'signal-T'], ['virtual', 'signal-U'], ['virtual', 'signal-V'], ['virtual', 'signal-W'], ['virtual', 'signal-X'], ['virtual', 'signal-Y'], ['virtual', 'signal-Z'], ['virtual', 'signal-green'], ['virtual', 'signal-blue'], ['virtual', 'signal-yellow'], ['virtual', 'signal-pink'], ['virtual', 'signal-cyan'], ['virtual', 'signal-white'], ['virtual', 'signal-grey'], ['virtual', 'signal-black'], ['virtual', 'signal-check'], ['virtual', 'signal-info'], ['virtual', 'signal-dot'], ['item', 'wooden-chest'], ['item', 'iron-chest'], ['item', 'steel-chest'], ['item', 'transport-belt'], ['item', 'storage-tank'], ['item', 'express-transport-belt'], ['item', 'fast-transport-belt'], ['item', 'fast-underground-belt'], ['item', 'underground-belt'], ['item', 'splitter'], ['item', 'express-underground-belt'], ['item', 'express-splitter'], ['item', 'fast-splitter'], ['item', 'inserter'], ['item', 'burner-inserter'], ['item', 'fast-inserter'], ['item', 'long-handed-inserter'], ['item', 'stack-inserter'], ['item', 'filter-inserter'], ['item', 'small-electric-pole'], ['item', 'stack-filter-inserter'], ['item', 'big-electric-pole'], ['item', 'medium-electric-pole'], ['item', 'pipe'], ['item', 'substation'], ['item', 'pump'], ['item', 'pipe-to-ground'], ['item', 'train-stop'], ['item', 'rail'], ['item', 'rail-chain-signal'], ['item', 'rail-signal'], ['item', 'cargo-wagon'], ['item', 'locomotive'], ['item', 'artillery-wagon'], ['item', 'fluid-wagon'], ['item', 'tank'], ['item', 'car'], ['item', 'construction-robot'], ['item', 'logistic-robot'], ['item', 'logistic-chest-passive-provider'], ['item', 'logistic-chest-active-provider'], ['item', 'logistic-chest-buffer'], ['item', 'logistic-chest-storage'], ['item', 'roboport'], ['item', 'logistic-chest-requester'], ['item', 'red-wire'], ['item', 'small-lamp'], ['item', 'arithmetic-combinator'], ['item', 'green-wire'], ['item', 'power-switch'], ['item', 'constant-combinator'], ['item', 'stone-brick'], ['item', 'programmable-speaker'], ['item', 'hazard-concrete'], ['item', 'concrete'], ['item', 'refined-hazard-concrete'], ['item', 'refined-concrete'], ['item', 'cliff-explosives'], ['item', 'landfill'], ['item', 'repair-pack'], ['item', 'boiler'], ['item', 'solar-panel'], ['item', 'accumulator'], ['item', 'nuclear-reactor'], ['item', 'heat-pipe'], ['item', 'steam-turbine'], ['item', 'burner-mining-drill'], ['item', 'electric-mining-drill'], ['item', 'offshore-pump'], ['item', 'pumpjack'], ['item', 'stone-furnace'], ['item', 'steel-furnace'], ['item', 'electric-furnace'], ['item', 'assembling-machine-1'], ['item', 'assembling-machine-2'], ['item', 'assembling-machine-3'], ['item', 'oil-refinery'], ['item', 'chemical-plant'], ['item', 'centrifuge'], ['item', 'lab'], ['item', 'beacon'], ['item', 'speed-module'], ['item', 'speed-module-2'], ['item', 'effectivity-module'], ['item', 'speed-module-3'], ['item', 'effectivity-module-3'], ['item', 'effectivity-module-2'], ['item', 'productivity-module-2'], ['item', 'productivity-module'], ['item', 'productivity-module-3'], ['item', 'coal'], ['item', 'wood'], ['item', 'iron-ore'], ['item', 'stone'], ['item', 'uranium-ore'], ['item', 'copper-ore'], ['item', 'iron-plate'], ['item', 'raw-fish'], ['item', 'solid-fuel'], ['item', 'copper-plate'], ['item', 'plastic-bar'], ['item', 'steel-plate'], ['item', 'battery'], ['item', 'sulfur'], ['item', 'crude-oil-barrel'], ['item', 'explosives'], ['item', 'light-oil-barrel'], ['item', 'heavy-oil-barrel'], ['item', 'petroleum-gas-barrel'], ['item', 'lubricant-barrel'], ['item', 'water-barrel'], ['item', 'sulfuric-acid-barrel'], ['item', 'iron-stick'], ['item', 'copper-cable'], ['item', 'empty-barrel'], ['item', 'iron-gear-wheel'], ['item', 'advanced-circuit'], ['item', 'electronic-circuit'], ['item', 'engine-unit'], ['item', 'processing-unit'], ['item', 'flying-robot-frame'], ['item', 'electric-engine-unit'], ['item', 'rocket-control-unit'], ['item', 'satellite'], ['item', 'rocket-fuel'], ['item', 'low-density-structure'], ['item', 'uranium-235'], ['item', 'nuclear-fuel'], ['item', 'uranium-fuel-cell'], ['item', 'uranium-238'], ['item', 'automation-science-pack'], ['item', 'used-up-uranium-fuel-cell'], ['item', 'military-science-pack'], ['item', 'logistic-science-pack'], ['item', 'production-science-pack'], ['item', 'chemical-science-pack'], ['item', 'space-science-pack'], ['item', 'utility-science-pack']]