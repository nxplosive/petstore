from voluptuous import Schema, PREVENT_EXTRA, Required

valid_trainer = Schema({"status": str, "data":[
    {
        # "data": {
        #     "token": str
        # },
        # "meta": {
        #     "exec_time": str,
        #     "query_count": int
        # }
        "city": str,
        "get_history_battle": str,
        "id": str,
        "level": str,
        "photo": str,
        "pokemons": list,
        # "pokemons": [
        #     {
        #         Required("id"): int,
        #         "name": str
        #     }    
        # ],
        "pokemons_alive": list,
        "pokemons_in_pokeballs": list,
        "trainer_name": str,
        "is_premium": False,
        "premium_duration": int
    }]},
    extra=PREVENT_EXTRA,
    required=True    
)