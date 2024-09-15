"""
Pipeline class will serve the main pipeline i.e it will fetch the data from different pluggins, 
it will serve as input to the Finllm and black litterman model. The output of this class will be an
updated model, which a user can interact with through APIs or UI.

This process can be run manually or as a cron job for regular update.
"""


class DataPipeline:

    """
    DataPipeline class will initiate data gathering from different pluggins under `Collector` and
    prepare different sources of data from different sources and make it homogeneous, and serve as the single
    source of input for different models under `MLModel` and `FinModle`
    """

    def __init__(self):
        pass


class Database:
    """
    Create or Use an existing in-memory persistent database
    """
    def __init__(self):
        pass        


class LLMPipeline(DataPipeline):

    def __init__(self):
        pass


class BLPipeline(DataPipeline):

    def __init__(self):
        pass


class CompletePipeline(BLPipeline, LLMPipeline):

    def __init__(self):
        pass
        



