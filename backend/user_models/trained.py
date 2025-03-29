import torch

class TrainedModel:
    @staticmethod
    def save_model(model, path):
        torch.save(model.state_dict(), path)

    @staticmethod
    def load_model(model_class, path):
        model = model_class()
        model.load_state_dict(torch.load(path))
        return model
