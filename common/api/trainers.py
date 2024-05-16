from common.api.basic import API


class TrainerApi(API):

    def get_trainer(self, trainer_id: int = None):
        url = f'{self.url}/trainers'
        return self.get(url=url, params={'trainer_id': trainer_id})