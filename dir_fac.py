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




sig_list=['signal-1', 'signal-2', 'signal-3', 'signal-4', 'signal-5', 'signal-6', 'signal-7', 'signal-8', 'signal-9', 'signal-0', 'signal-A', 'signal-B', 'signal-C', 'signal-D', 'signal-E', 'signal-F', 'signal-G', 'signal-H', 'signal-I', 'signal-J', 'signal-K', 'signal-L', 'signal-M', 'signal-N', 'signal-O', 'signal-P', 'signal-Q', 'signal-R', 'signal-S', 'signal-T', 'signal-U', 'signal-V', 'signal-W', 'signal-X', 'signal-Y', 'signal-Z', 'signal-red', 'signal-green', 'signal-blue', 'signal-yellow', 'signal-pink', 'signal-cyan', 'signal-white', 'signal-grey', 'signal-black', 'signal-check', 'signal-info', 'signal-dot'] 