from pytest_voluptuous import S

from common.api.trainers import TrainerApi
from common.helper.schema.trainer import valid_trainer


class TestTrainers():
    
    def test_get_trainer(self):
    
        trainer_api = TrainerApi()
        response = trainer_api.get_trainer(trainer_id=4052)
    
        trainer_api.status_code_should_be(expected_code=200)
    
        assert S(valid_trainer) == response.response.json()